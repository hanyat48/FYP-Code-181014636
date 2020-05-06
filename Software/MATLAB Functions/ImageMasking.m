%Code A - masking put into a function for Main script
function Testing = ImageMasking(Filepath)
    
    %add the images that have been produced by edges and the pervious CNN
    %to train the next CNN
    octMaskingCNN = MOCNN(Filepath);
    
    % inputing and changing the image into gray scale
    Testimage = imread(Filepath);
    
    %loading the perviously trained CNN
    load MCNN;
    load MTraining; 
    
    Testing = denoiseImage(Testimage,MTraining);
    imshowpair(Testing,Testimage,'montage');
    imwrite(Testing, 'MaskingOutput.png','png');

end