# -*- coding: utf-8 -*-

import os
from twisted.web.resource import Resource

class Data(Resource):
	isLeaf = True
	def render_GET(self, request):
		global text
		try:
			text = str(request.args['value'][0]).lower()
			if text != "":
				text_buscar = ("á","é","í","ó","ú","ñ")
				text_replace = ("a","e","i","o","u","n") 
				for i in range(len(text_buscar)):
					text = text.replace(text_buscar[i], text_replace[i])
				if "speak.txt" in os.listdir("/home/pi/seguridad"):
					os.remove("/home/pi/seguridad/speak.txt")
				with open("/home/pi/seguridad/speak.txt","w") as file:
					file.write(text)
		except Exception as e:
			print(e)
			return "Failed"

def main():
    dataFrom = Data()

if __name__ == '__main__':
    main()
