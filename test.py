from numpy.random import random

l = [1,2,3]
print l
print l + (2,)
print random(l + (2,))



import cv2
import numpy as np
import os


def getfiles(path):
        dirs = []
        for item in os.listdir(path):
                if item[-7:] == "ori.jpg":
                        dirs.append(item)
        return dirs


def make_contour_image(path):
    neiborhood24 = np.array([[1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1]],
                                np.uint8)

    gray = cv2.imread("image/image/" + path, cv2.IMREAD_GRAYSCALE)
    color = cv2.imread("image/image/" + path, cv2.IMREAD_COLOR )

    re = cv2.resize(gray,(128,128))
    color_re = cv2.resize(color,(128,128))


    cv2.imwrite("image/image_small/"+path, color_re)

    dilated = cv2.dilate(re, neiborhood24, iterations=1)

    diff = cv2.absdiff(dilated, re)

    contour = 255 - diff

    width, height = contour.shape

    for i in range(width):
        for j in range(height):
            if(contour[i][j] < 240):
                contour[i][j] = 0
            else:
                contour[i][j] = 255


    cv2.imwrite("image/image_small/"+path[:-7]+"edge.jpg", contour)

    return contour

path = 'image/image'

files = getfiles(path)


for file in files:
        print file
        make_contour_image(file)
