%Function of Code C for Main script 
function Model= ImageReconstruction(Filepath,number)
    
    %for loop to generate all the images
    %change the number depending on the number of images there are in the folder
    for i=1: number  
        %read the image starting from the first one
        array = imread(strcat(Filepath,'Image_ (',sprintf('%d',number),').png'));
        %remove the background
        Z = imsubtract(array,100);
        %insert the B-scan into a 3D array
        A(:,:,number) = Z; 
    end
    
    figure(1,'Name', '3D Model');
    %shows the 3D image
    Model = volshow(A); 

end