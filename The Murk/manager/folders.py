from os import environ, makedirs
from os.path import join
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes
from preferences.config import config


def Folders() -> None:
    try:
        makedirs(config.pathToLogs, exist_ok=True)
        SetFileAttributes(config.pathToLogs, FILE_ATTRIBUTE_HIDDEN)
        with open(join(environ["LOCALAPPDATA"], config.id), "w", encoding="utf-8"): pass
    except: pass