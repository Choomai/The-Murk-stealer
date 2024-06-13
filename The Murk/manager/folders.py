from os import environ, makedirs
from os.path import join
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes
from preferences.config import config


def Folders() -> None:
    user = environ['USERPROFILE']
    try:
        makedirs(join(user, config.pathToLogs), exist_ok=True)
        SetFileAttributes(join(user, config.pathToLogs), FILE_ATTRIBUTE_HIDDEN)
    except: pass