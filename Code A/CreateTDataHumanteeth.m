%This script is CreateTData which creates training data from the image that
%has been prompted from CodeADenoising.m
function FSharp = CreateTDataHumanteeth(FilePath)
    
    %  This function is used to create the training data using:
    %  1- Thresholding
    %  2- Using Locallapfilt we smooth the edges 
    %  3- Using BM3DSHARP, to further debur and sharpen
    %  4- Using imsharpen at the max 
    %  This is all done so the image has distinct features, that the CNN can
    %  recognise.
    
    %Make sure you have downloaded BM3D into your folder you are working
    addpath('BM3D');
    
    %make sure to addpath the folder that contains the training images
    addpath('TrainingDataCreatedHT');
    
    %It reads the png image or file path
    I = imread(FilePath);
    %it calculates the number of dimensions in the array
    dimensionsImg = ndims(I);
    %if the no. of dimensions is larger than 2 then trun it into gray scale
    if dimensionsImg > 2
        I = rgb2gray(I);
    end
    
    %Jons code to Threshold
    thresh = 0.095;
    hw = size(I);
    mask(hw(1),hw(2)) = true;
    %Calculate weights of pixels based on grayscale intensity difference for
    %use with fast marching image segmentation
    W = graydiffweight(I,mask,'GrayDifferenceCutoff',25);
    %Segment image using fast marching method, produces a segmented image (BW) of D
    [BW,D] = imsegfmm(W,mask,thresh);
    %Convert image to single format
    BW =im2single(BW);
    %Segment again now using k means with 2 clusers, 1 for bg noise and 1 for
    %structural information
    [L,cen]= imsegkmeans(BW,2);
    %Create a mask for the 2 clusters
    mask1 = L==1;
    clus1 = I .* uint8(mask1);
    mask2 = L==2;
    clus2 = I .* uint8(mask2);
    %Separate larger cluster based on pixel information contained in each mask
    if sum((clus2)) > sum((clus1))
        large = clus1;
    else
        large = clus2;
    end
    %take smaller matrix as it usualy contains more information (more noise)
    large = clus2;
    largeEdit = imadjust(large,[0.3 0.7],[]);
    %Boost contrast for strutural information slightly
    imshowpair(large,largeEdit,'blend','Scaling','joint');
    h = getframe; contrast = h.cdata;
    %Fuse contrast boosted matrix with original matrix containing structural
    %information
    contrast = imfuse(clus2,largeEdit,'blend','Scaling','joint');
    h = getframe; contrast = h.cdata;
    %Shows image with background removed and original image
    imshow(contrast);
    imwrite(contrast,'TrainingDataCreatedHT/HTThresholdData.png');
    
  
    %uses Fast local laplacian filtering of images to smooth the edges
    L = locallapfilt (I, 0.3, 4.0);
    imwrite(L,'TrainingDataCreatedHT/HTTDtest10.png');
    %L1 = rgb2gray(L1);
    %uses BM3Dsharp to sharpen the image with 10 SNR noise
    Sharp = BM3DSHARP(L,50, 1.5, 'np', 1);
    imwrite(Sharp,'TrainingDataCreatedHT/HTTDtest11.png');
    %further sharpening is done using imsharpen at the max
    FSharp = imsharpen(Sharp,'Threshold',0.7,'Amount',2,'Radius',2);
    imwrite(FSharp,'TrainingDataCreatedHT/HTTDtest12.png');
    
    
    %% Masking Training Data 
    
    %make sure to addpath the folder that contains the training images
    addpath('MaskingTDHT');

    %finding the edges of the image for masking 
    %uses the log method
    BinaryLog = edge(FSharp,'log');
    %multiplies the binary array by 255 to change it to a rgb array
    BILog = (255*BinaryLog); 
    %saves the image
    imwrite(BILog,'MaskingTDHT/RegMtest10.png');
    %uses the Zerocross method
    BinaryZC = edge(FSharp,'zerocross');
    %multiplies the binary array by 255 to change it to a rgb array
    BIZC = (255*BinaryZC);
    %saves the image
    imwrite(BIZC,'MaskingTDHT/RegMtest11.png');
    %uses the Canny method
    BinaryCanny = edge(FSharp,'Canny');
    %multiplies the binary array by 255 to change it to a rgb array
    BICanny = (255*BinaryCanny);
    %saves the image
    imwrite(BICanny,'MaskingTDHT/RegMtest12.png');  


    
   %% Error calculations
   
   %in this section MSE PSNR SSIM are calculated for each stage of the
   %training data
   %Uncomment for the error to show
%    %FLLP
%    Fmse = immse(uint8(L), I);
%    Fpsnr = psnr(uint8(L), I);
%    Fssim = ssim(uint8(L), I);
%    disp('FLLP MSE');
%    disp(Fmse);
%    disp('FLLP PSNR');
%    disp(Fpsnr);
%    disp('FLLP SSIM');
%    disp(Fssim);     
%    %BM3DSharp
%    BSmse = immse(uint8(DBI), I);
%    BSpsnr = psnr(uint8(DBI), I);  
%    BSssim = ssim(uint8(DBI),I);
%    disp('BM3DSharpen MSE');
%    disp(BSmse);
%    disp('BM3DSharpen PSNR');
%    disp(BSpsnr);
%    disp('BM3DSharpen SSIM');
%    disp(BSssim);
%    %Imsharpen
%    Smse = immse(uint8(FSharp), I);
%    Spsnr = psnr(uint8(FSharp), I);
%    Sssim = ssim(uint8(FSharp), I);
%    disp('Imsharpen MSE');
%    disp(Smse);
%    disp('Imsharpen PSNR');
%    disp(Spsnr);
%    disp('Imsharpen SSIM');
%    disp(Sssim);
%    %Thresholding
%    Tmse = immse(uint8(contrast), I);
%    Tpsnr = psnr(uint8(contrast), I);
%    Tssim = ssim(uint8(contrast), I);
%    disp('Thresholding MSE');
%    disp(Tmse);
%    disp('Thresholding PSNR');
%    disp(Tpsnr);
%    disp('Thresholding SSIM');
%    disp(Tssim);
end 
