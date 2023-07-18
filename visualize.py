import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import cv2 as cv 

def display(img):
    x, y = np.arange(1600), np.arange(782)
    x, y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot_surface(x, y, img.T)
    plt.show()

def main():
    fari = cv.cvtColor(
        cv.imread(
            'static/processed_img.jpeg'
        ),
        cv.COLOR_BGR2GRAY
    )
    display(fari)

if __name__ == '__main__':
    main()