import math, operator
from PIL import Image
from functools import reduce
from datetime import datetime
#import talkey
import os
import subprocess
from time import sleep

Image.LOAD_TRUCATED_IMAGES = True

def compare(file1, file2):
    h1 = file1.histogram()
    h2 = file2.histogram()
    rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def speak(file1, file2):
    global tts
    global text
    global current_time
    if compare(file1,file2) > 700:
        tts.say(text)
        current_time = datetime.now()

def save_page(name):
    sudoPassword = 'informatica_rasp'
    command = 'python3 /home/pi/seguridad/save_page.py "%s"'
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command % name))

def recent_file(directorio):
    files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
    creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
    return files[creates_dates.index(max(creates_dates))]

def oldest_file(directorio):
    files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
    creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
    if len(creates_dates) == 0:
        return None
    return files[creates_dates.index(min(creates_dates))]

def resize_image(im):
    width, height = im.size
    left = width/4
    top = height/4
    right = 3*width/4
    bottom = 3*height/4
    cropped = im.crop((0,0,width,(height//4*3)))
    return cropped

def main():
    global current_time
    global text
    #global tts
    dir_items = 0
    directorio = "/home/pi/images/"
    image1 = Image.open("/home/pi/seguridad/original.jpg")
    #image1 = resize_image(im1)
    print("comenzando")
    while True:
        files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
        if len(files) != dir_items:
            try:
                #print("in while")
                image2 = Image.open(str(directorio+recent_file(directorio)))
                #image2 = resize_image(im2)
                dir_items = len(files)
                try:
                    if compare(image1,image2) > 400:
                        if (datetime.now() - current_time).seconds >= 4:
                            #with open("/home/pi/seguridad/speak.txt","r") as file:
                                #tts.say(file.read())
                            #tts.say(text)
                            print("hay gente")
                            current_time = datetime.now()
                            save_page(image2.filename)
                except Exception as er:
                    print(er)
		    #image1 = Image.open("/home/pi/seguridad/original.jpg")
                    #image1 = resize_image(im1)
            except IOError as er:
                print(er)
            #sleep(0.5)
                    

if __name__ == '__main__':
    text = "hola caraculo"
    #tts = talkey.Talkey(espeak = {'languages': {'es': {'voice': 'spanish-mb-es1','words_per_minute': 130},}})
    current_time = datetime.now()
    main()
