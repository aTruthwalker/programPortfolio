%cells 1-320 are for training and finding our model 
%cells 321-400 are for dummy prediction practice
%remember to omit zero values from our graphs so they dont skew us
%just make a copy of those that have those zeroes and replace those zeroes
%entries with Nan.
%for now, its fine to have the zeroes in when finding the multi-linear
%model

%plan for program.  First, centrilize our data into new matrices

%sqft



sz = size(sqft);
sqftCenter = zeros(sz);

for i = 1:sz
    sqftCenter(i) = (sqft(i) - mean(sqft));
end
%baths
sz = size(baths);
bathsCenter = zeros(sz);

for i = 1:sz
    bathsCenter(i) = (baths(i) - mean(baths));
end
%beds
sz = size(beds);
bedsCenter = zeros(sz);

for i = 1:sz
    bedsCenter(i) = (beds(i) - mean(beds));
end

%basement
sz = size(basement);
basementCenter = zeros(sz);

for i = 1:sz
    basementCenter(i) = (basement(i) - mean(basement));
end

%garage
sz = size(garage);
garageCenter = zeros(sz);

for i = 1:sz
    garageCenter(i) = (garage(i) - mean(garage));
end

%year
sz = size(yearbuilt);
yearbuiltCenter = zeros(sz);

for i = 1:sz
    yearbuiltCenter(i) = (yearbuilt(i) - mean(yearbuilt));
end

%center our y, saleprice
sz = size(saleprice);
salepriceCenter = zeros(sz);

for i = 1:sz
    salepriceCenter(i) = (saleprice(i) - mean(saleprice));
end

%with these centralize variables, we now have removed the y-intercept

%we now create the matrix of all predictors, called X here.
X = [basementCenter,bathsCenter, bedsCenter, garageCenter,sqftCenter, yearbuiltCenter];

%AND REGRESSION!

B = regress( salepriceCenter, X); %the garage, basements, and yearbuilt data is skewing this one

X2 = [bathsCenter, bedsCenter, sqftCenter];

B2 = regress(salepriceCenter, X2); %this is what my model would have been originally


%repeat for B, but only use first 200 elements.

%first, we partition new matrices from our old ones. 
limit = 200;


basement2 = zeros(limit, 1);

for i = 1:limit
    basement2(i) = basement(i);
end


baths2 = zeros(limit, 1);

for i = 1:limit
    baths2(i) = baths(i);
end


beds2 = zeros(limit, 1);

for i = 1:limit
    beds2(i) = beds(i);
end


garage2 = zeros(limit, 1);

for i = 1:limit
    garage2(i) = garage(i);
end


saleprice2 = zeros(limit, 1);

for i = 1:limit
    saleprice2(i) = saleprice(i);
end


sqft2 = zeros(limit, 1);

for i = 1:200
    sqft2(i) = sqft(i);
end


yearbuilt2 = zeros(limit, 1);

for i = 1:limit
    yearbuilt2(i) = yearbuilt(i);
end


%uncentralized version
X3 = [basement2, baths2, beds2, garage2, sqft2, yearbuilt2];
B3 = regress(saleprice2, X3);

%Centralized version



basement2Center = zeros(limit, 1);
for i = 1:limit
    basement2Center(i) = (basement2(i) - mean(basement2));
end


baths2Center = zeros(limit, 1);
for i = 1:limit
    baths2Center(i) = (baths2(i) - mean(baths2));
end



beds2Center = zeros(limit, 1);
for i = 1:limit
    beds2Center(i) = (beds2(i) - mean(beds2));
end



garage2Center = zeros(limit, 1);
for i = 1:limit
    garage2Center(i) = (garage2(i) - mean(garage2));
end



saleprice2Center = zeros(limit, 1);
for i = 1:limit
    saleprice2Center(i) = (saleprice2(i) - mean(saleprice2));
end


sqft2Center = zeros(limit, 1);
for i = 1:limit
    sqft2Center(i) = (sqft2(i) - mean(sqft2));
end


yearbuilt2Center = zeros(limit, 1);
for i = 1:limit
    yearbuilt2Center(i) = (yearbuilt2(i) - mean(yearbuilt2));
end

X4 = [basement2Center, baths2Center, beds2Center, garage2Center, sqft2Center, yearbuilt2Center];

B4 = regress(saleprice2Center, X4);


%201-218 are for testing

prediction = ones(18,1);

for i =1:18
    prediction(i) = (B4(1)*basementCenter(200+i)) + (B4(2)*bathsCenter(200+i)) + (B4(3)*bedsCenter(200+i)) + (B4(4)*garageCenter(200+i)) + (B4(5)*sqftCenter(200+i)) + (B4(6)*yearbuiltCenter(200+i));
end

error = ones(18, 1);
for i = 1:18
    error(i) = (salepriceCenter(i) - prediction(i));
    error(i) = error(i).^2;
end


MSE = mean(error);
RMSE = sqrt(MSE);

prediction2 = ones(18,1);
for i = 1:18
    prediction2(i) = B2(1)*bathsCenter(200+i) + B2(2)*bathsCenter(200+i) + B2(3)*sqftCenter(200+i);
end


error2 = ones(18, 1);
for i = 1:18
    error2(i) = (salepriceCenter(i) - prediction2(i));
    error2(i) = error2(i).^2;
end

MSE2 = mean(error2);
RMSE2 = sqrt(MSE2);
