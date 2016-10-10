prompt = 'Enter video dir with trailing slash or backslash: ';
vidPath = input(prompt,'s');
allVids = dir(strcat(fullfile(vidPath,'*.mp4')));
vidCount = size(allVids);
outfile = fopen(fullfile(pwd(),'motionVects'),'w');
r = 2;

r = input('please enter r val:');
siftVectAccu = [];
for vidNum = 1:vidCount(1)
    file = allVids(vidNum).name;
    indiFilePath = fullfile(vidPath,file);
    executable = fullfile(pwd(),'mail_output\\motionvrdemo.exe');
    readVid = VideoReader(indiFilePath);
    mvrOp = fullfile(pwd(),'mvrop.txt');
    cmd = strcat(executable,{' '},indiFilePath,'>',mvrOp);
    system(char(cmd));
    readFromOp = fileread(fullfile(pwd(),'mvrop.txt'));
    linProcess = strsplit(readFromOp,'\n');
    sizeOfLines = size(linProcess);
    spaceProcess = [];
    for i=1:sizeOfLines(2)
        splitSize = size(strsplit(char(linProcess(i)),','));
        if splitSize(2)==1
            continue;
        end
        spaceProcess = [spaceProcess;strsplit(char(linProcess(i)),',')];
    end
    linNums = size(linProcess);
    spaceProcSize= size(spaceProcess);
    finArr = [];
    for z=1:spaceProcSize(1)
      x = ceil(str2double(spaceProcess(z,9)));
      y = ceil(str2double(spaceProcess(z,10)));
      ht = ceil(str2double(spaceProcess(z,2)));
      wt = ceil(str2double(spaceProcess(z,3)));
      firstVal = floor((y*r)/ht);
      if firstVal > (r-1)
        firstVal = r-1;
      end
      secondVal = floor((x*r)/wt);
      if secondVal > (r-1)
        secondVal = r-1;
      end
      computedVal = (firstVal*r) + (secondVal+1);
      finArr = [finArr computedVal];
    end
    finArr = finArr';
    finArr = fix(finArr);
    [rowVidName,colVidName] = size(finArr);
    vidName = cell(rowVidName,1);
    vidName(:) = cellstr(file);
    siftVectAccu = [siftVectAccu;horzcat(vidName,spaceProcess,num2cell(finArr))];
end
fileName = 'out_file.mvect';
fid = fopen(fileName,'wt');
formatSpec = '%s %s %s %s %s %s %s %s %s %s %s %f \n';
[nrows,ncols] = size(siftVectAccu);
for row = 1:nrows
    fprintf(fid,formatSpec,siftVectAccu{row,:});
end

%fprintf(fid,siftVectAccu);
fclose(fid);