%This script is for Code B- Image Registration 

%prompts the user for the file path of the moving image 
Moving = input('Please enter the filepath of the Moving image i.e Image.png', 's');
%It reads the png image or file path the moving image
MI = imread(Moving);
%it calculates the number of dimensions in the array
dimensionsImg = ndims(MI);
%if the no. of dimensions is larger than 2 then trun it into gray scale
if dimensionsImg > 2
    MI = rgb2gray(MI);
end

%prompts the user for the file path of the fixed image 
Fixed = input('Please enter the filepath of the Fixed image i.e Image.png', 's');
%It reads the png image or file path the fixed image
FI = imread(Fixed);
%it calculates the number of dimensions in the array
dimensionsImg = ndims(FI);
%if the no. of dimensions is larger than 2 then trun it into gray scale
if dimensionsImg > 2
    FI = rgb2gray(FI);
end
%figure showing before
figure("Name", "Before");
imshowpair(FI, MI,'Scaling','joint'); %in purple green 

% MONOMODAL REGISTRATION 
%uncommnent below to use monomodal registration then comment out the optmizer and metric section of the Multimodal registration.
% %optimizer for modal
% % optimizer = registration.optimizer.RegularStepGradientDescent();
% % metric = registration.metric.MeanSquares();
% %modifying the regular step gradient 
% % optimizer.MaximumIterations = 300;
% % optimizer.MinimumStepLength = 5e-4;

% MULTIMODAL REGISTRATION
%optimizer and metric choosen for multimodal operation 
optimizer = registration.optimizer.OnePlusOneEvolutionary();
metric = registration.metric.MattesMutualInformation();

%modifying the one plus one evolutionary 
%we modifiy it so the transformation matrix is at its global maximum 
optimizer.InitialRadius = 0.009;
optimizer.Epsilon = 1.5e-6;
optimizer.GrowthFactor = 1.01;
optimizer.MaximumIterations = 500;
optimizer.InitialRadius = optimizer.InitialRadius/4.5;

%MULTIMODAL Translation Registration
movingRegistered = imregister(MI,FI, 'affine', optimizer, metric);

%MULTIMODAL Similarity and Rigid Registration 
%using imregtform to use the geometeric function
tformSimilarity = imregtform(MI,FI,'similarity',optimizer,metric);
Rfixed = imref2d(size(FI));
movingRegisteredRigid = imwarp(MI,tformSimilarity,'OutputView',Rfixed);

%MULTIMODAL Affine Registration 
movingRegisteredAffineWithIC = imregister(MI,FI,'affine',optimizer,metric,...
    'InitialTransformation',tformSimilarity);


%figures showing the after images
figure('Name', 'After- Translation Registration');
imshowpair(FI, movingRegistered,'Scaling','joint');
figure('Name', 'After- Rigid Registration');
imshowpair(movingRegisteredRigid, FI);
figure('Name', 'After- Affine Registration');
imshowpair(movingRegisteredAffineWithIC,FI);
