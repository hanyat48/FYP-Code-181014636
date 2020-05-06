from django.shortcuts import render
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#Importing the needed libraries 
import numpy as np
import pandas as pd
import cv2 as cv 
import os
from matplotlib import pyplot
import matlab.engine
import matplotlib.pyplot as plt
import skimage
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label
from skimage import feature,io
from PIL import Image, ImageDraw, ImageFont


def Home(request):
    return render(request, 'ImageProcessing/Home.html', {})

def twoRegistration(request):
    if request.method == 'POST' and request.FILES.get('MovingImage') and request.FILES.get('FixedImage') and request.POST.get('RegisteredImage'):
        #moving image
        Mmyfile = request.FILES.get('MovingImage')
        Mfs = FileSystemStorage()
        Mfilename = Mfs.save(Mmyfile.name, Mmyfile)
        Moving_file_url = Mfs.url(Mfilename)
        MI =os.path.join(settings.MEDIA_ROOT,Mfilename)
        #fixed image
        Fmyfile = request.FILES.get('FixedImage')
        Ffs = FileSystemStorage()
        Ffilename = Ffs.save(Fmyfile.name, Fmyfile)
        Fixed_file_url = Ffs.url(Ffilename)
        FI =os.path.join(settings.MEDIA_ROOT,Ffilename)
        #Registered Name
        RName = request.POST.get('RegisteredImage')
        RI = os.path.join(settings.MEDIA_ROOT,RName)
        #Starts the matlab engine
        eng = matlab.engine.start_matlab()
        #running the correct function
        Image = eng.ImageReg(MI,FI)
        pyplot.imsave(RI,Image)
        return render(request, 'ImageProcessing/twoRegistration.html', {
            'Moving_file_url': Moving_file_url, 'Fixed_file_url': Fixed_file_url,
            'Registered_file_url':RI, 'Image': Image})
        
    return render(request, 'ImageProcessing/twoRegistration.html')

def Reconstruction(request):
    if request.method =='POST' and request.POST.get('Filepath') and request.POST.get('Number'):
        Images = request.POST.get('Filepath')
        Number = request.POST.get('Number')
        Volume = eng.ImageReconstruction(Images,Number)
        return render(request, 'ImageProcessing/Reconstruction.html', {})
    
    return render(request, 'ImageProcessing/Reconstruction.html', {})

def Denoising(request):
    if request.method =='POST' and request.POST.get('Filepath') and request.POST.get('Name'):
        DImage = request.POST.get('Filepath')
        #Name
        Name = request.POST.get('Name')
        I = os.path.join(settings.MEDIA_ROOT,Name)
        #Starts the matlab engine
        eng = matlab.engine.start_matlab()
        #creating the training data
        Image1 = eng.CreateTData(DImage)
        #start the CNN
        Denoised = ImageDenoising(Image1)
        pyplot.imsave(I,Denoised)
        return render(request, 'ImageProcessing/Denoising.html', {
             'Denoised': Denoised, 'I': I})
    return render(request, 'ImageProcessing/Denoising.html', {})

def Masking(request):
    if request.method =='POST' and request.POST.get('Filepath') and request.POST.get('Name'):
        MImage = request.POST.get('Filepath')
        #Name
        Name = request.POST.get('Name')
        I = os.path.join(settings.MEDIA_ROOT,Name)
        #Starts the matlab engine
        eng = matlab.engine.start_matlab()
        #creating the training data
        Image2 = eng.CreateTData(MImage)
        #start the CNN
        Masked = ImageDenoising(Image2)
        pyplot.imsave(I,Masked)
        return render(request, 'ImageProcessing/Denoising.html', {
             'Masked': Masked, 'I': I})
    return render(request, 'ImageProcessing/Masking.html', {})

def Length(request):
    if request.method == 'POST' and request.POST.get('FP'):
        #filepath
        FP= request.POST.get('FP')
        ##Length code
        #Load the image
        image = skimage.io.imread(FP,as_gray =True)

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
        lbi = os.path.join(settings.MEDIA_ROOT,'Label_image.png')
        pyplot.imsave(lbi, label_image)
        #cv.imwrite('Label_image.png',label_image)

        #text
        text_image = Image.open(lbi)
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
        
        LFp = os.path.join(settings.MEDIA_ROOT,'Length.png')
        pyplot.imsave(LFp, text_image)
        return render(request, 'ImageProcessing/Length.html', {
             'text_image': text_image})
    return render(request, 'ImageProcessing/Length.html', {})

def SuggestedDecay(request):
    if request.method == 'POST' and request.POST.get('Filepath') and request.POST.get('Name'):
        #filepath
        FP = request.POST.get('Filepath')
        #Name
        Name = request.POST.get('Name')
        I = os.path.join(settings.MEDIA_ROOT,Name)
        #Name1
        Name1 = request.POST.get('Name1')
        I1 = os.path.join(settings.MEDIA_ROOT,Name1)
        #SUGGESTEDDECAY CODE
        #XMT images pre processing
        Im = cv.imread(FP)
        for x in range(0, len(Im)-1): 
            for y in range(0, len(Im[x])-1):
              if (sum(Im[x][y]) < 336 and sum(Im[x][y]) > 315):
                Im[x][y] = [255,0,0]
              else:
                Im[x][y] = Im[x][y]
        pyplot.imsave(I,Im)
        #XMT Green
        Im1 = cv.imread(I)
        boxsize = 15
        for x in range(len(Im1)-51):
            for y in range(len(Im1)-51):
              redpixels = 0
              for i in range(boxsize):
                for j in range(boxsize):
                  if np.array_equal(Im1[x+i][y+j], [255,0,0]):
                    redpixels+=1
            if redpixels/(boxsize*boxsize) > 0.5:
                for b in range(boxsize):
                  for c in range(boxsize):
                    Im1[x+b][y+c] = [0, 255, 0]

        pyplot.imsave(I1, Im1)
        return render(request, 'ImageProcessing/SuggestedDecay.html', {
            'Im': Im, 'Im1': Im1,
            'I':I, 'I1': I1})
    return render(request, 'ImageProcessing/SuggestedDecay.html', {})

