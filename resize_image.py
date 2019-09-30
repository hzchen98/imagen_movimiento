from PIL import Image

def resize_image(im):
    original = Image.open(im)
    width, height = original.size
    left = width/4
    top = height/4
    right = 3*width/4
    bottom = 3*height/4
    cropped = original.crop((0,0,width,(height//4*3)))
    cropped.save("2"+im)



resize_image("language_ch.png")
