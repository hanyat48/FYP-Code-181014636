%This CNN is for training the CNN and denoising images 
function TCNN = TOCNN(FilePath1)

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
    'InitialLearnRate',0.01, ...
    'Verbose',true, ...
    'Plots','training-progress');

%saves pre-trained CNN
save TCNN;

%trains the network using options
Training = trainNetwork(dnimds,Layers,Toptions);
%saves trained network
save Training; 
%outputs trained network
TCNN = Training;
%saves trained network 
save TCNN;

%prompts the user to enter a testing image 
prompt ='Please enter the name of your image, i.e "Image1.png"';
test = input(prompt, 's');

%testing the image, has to be in grayscale
testingImage = imread(test);
%using denoise image to test image
dn = denoiseImage(testingImage,Training);

%outputs the network and the layers
analyzeNetwork(Training);

%shows before and after on testing image
imshowpair(dn,testingImage,'montage');
%outputs tested image into folder
imwrite(dn,'TestedImage.png','png');

end 