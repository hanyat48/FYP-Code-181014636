#!/usr/bin/env python
#This is the script that measures the length of the borders in the images

#importing the needed libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label
from skimage import feature,io
from PIL import Image, ImageDraw, ImageFont

#prompts the user to enter the filepath of the image
filepath = input("Please enter the image filepath")

#Load the image
image = skimage.io.imread(filepath,as_gray =True)

#creating 3 subplots
fig, axes = plt.subplots(4,
                         figsize=(20, 20))
ax0, ax1, ax2,ax3 = axes.flat
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Original', fontsize=24)
ax0.axis('off')

#Detect edges using the canny effect
edges = feature.canny(image, sigma=3,
                     low_threshold=10,
                     high_threshold=60)

ax1.imshow(edges, cmap=plt.cm.gray)
ax1.set_title('Edges', fontsize=24)
ax1.axis('off')

#label the edges
label_image = label(edges)
ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_title('Labeled items', fontsize=24)
ax2.axis('off')

#saving the image
cv.imwrite('Label_image.png',label_image)

#text
text_image = Image.open('Label_image.png')
#font = ImageFont.truetype('Roboto-Bold.ttf', size=15)
draw = ImageDraw.Draw(text_image)

#drawing the red squares
for region in regionprops(label_image):
    # Draw rectangle around segmented coins.
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr),
                              maxc - minc,
                              maxr - minr,
                              fill=False,
                              edgecolor='red',
                              linewidth=2)
    ax2.add_patch(rect)
    length = maxr-minr
    width = maxc-minc
    print(width,length)
    draw.text((minc, minr),"{}".format(length),fill=(255))

ax3.imshow(text_image, cmap=plt.cm.gray)
ax3.set_title('Lengths', fontsize=24)
ax3.axis('off')

plt.tight_layout()
plt.show()
