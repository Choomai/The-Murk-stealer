from os import environ
from os.path import join
from preferences.config import config

def Log(string) -> None:
    with open(join(environ['LOCALAPPDATA'], str(config.id)), "a", encoding="utf-8") as f:
        return f.write(string + "\n")