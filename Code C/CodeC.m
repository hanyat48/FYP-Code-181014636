%This script is Code C which is to construct the XMT and OCT registered images 

%make sure to addpaths to both folders containing the B-scans of XMT and OCT
addpath('Nok1_XMT_Reg');
addpath('OCTReg-denoised');

%XMT B-SCANS
%an unsigned int variable
numberXMT = uint8(0);
%for loop to generate all the images
%change the number depending on the number of images there are in the folder
for i=1: 419 
    numberXMT = i; 
    %read the image starting from the first one
    arrayXMT = imread(strcat('XMT_ (',sprintf('%d',numberXMT),').png'));
    %remove the background
    Z = imsubtract(arrayXMT,100);
    %insert the B-scan into a 3D array
    XMT3D(:,:,numberXMT) = Z; 
end

figure('Name', 'XMT 3D');
%shows the 3D image
Model = volshow(XMT3D); 

%OCT B-SCANS
%an unsigned int variable
numberOCT = uint8(0);
%for loop to generate all the images
%change the number depending on the number of images there are in the folder
for i=1: 419 
    numberOCT = i;  
    %read the image starting from the first one
    arrayOCT = imread(strcat('REOCT_ (',sprintf('%d',numberOCT),').png'));
    %remove the background
    Z1 = imsubtract(arrayOCT,20);
    %insert the B-scan into a 3D array
    OCT3D(:,:,numberOCT) = Z1; 
end

figure('Name', 'OCT 3D');
%show the 3D image
Model1 = volshow(OCT3D);

