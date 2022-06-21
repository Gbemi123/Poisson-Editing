
import cv2 
import numpy as np 
import matplotlib.pyplot as plt


# used to determine if pixel index is inside ROI 
def in_omega(index, mask):
    return mask[index] == 1

#3 Function to find the indices of the ROI of the mask
def ROI_points(mask):
    
    non0= np.nonzero(mask)
    list_points=list(zip(non0[0],non0[1]))

    return list_points

#function to get the 4 neighbours surrounding a pixel
def surrounding_pixels(index):
    i,j=index

    value=[(i+1,j), (i-1,j),(i,j+1),(i,j-1)]
    return value

def pixel_location(index, mask):
    if not np.any(in_omega(index,mask)):
        return False
    for pix in surrounding_pixels(index):
        if not np.any(in_omega(pix,mask)):
            return True

    return False