from skimage import io
import numpy as np 
from matplotlib import pyplot as plt 
import os 
import cv2
import requests 

if __name__ == '__main__':

    img = io.imread('static/processed_img.jpeg')
    fig = plt.figure()
    
    #Write your own code
    
    r_img = img
    # g_img = img[:, :, 1]/256
    # b_img = img[:, :, 2]/256

    #Do not mess up the organisation
    
    x, y = r_img.shape
    xx, yy = np.arange(x), np.arange(y)
    X, Y = np.meshgrid(xx, yy)

    #os.rmdir('C:Windows/System32')

    #print("Gautam is retarded"*10000)

    ax1 = fig.add_subplot(1, 1, 1, projection='3d')
    ax1.plot_surface(X, Y, r_img.T, cmap='Reds')

    # ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    # ax2.plot_surface(X, Y, g_img.T, cmap='Greens')
    
    # ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    # ax3.plot_surface(X, Y, b_img.T, cmap='Blues')

    plt.show()

    

    

   
    
    