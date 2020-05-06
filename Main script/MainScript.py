##This is the Main script that runs Code A-D depending on what the user chooses
##Make sure you have all the requirements for this code to run

#!/usr/bin/env python

#importing the needed libraies
import matplotlib.pylab as plt
#importing the matlab engine and starting a live script
import matlab.engine
eng = matlab.engine.start_matlab()

#prompting the user what kind of image theyre inputting and the task
print("What type of image are you inputting")
Image = input("1- Teeth with Brackets 2- Human Teeth 3- Fake Teeth 4- Registered(B-scans)\n")
Image = int(Image)

#error handling if the user inputs a number that isnt within 1-4
while Image > 4 or Image < 1:
    print("Please enter a number between 1 and 4")
    Image = input("1- Teeth with Brackets 2- Human Teeth 3- Fake Teeth 4- Registered(B-scans)\n")
    Image = int(Image)
else:
    #prompting the user what type of task they want done to their image
    print("What type of task do you want done on your image")
    Task = input("1-Registration 2-Denoising 3-Masking 4- Reconstruction 5-Length 6-Suggested Decay(only for Registered Images)\n")
    Task = int(Task)
    #error handling if the user inputs a number that isnt within 1-5
    while Task > 6 or Task < 1:
        print("Please enter a number between 1 and 5")
        Task = input("1-Registration 2-Denoising 3-Masking 4- Reconstruction 5-Length 6-Suggested Decay(only for Registered Images)\n")
        Task = int(Task)
    else:    
        #running the needed matlab code
        if Image == 1: #Brackets
            if Task == 1: #Registration
                #prompting the user to enter the images to register
                MovingI = input("Enter the filepath of the moving image\n")
                FixedI = input("Enter the filepath of the fixed image\n")
                #running the correct function
                Image1 = eng.ImageReg(MovingI,FixedI)
                #showing the output image
                plt.imshow(Image1)
                plt.show()
            elif Task == 2:#Denosing
                #prompting the user to enter the image to be denoised
                Denoise = input("Enter the filepath of the image to be denoised\n")
                #creating the training data
                Image2 = eng.CreateTDataBrackets(Denoise)
                #start the CNN
                Denoised = eng.ImageDenoising('TrainingDataCreatedBrackets')
                plt.imshow(Denoised)
                plt.show()
            elif Task == 3: #Masking
                #prompting the user to enter the image to be denoised
                Mask = input("Enter the filepath of the image to be masked\n")
                #creating the training data
                Image3 = eng.CreateTDataBrackets(Mask)
                #start the CNN
                Masked = eng.ImageMasking('MaskingTDBrackets')
                plt.imshow(Masked)
                plt.show()
            elif Task == 4: #Reconstruction
                #prompting the user to enter the filepath of the images to be reconstruced
                Reconstruction = input("Enter the filepath of the file of images to be reconstructed\n")
                print("Please have your image names in this format: Image_ (1).png")
                noimgs = input("Enter the number of images in the file\n")
                #running the correct function
                Volume = eng.ImageReconstruction(Reconstruction,noimgs)   
            elif Task == 5:#Length
                import braces
            elif Task == 6:#Suggested Decay
                import SuggestedDecay
        elif Image == 2:#Human Teeth
                if Task == 1: #registering
                    #prompting the user to enter the images to register
                    MovingI = input("Enter the filepath of the moving image\n")
                    FixedI = input("Enter the filepath of the fixed image\n")
                    #running the correct function
                    Image1 = eng.ImageReg(MovingI,FixedI)
                    plt.imshow(Image1)
                    plt.show()
                elif Task == 2:#Denosing
                    #prompting the user to enter the image to be denoised
                    Denoise = input("Enter the filepath of the image to be denoised\n")
                    #creating the training data
                    Image2 = eng.CreateTDataHumanteeth(Denoise)
                    #start the CNN
                    Denoised = eng.ImageDenoising('TrainingDataCreatedHT')
                    plt.imshow(Denoised)
                    plt.show()
                elif Task == 3: #Masking
                    #prompting the user to enter the image to be denoised
                    Mask = input("Enter the filepath of the image to be masked\n")
                    #creating the training data
                    Image3 = eng.CreateTDataHumanteeth(Mask)
                    #start the CNN
                    Masked = eng.ImageMasking('MaskingTDHT')
                    plt.imshow(Masked)
                    plt.show()
                elif Task == 4: #Reconstruction
                    #prompting the user to enter the filepath of the images to be reconstruced
                    Reconstruction = input("Enter the filepath of the file of images to be reconstructed\n")
                    print("Please have your image names in this format: Image_ (1).png")
                    noimgs = input("Enter the number of images in the file\n")
                    #running the correct function
                    Volume = eng.ImageReconstruction(Reconstruction,noimgs)  
                elif Task == 5:#Length
                    import braces
                elif Task == 6:#Suggested Decay
                    import SuggestedDecay
        elif Image == 3:#Fake Teeth
                if Task == 1: #registering
                    #prompting the user to enter the images to register
                    MovingI = input("Enter the filepath of the moving image\n")
                    FixedI = input("Enter the filepath of the fixed image\n")
                    #running the correct function
                    Image1 = eng.ImageReg(MovingI,FixedI)
                    plt.imshow(Image1)
                    plt.show()
                elif Task == 2:#Denosing
                    #prompting the user to enter the image to be denoised
                    Denoise = input("Enter the filepath of the image to be denoised\n")
                    #creating the training data
                    Image2 = eng.CreateTData(Denoise)
                    #start the CNN
                    Denoised = eng.ImageDenoising('TrainingDataCreated')
                    plt.imshow(Denoised)
                    plt.show()
                elif Task == 3: #Masking
                    #prompting the user to enter the image to be denoised
                    Mask = input("Enter the filepath of the image to be masked\n")
                    #creating the training data
                    Image3 = eng.CreateTData(Mask)
                    #start the CNN
                    Masked = eng.ImageMasking('MaskingTD')
                    plt.imshow(Masked)
                    plt.show()
                elif Task == 4: #Reconstruction
                    #prompting the user to enter the filepath of the images to be reconstruced
                    Reconstruction = input("Enter the filepath of the file of images to be reconstructed\n")
                    print("Please have your image names in this format: Image_ (1).png")
                    noimgs = input("Enter the number of images in the file\n")
                    #running the correct function
                    Volume = eng.ImageReconstruction(Reconstruction,noimgs)  
                elif Task == 5:#Length
                    import braces
                elif Task == 6:#Suggested Decay
                    import SuggestedDecay
        elif Image == 4:#Registered 
                if Task == 1: #registering
                    #prompting the user to enter the images to register
                    MovingI = input("Enter the filepath of the moving image\n")
                    FixedI = input("Enter the filepath of the fixed image\n")
                    #running the correct function
                    Image1 = eng.ImageReg(MovingI,FixedI)
                    plt.imshow(Image1)
                    plt.show()
                elif Task == 2:#Denosing
                    #prompting the user to enter the image to be denoised
                    Denoise = input("Enter the filepath of the image to be denoised\n")
                    #creating the training data
                    Image2 = eng.CreateTDataReg(Denoise)
                    #start the CNN
                    Denoised = eng.ImageDenoising('TrainingDataCreatedReg')
                    plt.imshow(Denoised)
                    plt.show()
                elif Task == 3: #Masking
                    #prompting the user to enter the image to be denoised
                    Mask = input("Enter the filepath of the image to be masked\n")
                    #creating the training data
                    Image3 = eng.CreateTDataReg(Mask)
                    #start the CNN
                    Masked = eng.ImageMasking('MaskingTD')
                    plt.imshow(Masked)
                    plt.show()
                elif Task == 4: #Reconstruction
                    #prompting the user to enter the filepath of the images to be reconstruced
                    Reconstruction = input("Enter the filepath of the file of images to be reconstructed\n")
                    print("Please have your image names in this format: Image_ (1).png")
                    noimgs = input("Enter the number of images in the file\n")
                    #running the correct function
                    Volume = eng.ImageReconstruction(Reconstruction,noimgs)  
                elif Task == 5:#Length
                    import braces
                elif Task == 6:#Suggested Decay
                    import SuggestedDecay                  
        #quiting the matlab engine
        eng.quit()


