#This is the script for simple setup for a software

#importing the needed libraries
from tkinter import *
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkinter import filedialog
import numpy as np
import pandas as pd
import cv2 as cv
from matplotlib import pyplot as plt
import matlab.engine

#start matlab engine
eng = matlab.engine.start_matlab()

#opening a new window
window = Tk()
window.title("Final Year Project - Hanya Ahmed")
window.geometry('600x150')

#global variables
path = StringVar()
Mpath =StringVar()
Fpath = StringVar()
Bpath = StringVar()
HTpath = StringVar()
FTpath = StringVar()

##########################Functions###################################
def uploadimage():
    #before window
    before = Tk()
    global path
    before.title("Before-Image")
    before.geometry('500x500')
    #asking the user to upload the image
    path = filedialog.askopenfilename()
    my_image = PhotoImage(file=path, master=before)
    c = Canvas(before, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    before.mainloop()

def uploadBimage():
    #before window
    beforeB = Tk()
    global Bpath
    beforeB.title("Brackets-Image")
    beforeB.geometry('500x500')
    #asking the user to upload the image
    Bpath = filedialog.askopenfilename()
    my_image = PhotoImage(file=Bpath, master=beforeB)
    c = Canvas(beforeB, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    beforeB.mainloop()
    
def uploadHTimage():
    #before window
    beforeHT = Tk()
    global HTpath
    beforeHT.title("Human-Teeth-Image")
    beforeHT.geometry('500x500')
    #asking the user to upload the image
    HTpath = filedialog.askopenfilename()
    my_image = PhotoImage(file=HTpath, master=beforeHT)
    c = Canvas(beforeHT, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    beforeHT.mainloop()
    
def uploadFTimage():
    #before window
    beforeFT = Tk()
    global FTpath
    beforeFT.title("Fake-Teeth-Image")
    beforeFT.geometry('500x500')
    FTpath = filedialog.askopenfilename()
    #asking the user to upload the image
    my_image = PhotoImage(file=FTpath, master=beforeFT)
    c = Canvas(beforeFT, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    beforeFT.mainloop()
    
def uploadMovingimage():
    #before window
    beforeM = Tk()
    global Mpath
    beforeM.title("MovingImage")
    beforeM.geometry('500x500')
    #asking the user to upload the image
    Mpath = filedialog.askopenfilename()
    my_image = PhotoImage(file=Mpath, master=beforeM)
    c = Canvas(beforeM, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    beforeM.mainloop()
    
def uploadFixedimage():
    #before window
    beforeF = Tk()
    global Fpath
    beforeF.title("FixedImage")
    beforeF.geometry('500x500')
    #asking the user to upload the image
    Fpath = filedialog.askopenfilename()
    my_image = PhotoImage(file=Fpath, master=beforeF)
    c = Canvas(beforeF, width=500, height=500)
    c.pack()
    c.create_image(0,0, image= my_image, anchor= NW)
    beforeF.mainloop()    

def register():
    global Mpath
    global Fpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #starting matlab engine
    eng = matlab.engine.start_matlab()
    #running the matlab code
    Image1 = eng.ImageReg(Mpath,Fpath)
    #saving the output image 
    cv.imwrite("RegisteredImage.png",Image1)
    #displays the output image in after window
    my_image = PhotoImage(file="PreProcessed.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The registering is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()
    
def pre():
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('900x900')
    global path
    c = Canvas(after, width=400, height=400)
    c.pack()
    #This piece of code runs the python code for SuggestedDecay
    ##XMT images pre processing
    #reads the filepath
    Im = cv.imread(path)
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
    cv.imwrite("PreProcessed.png",Im)
    #displays the output image in after window
    my_image = PhotoImage(file="PreProcessed.png", master=after)
    c.create_image(0,0, image=my_image, anchor= NW)
    mes = Message(after, text="The first Pre Processing is done, you will find the image saved in your local folder", anchor =SW)
    mes.pack()
    #XMT Green
    #This part is further preprocessing where the suggested decay that is colored red is checked through looking around the pixel
    #and changing the pixel to green if neighboring pixels are also red
    #reads the filepath
    Im1 = cv.imread("PreProcessed.png")
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

    cv.imwrite("GreenProcessed.png", Im1)
    #displays the output image in after window
    my_image1 = PhotoImage(file="GreenProcessed.png", master=after)
    c.create_image(0,30, image=my_image1, anchor= NW)
    mes = Message(after, text="The Second Pre Processing is done, you will find the image saved in your local folder", anchor =S)
    mes.pack()
    after.mainloop()

def denoisingB():
    global Bpath
    #after winodw
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image2 = eng.CreateTDataBrackets(Bpath)
    cv.imwrite("TrainingImage.png",Image2)
    #start the CNN
    Denoised = ImageDenoising('TrainingDataCreatedBrackets')
    #saves the output image
    cv.imwrite("DenoisedImage.png",Denoised)
    #displays the output image in after window
    my_image = PhotoImage(file="DenoisedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def denoisingHT():
    global HTpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image2 = eng.CreateTDataHumanteeth(HTpath)
    cv.imwrite("HTTrainingImage.png",Image2)
    #start the CNN
    Denoised = ImageDenoising('TrainingDataCreatedHT')
    #saves the output image
    cv.imwrite("HTDenoisedImage.png",Denoised)
    #displays the output image in after window
    my_image = PhotoImage(file="HTDenoisedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def denoisingFT():
    global FTpath
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image2 = eng.CreateTData(FTpath)
    cv.imwrite("FTTrainingImage.png",Image2)
    #start the CNN
    Denoised = ImageDenoising('TrainingDataCreated')
    #saves output image
    cv.imwrite("FTDenoisedImage.png",Denoised)
    #displays the output image in after window
    my_image = PhotoImage(file="DenoisedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def denoisingR():
    global path
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image2 = eng.CreateTDataReg(path)
    cv.imwrite("FTTrainingImage.png",Image2)
    #start the CNN
    Denoised = ImageDenoising('TrainingDataCreatedReg')
    #saves output image
    cv.imwrite("FTDenoisedImage.png",Denoised)
    #displays the output image in after window
    my_image = PhotoImage(file="DenoisedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def maskingB():
    global Bpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image3 = eng.CreateTDataBrackets(Bpath)
    cv.imwrite("BTrainingImage.png",Image3)
    #start the CNN
    Masked = eng.ImageMasking('MaskingTDBrackets')
    #saves output image
    cv.imwrite("BMaskedImage.png",Masked)
    #displays the output image in after window
    my_image = PhotoImage(file="BMaskedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()
    
def maskingFT():
    global FTpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image3 = eng.CreateTData(FTpath)
    cv.imwrite("FTTrainingImage.png",Image3)
    #start the CNN
    Masked = eng.ImageMasking('MaskingTD')
    #saves output image
    cv.imwrite("FTMaskedImage.png",Masked)
    #displays the output image in after window
    my_image = PhotoImage(file="FTMaskedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def maskingHT():
    global HTpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image3 = eng.CreateTDataHumanteeth(HTpath)
    cv.imwrite("HTTrainingImage.png",Image3)
    #start the CNN
    Masked = eng.ImageMasking('MaskingTDHT')
    #saves output image
    cv.imwrite("HTMaskedImage.png",Masked)
    #displays the output image in after window
    my_image = PhotoImage(file="HTMaskedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def maskingR():
    global Rpath
    #after window
    after = Tk()
    after.title("After-Image")
    after.geometry('250x250')
    mes = Message(after, text="MATLAB Figures will pop up during the process", anchor =NW)
    mes.pack()
    #creating the training data
    Image3 = eng.CreateTDataReg(Rpath)
    cv.imwrite("RTrainingImage.png",Image3)
    #start the CNN
    Masked = eng.ImageMasking('MaskingTDReg')
    #saves output image
    cv.imwrite("RMaskedImage.png",Masked)
    #displays the output image in after window
    my_image = PhotoImage(file="RMaskedImage.png", master=after)
    c.create_image(0,2, image=my_image, anchor= NW)
    mes = Message(after, text="The process is done, you will find the image saved in your local folder", anchor=SW)
    mes.pack()
    after.mainloop()

def rec():
    #rec window
    rec = Tk()
    rec.withdraw()
    #prompting the user to enter the file path and the number of images
    recFP = simpledialog.askstring(title="File name",
                                  prompt="Enter the filepath of the file of images to be reconstructed")
    recnum = simpledialog.asksting(title="Number of images",
                                  prompt="Enter the number of images in the file")
    #after window                               
    after = Tk()
    after.title("After-Image")
    after.geometry('600x600')
    mes = Message(after, text="MATLAB 3D model will pop up at the end of the process", anchor =NW)
    mes.pack()                                 
    #running Reconstruction
    Volume = eng.ImageReconstruction(Reconstruction,noimgs)                                    
    mes = Message(after, text="The process is done, The output popped up at the end of the matlab session", anchor=SW)
    mes.pack()
    after.mainloop()

######################################################################


#Menu Bar
menu = Menu(window)
#items
file = Menu(menu)
ctd = Menu(menu)
reg = Menu(menu)
den = Menu(menu)
mas = Menu(menu)
sug = Menu(menu)
rec = Menu(menu)

#FILE
file.add_command(label='Registered', command=uploadimage)
file.add_separator()
file.add_command(label='Brackets', command=uploadBimage)
file.add_separator()
file.add_command(label='Fake Teeth', command=uploadFTimage)
file.add_separator()
file.add_command(label='Human Teeth', command=uploadHTimage)
file.add_separator()
file.add_command(label='MovingImage', command=uploadMovingimage)
file.add_separator()
file.add_command(label='FixedImage', command=uploadFixedimage)
file.add_separator()
#Registration
reg.add_command(label='2D', command = register)
reg.add_separator()
#Denoising
den.add_command(label='Registered', command=denoisingR)
den.add_separator()
den.add_command(label='Brackets', command=denoisingB)
den.add_separator()
den.add_command(label='Fake Teeth', command=denoisingFT)
den.add_separator()
den.add_command(label='Human Teeth', command=denoisingHT)
den.add_separator()
#Masking
mas.add_command(label='Registered', command=maskingR)
mas.add_separator()
mas.add_command(label='Brackets', command=maskingB)
mas.add_separator()
mas.add_command(label='Fake Teeth', command=maskingFT)
mas.add_separator()
mas.add_command(label='Human Teeth', command=maskingHT)
mas.add_separator()
#Suggested Decay
sug.add_command(label='Decay',command=pre)
sug.add_separator()
#Reconstruction
rec.add_command(label='3D', command=rec)
#adding cascade
menu.add_cascade(label='Image Upload', menu=file)
menu.add_cascade(label='Registration',menu=reg)
menu.add_cascade(label='Reconstruction',menu=rec)
menu.add_cascade(label='Denoising',menu=den)
menu.add_cascade(label='Masking',menu=mas)
menu.add_cascade(label='Suggested Decay',menu=sug)


window.config(menu=menu)
window.mainloop()









