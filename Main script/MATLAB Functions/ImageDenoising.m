%Code A - Denoising put into a function for Main script
function Testing = ImageDenoising(Filepath)
    
    %This trains the CNN with the newest training data
    octDenoisingCNN = TOCNN(Filepath);
 
    % inputing and changing the image into gray scale
    Testimage = imread(Filepath);
    
    %loading the perviously trained CNN
    load TCNN;
    load Training; 
    
    %denoises the image using the trained CNN
    Testing = denoiseImage(Testimage,Training);
    %displays the before and after images
    imshowpair(Testing,Testimage,'montage');
    %saves the after image in workspace
    imwrite(Testing, 'DenoisingOutput.png','png');

end