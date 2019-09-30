import os
from PIL import Image

def recent_file(directorio):
    files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
    creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
    return str(files[creates_dates.index(max(creates_dates))])

def command(directorio):
    sudoPassword = 'informatica_rasp'
    command = 'cp %s /home/pi/seguridad/original.jpg'
    image = directorio+recent_file(directorio)
    print(image)
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command % image))

def main():
    directorio = "/home/pi/images/"
    #file = Image.open(directorio+recent_file(directorio))
    #print(file.filename)
    #file.save("/home/pi/seguridad/original.jpg")
    command(directorio)

if __name__=='__main__':
    main()
