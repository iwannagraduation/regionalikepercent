import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

'''
    first of all, I need read in two same size images.
    then, sub them and get the diff.
    till now, I need judge their similarity and decide which of them are alike and which are different.
    finally, gainning a value to evaluate their similarity.
'''


def readImg(path: str) -> Image:
    image = Image.open(path)
    return image

def imgDifference(image1: Image, image2: Image) -> Image:
    image1 = np.array(image1)
    image2 = np.array(image2)

    diff = image1 - image2
    diff = Image.fromarray(diff)
    return diff

def drawImg(image: Image) -> int:
    try:
        print(image.size)
        plt.imshow(image)
        plt.show()
        return 1
    except Exception as e:
        print(e)
        return -1

def imageToCsv(image: Image, file):
    data = pd.DataFrame(np.array(image))#(np.array(image)[0] +  np.array(image)[1] +  np.array(image)[3]) / 3
    data.to_csv(file)

if __name__ == "__main__":
    image1 = readImg("./data/image1.jpg")
    image2 = readImg("./data/image2.jpg")

    imgdiff = imgDifference(image1, image2)
    imageToCsv(imgdiff, "./data/test.csv")
    drawImg(imgdiff)