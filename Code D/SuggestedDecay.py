#This script is for Code D - Detecting Decay
#However there are faults in this code that does not achieve the objective

#importing the needed libraries
import numpy as np
import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt

#Prompt for the user to enter the filepath of B-scan image
FilePath = input("Please Enter the filepath of the BScan i.e Image.png")

##XMT images pre processing
#reads the filepath
Im = cv.imread(FilePath)
#nested for loops to run through the image array to check if the pixel number is between a certain color that corresponds to decay
#this is where the fault is, the pixel range is not the corrent color for decay
for x in range(0, len(Im)-1): 
  for y in range(0, len(Im[x])-1):
    if (sum(Im[x][y]) < 336 and sum(Im[x][y]) > 315):
      #if its within the range color it red
      Im[x][y] = [255,0,0]
    else:
      #else keep it as it is
      Im[x][y] = Im[x][y]
#saves the new image in the same folder
cv.imwrite("PreprocessingImage.png",Im)
#displays the image 
plt.imshow(Im)
plt.show()

#XMT Green
#This part is further preprocessing where the suggested decay that is colored red is checked through looking around the pixel
#and changing the pixel to green if neighboring pixels are also red

#reads the filepath
Im1 = cv.imread("PreprocessingImage.png")
#sets the box of neighboring pixels
boxsize = 15
#nested for loops to run through the image array 
for x in range(len(Im1)-51):
  for y in range(len(Im1)-51):
    redpixels = 0
    #nested for loops to run through the box around selected pixel 
    for i in range(boxsize):
      for j in range(boxsize):
        if np.array_equal(Im1[x+i][y+j], [255,0,0]):
          redpixels+=1
  if redpixels/(boxsize*boxsize) > 0.5:
    for b in range(boxsize):
      for c in range(boxsize):
        Im1[x+b][y+c] = [0, 255, 0]
#saves the new image in the same folder
cv.imwrite("GreenProcessedImage.png", Im1)
#displays the image 
plt.imshow(Im1)
plt.show()
