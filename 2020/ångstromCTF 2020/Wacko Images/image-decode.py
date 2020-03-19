
from numpy import *
from PIL import Image

flag = Image.open(r"flag.png")
img = array(flag)

key = [41, 37, 23]

a, b, c = img.shape
for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            xx = 10500
            while True:
                if xx % 251 == pixel[i]:
                    if (xx / key[i]).is_integer():
                        pixel[i] = xx / key[i]
                        break
                xx -= 1
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('enc.png')

