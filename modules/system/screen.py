from PIL import ImageGrab

def Screenshot():
	try:
		screen = ImageGrab.grab()
		screen.save(r'C:\windll\sreenshot.jpg')
	except Exception as e:
		print(e)