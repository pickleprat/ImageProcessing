import skimage
import numpy as np 
from matplotlib import pyplot as plt 
import os 
import cv2
import requests 
from bs4 import BeautifulSoup 
import io 
from zipfile import ZipFile 
import shutil 

# I AM SO COOOL 

if __name__ == '__main__':

    URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00360/'
    webpage = requests.get(URL).content
    page = BeautifulSoup(webpage, 'lxml')
    zip_name = page.find_all('a')[1]['href'] 
    zipfile = io.BytesIO(requests.get(f'{URL}/{zip_name}').content) 
    
    try: 
        os.mkdir('DATASET')
    except Exception as e: 
        shutil.rmtree('DATASET')
        os.mkdir('DATASET')

    with ZipFile(zipfile) as f: 
        f.extractall('./DATASET')

    print(os.listdir('DATASET'))

    
    

    

