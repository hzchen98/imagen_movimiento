# -*- coding: utf-8 -*-
import os
import sys
from shutil import copyfile

def recent_file(directorio):
    files = [f for f in os.listdir(directorio) if ".jpg" in f and os.path.isfile(os.path.join(directorio,f))]
    creates_dates = [os.path.getctime(os.path.join(directorio,f)) for f in files]
    return files[creates_dates.index(max(creates_dates))]

def main():
    directorio = "/home/pi/images/"
    os.chdir("/var/www/html")
    html = """<!DOCTYPE html>
            <html>
            <head>
                    <meta charset="utf-8">
                    <title>Videovigilancia departamento de informática.</title>
            </head>
            <body>
                    <h3>El último movimiento</h3>
                    <img src="%s" alt="imagen"></img>
            </body>
            </html>
            """
    for file in os.listdir("."):
        if file == "index.html" in file: #or ".jpg" in file:
            os.remove(file)
    #copyfile(sys.argv[1], "/var/www/html/image.jpg")
    image = [file for file in os.listdir() if ".jpg" in file]
    try:
        with open("/var/www/html/index.html", "w") as file:
            file.write(html % image[0])
    except:
        pass

if __name__ == '__main__':
    main()

