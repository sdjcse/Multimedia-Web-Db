prompt = 'Please enter the r Value';
binPrompt = 'Please enter n for bin value: ';
pathPrompt = 'Please enter video path with trailing slash or backslash: ';

r = 2;
r = input(prompt);
binVal = input(binPrompt);
filePath = input(pathPrompt,'s');
files = dir(strcat(filePath,'*.mp4'));
% path = '/home/sdj/CourseAssignments/CSE515/Phase1/DataR/';
strToWrite = '';
%r = 2;
cellCount = 1;
for itr = 1:size(files)
  %strToWrite = '';
  mainVid = VideoReader(strcat(filePath,files(itr).name));
  heightDiv = int8(floor(mainVid.Height/r));
  widthDiv = int8(floor(mainVid.Width/r));
  modhgt = mod(mainVid.Height,r);
  modwdt = mod(mainVid.Width,r);
  vidDet = [];
  vidNum = [];
  frameNums = [];
  for frameNum = 1:mainVid.NumberOfFrames
    % Reading one frame from video
    rgbArr(:,:,:,frameNum) = rgb2gray(read(mainVid,frameNum));
    test = rgb2gray(read(mainVid,frameNum));
    % Taking one frame
    i = rgbArr(:,:,:,frameNum);
    % Splitting the frame according to the given r value
    hgt = heightDiv*int8(floor(ones(1,size(i,1)/heightDiv)));
    hgt(int8(floor(ones(1,size(i,1)/heightDiv)))) = hgt(int8(floor(ones(1,size(i,1)/heightDiv)))) + modhgt;

    %hgt(1,size(i,1)/heightDiv) = hgt(1,size(i,1)/heightDiv)+modhgt;

    wdt = widthDiv*int8(floor(ones(1,size(i,2)/widthDiv)));
    wdt(int8(floor(ones(1,size(i,1)/widthDiv)))) = wdt(int8(floor(ones(1,size(i,1)/widthDiv)))) + modwdt;
    g = mat2cell(i,hgt,wdt);
    vidDet = [itr frameNum ];
    cellCount = 1;
    for x=1:size(g(:,1))
      for y = 1:size(g(:,2))
        individualCell = cell2mat(g(x,y));
        [storable,junk] = imhist(individualCell,binVal);
        storable = storable';
        storable = [itr frameNum cellCount storable];
        strToWrite = strcat(strToWrite,mat2str(storable));
        strToWrite = strcat(strToWrite,'\n');
        cellCount=cellCount+1;
      end
    end
    cellCount = 1;
  end
  fileName = 'out_file.chst';
  fid = fopen(fileName,'wt');
  fprintf(fid,strToWrite);
  fclose(fid);
end
