from PIL import Image
import math
import os
import sys


chars = ['@','#','0','X','W','M','O','Q','q','i','+','~','|','*','\'','.',' ']

def getGrayScalePixels(img):
    pixels = list(img.getdata())
    for i in range(len(pixels)):
        pixels[i] = 0.3*pixels[i][0]+0.59*pixels[i][1]+0.11*pixels[i][2]
    return pixels


def writeAsciiImage(imgPath, path):
    global chars
    img = Image.open(imgPath)
    img = img.resize((256,128), Image.ANTIALIAS)
    width, height = img.size

    print("out\\" + path)
    with open("out\\" + path, "a") as f:
        grayScaleList = getGrayScalePixels(img)
        for i in range(width*height):
            printChar = chars[mapCharToGrayValue(grayScaleList[i])]
            f.write(printChar)
            if(i % width == 0):
                f.write("\n")


def mapCharToGrayValue(val):
    global chars
    return math.ceil((val % 255) * len(chars) / 255) - 1


def main():
    if os.path.exists('out\\asciiImg.txt'):
        os.remove('out\\asciiImg.txt')
    writeAsciiImage(sys.argv[1], "asciiImg.txt")


if __name__ == '__main__':
    main()
