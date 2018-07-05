from PIL import Image, ImageOps
import sys
import os

image = Image.open("nature.jpg")

if len(sys.argv) != 3:
    print("This function needs at least two arguments!! \n<name of the function> <path to image> <image treshold>")

else:
    image = Image.open(sys.argv[1])
    f = open("picture.txt", "w")

spinImage = ImageOps.mirror(image)
spinImage = spinImage.rotate(90)
width, height = image.size

width *= 10
height *= 10

def generate(brush_color1, brush1, brush_color2, brush2, brush_color3, brush3, tresh = 100):
    px = spinImage.load()

    presledek = ""
    for i in range(0, len(brush1)):
        presledek += " "

    for x in range(0, spinImage.size[0]):
        niz_slika = ""
        for y in range(0, spinImage.size[1]):

            # 1st channel ----------------------
            if px[x, y][0] < tresh:
                niz_slika += brush_color1

            elif px[x, y][0] == tresh:
                niz_slika += brush1

            else:
                niz_slika += presledek

            # 2nd channel ----------------------
            if px[x, y][1] < tresh:
                niz_slika += brush_color2

            elif px[x, y][1] == tresh:
                niz_slika += brush2

            else:
                niz_slika += presledek

            # 3rd channel ----------------------
            if px[x, y][2] < tresh:
                niz_slika += brush_color3

            elif px[x, y][2] == tresh:
                niz_slika += brush3

            else:
                niz_slika += presledek

        f.write(niz_slika + '\n')

if len(sys.argv) == 3:
    generate("#", "-", "0", "-", "%", "*", int(sys.argv[2]))
    f.close()
    print("Showing the converted image...")
    os.system("picture.txt")
    print("Converted image closed.")
