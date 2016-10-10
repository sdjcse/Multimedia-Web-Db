prompt = 'Please enter the r Value';
promptPath = 'Please enter the path of video files with trailing slash or backslash: ';
r = 2;
r = input(prompt);
path = input(promptPath,'s');
files = dir(strcat(path,'*.mp4'));
%path = 'C:\MWD\vids\';
strToWrite = '';
%r = 2;
siftVectAccu = [];
for itr = 1:size(files)
  %strToWrite = '';
  mainVid = VideoReader(strcat(path,files(itr).name));
  heightDiv = int8(floor(mainVid.Height/r));
  widthDiv = int8(floor(mainVid.Width/r));
  modhgt = mod(mainVid.Height,r);
  modwdt = mod(mainVid.Width,r);
  for frameNum = 1:mainVid.NumberOfFrames
    % Reading one frame from video
    vidNbr = [];
    frameNbr = [];
    finArr = [];
    rgbArr(:,:,:,frameNum) = rgb2gray(read(mainVid,frameNum));
    % Taking one frame
    i = rgbArr(:,:,:,frameNum);
    % Splitting the frame according to the given r value
    [frames1,descr1,gss1,dogss1] = sift(im2double(i)) ;
    siftVect = [frames1;descr1];
    [siftRows,siftCols] = size(siftVect);

    for z=1:siftCols
      x = ceil(siftVect(1,z));
      y = ceil(siftVect(2,z));
      firstVal = floor((y*r)/mainVid.Height);
      if firstVal > (r-1)
        firstVal = r-1;
      end
      secondVal = floor((x*r)/mainVid.Width);
      if secondVal > (r-1)
        secondVal = r-1;
      end
      computedVal = (firstVal*r) + (secondVal+1);
      finArr = [finArr computedVal];
    end
    vidNbr(1:siftCols) = itr;
    frameNbr(1:siftCols) = frameNum;
    siftVectAccu = [siftVectAccu [vidNbr;frameNbr;finArr;siftVect]];
  end
end
fileName = 'out_file.sift';
fid = fopen(fileName,'wt');
%siftVectAccu = siftVectAccu';
strOp = mat2str(siftVectAccu');
writable = strrep(strOp,';',' \n ');
fprintf(fid,writable);
fclose(fid);
