%This is a script for Code A Masking
%make sure to addpath the folder that contains the training images
addpath('MaskingTD');

%add the images that have been produced by edges and the pervious CNN
%to train the next CNN
octMaskingCNN = MOCNN('MaskingTD');

% asks the user to input image for denoising 
prompt ='Please enter the name of your image, i.e "Image1.pn"';
Image = input(prompt, 's'); 

% inputing and changing the image into gray scale
Testimage = imread(Image);

%loading the perviously trained CNN
load MCNN;
load MTraining; 

%denoises the image using the trained CNN 
Testing = denoiseImage(Testimage,MTraining);
%displays the before and after images
imshowpair(Testing,Testimage,'montage');
%saves the after image in workspace
imwrite(Testing, 'MaskingOutput.png','png');

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
