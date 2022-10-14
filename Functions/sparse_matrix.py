import cv2 
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
from cv2 import imshow
import scipy.sparse as SC
import scipy.sparse.linalg as linalg
from PixelLocation import surrounding_pixels


# Function to make cooefficient matrix(The sparse A matrix)

def sparse_matrix(Indices):

  m=len(Indices)

  A_Mat=SC.lil_matrix((m,m))
  for i, index in enumerate(Indices):
    A_Mat[i,i]=4

    for x in surrounding_pixels(index):
      if x not in Indices:
        continue
      j=Indices.index(x)
      A_Mat[i,j]=-1
    
  return A_Mat
