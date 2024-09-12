# environment and libraries
import os
import glob
import numpy as np
import random
import cv2
import matplotlib
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)
warnings.simplefilter(action = "ignore", category = UserWarning)

from mpl_toolkits.mplot3d import Axes3D


def convert_rgb_to_opponent(input_image):
    '''
    Converts an RGB image into the opponent color space and 
    returns the image with opponent color channels.

    Args:
        input_image: RGB image

    Returns:
        new_image: image with channels representing opponent color space
    '''

    # YOUR CODE HERE
    # convert input image to array format if not already
    if not isinstance(input_image, np.ndarray):
        input_image = np.array(input_image)

    # extract the color channels for further calculations
    R = input_image[:,:,0]
    G = input_image[:,:,1]
    B = input_image[:,:,2]

    # Compute O1,O2,O3
    O1 = (R-G) / np.sqrt(2)
    O2 = (R+G-2*B) / np.sqrt(6)
    O3 = (R+G+B) / np.sqrt(3)

     # Compute O1,O2,O3
    O1 = (R-G) / np.sqrt(2)
    O2 = (R+G-2*B) / np.sqrt(6)
    O3 = (R+G+B) / np.sqrt(3)

    # Normalize to [0,1] range
    
    # -255/sqrt(2) <= O1 <= 255/sqrt(2)
    maxO1 = 255/np.sqrt(2)
    minO1 = -255/np.sqrt(2)
    O1 = (O1 - minO1)/(maxO1 - minO1)
    
    # (-2*255)/sqrt(6) <= O2 <= (2*255)/sqrt(6)
    maxO2 = (2*255)/np.sqrt(6)
    minO2 = (-2*255)/np.sqrt(6)
    O2 = O2 = (O2 - minO2)/(maxO2 - minO2)

    # 0 <= O3 <= 3*255/sqrt(3)
    maxO3 = 3*255/np.sqrt(3)
    minO3 = 0
    O3 = O3 = (O3 - minO3)/(maxO3 - minO3)

    new_image = np.stack((O1, O2, O3), axis=-1)

    return new_image

if __name__ == '__main__':
    # generate opponent image using the function defined above
    #input_image = cv2.imread('images/sunflower.jpg')
    input_image = cv2.imread('images/beehive_house.jpg')
    # Convert the image into double precision for conversions
    input_image = input_image.astype(np.float32)

    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    opponent = convert_rgb_to_opponent(input_image)

    cv2.imshow('all',opponent)

    cv2.imshow('O1',opponent[:,:,0])

    cv2.imshow('O2',opponent[:,:,1])

    cv2.imshow('O3',opponent[:,:,2])
    cv2.waitKey(0)