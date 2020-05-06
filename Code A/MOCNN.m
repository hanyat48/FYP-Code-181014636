%This CNN is for training the CNN and masking images 
function MCNN = MOCNN(FilePath1)

%Image datastore that will be used for denoising.
%Converts IMDS into Denoising Image Datastore
dnimds = denoisingImageDatastore(imageDatastore(FilePath1));

%creates denoising CNN layers
Layers = dnCNNLayers('NetworkDepth',20);

%training options 
%uses ADAM optimizer 
%20 epochs
%learning rate at 0.01
Toptions = trainingOptions('adam', ...
    'MaxEpochs',20,...
    'InitialLearnRate',0.001, ...
    'Verbose',true, ...
    'Plots','training-progress');

%saves pre-trained CNN
save MCNN;

%trains the network using options
MTraining = trainNetwork(dnimds,Layers,Toptions);
%saves trained network
save MTraining; 
%outputs trained network
MCNN = MTraining;
%saves trained network 
save MCNN;

%prompts the user to enter a testing image 
prompt ='Please enter the name of your image, i.e "Image1.png"';
test = input(prompt, 's');

%testing the image, has to be in grayscale
testingImage = imread(test);
%using denoise image to test image
mn = denoiseImage(testingImage,MTraining);

%outputs the network and the layers
analyzeNetwork(MTraining);

%shows before and after on testing image
imshowpair(mn,testingImage,'montage');
%outputs tested image into folder
imwrite(mn,'MTestedImage.png','png');

end 