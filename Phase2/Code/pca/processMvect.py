#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sbhar
#
# Created:     22/10/2016
# Copyright:   (c) sbhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
def filterMvect(motionVrPath):
    fr=open(os.path.join(motionVrPath,"out_file.mvect"),"r")
    filteredFile=os.path.join(motionVrPath,"out_file.mvect.filtered")
    fw=open(filteredFile,"w")
    lines=fr.readlines()
    for line in lines:
        tokens=line[:len(line)-1].split(",")
        src_x=int(tokens[3])
        src_y=int(tokens[4])
        dst_x=int(tokens[5])
        dst_y=int(tokens[6])
        diffVr=(dst_x-src_x,dst_y-src_y)
        if not diffVr==(0,0):
            newLine=tokens[0]+","+str(tokens[1])+","+str(tokens[2])+","+str(dst_x)+","+str(dst_y)+","+str(diffVr[0])+","+str(diffVr[1])+"\n"
            #newLine=tokens[0]+","+str(tokens[1])+","+str(tokens[2])+","+str(diffVr[0])+","+str(diffVr[1])+"\n"
            #newLine=line
            fw.write(newLine)
    fr.close()
    fw.close()
    return filteredFile


def main():
    None
    #filterMvect()

if __name__ == '__main__':
    main()
