%This is a script for Code A
%This script will run CreateTData.m to the image you've inputted, to create
%training data. Then it will run TOCNN.m to creat and train the CNN. Then
%it will ask you to enter a filepath of the image again to test it then it will output the
%denoised image.

%make sure to addpath the folder that contains the training images
addpath('TrainingDataCreated');

%prompt to ask the user for the filepath of the image to create training
%data
Input = input('Please enter the filepath of your image','s');

%%these are to create new training images using the image you will input 
%to denoise regular images then uncomment the line below
%TData = CreateTData(Input);
%to denoise registered images then uncomment the line below
TData = CreateTDataReg(Input);
%to denoise brackets images then uncomment the line below
%TData = CreateTDataBrackets(Input);
%to denoise Humanteeth images then uncomment the line below
%TData = CreateTDataHumanTeeth(Input);

%This trains the CNN with the newest training data 
%Make sure to change the folder name depending on which type of image was inputted
octDenoisingCNN = TOCNN('TrainingDataCreated');

% asks the user to input image for denoising 
prompt ='Please enter the name of your image, i.e "Image1.png"';
Image = input(prompt, 's'); 

%inputing the image prompted by the user for testing
Testimage = imread(Image);

%loading the newly trained CNN
load TCNN;
load Training; 

%denoises the image using the trained CNN
Testing = denoiseImage(Testimage,Training);
%displays the before and after images
imshowpair(Testing,Testimage,'montage');
%saves the after image in workspace
imwrite(Testing, 'DenoisingOutput.png','png');

%%ERROR CALCULATIONS 
%uncomment below to print the errors 
%    %CNN
%    CNNmse = immse(uint8(Testing), Testimage);
%    CNNpsnr = psnr(uint8(Testing), Testimage);
%    CNNssim = ssim(uint8(Testing), Testimage);
%    disp('CNN MSE');
%    disp(CNNmse);
%    disp('CNN PSNR');
%    disp(CNNpsnr);
%    disp('CNN SSIM');
%    disp(CNNssim); 