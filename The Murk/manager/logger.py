from os import environ
from preferences.config import config

def Log(string):
    try:
        user = environ['USERPROFILE']
        f = open(f'{user}\\AppData\\Local\\Microsoft\\Windows\\{str(config.id)}', 'a', encoding='utf-8')
        f.write(string+'\n')
        f.close()
    except:
        pass