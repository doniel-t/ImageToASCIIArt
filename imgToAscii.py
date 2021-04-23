from PIL import Image
import math
import os
import sys


chars = [' ','@','#','0','X','Q','i','+','~','|','*','\'','.', ' ']

def getGrayScalePixels(img):
    pixels = list(img.getdata())
    for i in range(len(pixels)):
        pixels[i] = 0.3*pixels[i][0]+0.59*pixels[i][1]+0.11*pixels[i][2]
    return pixels

#scales Image down; keeps ascpect ratio; higher maxWidth means higher "resolution"
def scaleImage(img, maxWidth):
    width, height = img.size
    ratio = float(width)/height
    newHeight = math.floor(maxWidth / ratio) 
    scaledImage = img.resize((maxWidth, newHeight), Image.ANTIALIAS)
    return scaledImage


def writeAsciiImage(imgPath, path):
    global chars
    img = Image.open(imgPath)
    img = scaleImage(img,int(sys.argv[2]))
    width, height = img.size
    print(img.size)

    print("out\\" + path)
    with open("out\\" + path, "a") as f:
        grayScaleList = getGrayScalePixels(img)
        for i in range(width*height):
            printChar = chars[mapCharToGrayValue(grayScaleList[i])]
            if(grayScaleList[i] < 20):
                f.write('@')
            else:
                f.write(printChar)
            if(i % width == 0):
                f.write("\n")


def mapCharToGrayValue(val):
    global chars
    return math.ceil((val % 256) * len(chars) / 255) - 1


def main():
    if os.path.exists('out\\asciiImg.txt'):
        os.remove('out\\asciiImg.txt')
    writeAsciiImage(sys.argv[1], "asciiImg.txt")


if __name__ == '__main__':
    main()
