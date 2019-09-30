import math, operator
from PIL import Image
from functools import reduce
#from datetime import datetime
#from io import BytesIO
#import requests
import os
import time

def compare(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def recent_file(directorio):
    files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
    creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
    return files[creates_dates.index(max(creates_dates))]

"""def speak(file1, file2):
    global tts
    global text
    image1 = file1
    image2 = file2
    time = datetime.now()
    while True:
        if (datetime.now() - time).seconds >= 20:
            if compare(image1, image2) != 0:
                tts.say(text)
            time = datetime.now()"""

if __name__=='__main__':
    file1 = "/home/pi/seguridad/original.jpg"
    #files2 = requests.get("http://localhost:8082")
    #file2 = "/home/pi/images/2018-05-04_091632.jpg"
    #img = BytesIO(response.content)
    text = "Hola, bienvenido al departamento de informatica!"
    while True:
        try:
            file2 = recent_file("/home/pi/images")
            print(compare(file1,"/home/pi/images/"+file2))
        except Exception as er:
            print(er)
        time.sleep(1)
