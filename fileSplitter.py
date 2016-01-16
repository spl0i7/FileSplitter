#!/usr/bin/env python
import os
import sys
import shutil
def fileSplitter(file,chunk,tmpDirname):
    fileSize=os.path.getsize(file)
    chunk=chunk-1
    chunkSize=fileSize/chunk
    print("File Size : "+str(fileSize)+ " bytes")
    print("Chunk Size : "+str(chunkSize)+ " bytes")
    print("Parts : "+ str(chunk+1))
    print("")
    pointer=chunkSize
    tmpfileName='part'
    tmpFilecount=0
    configureDir(tmpDirname)
    fr=open(file,'rb')
    while (True):
        fr.seek(pointer-chunkSize)
        buf=fr.read(chunkSize)
        if(buf==''):
            break
        fw=open(tmpDirname+'/'+tmpfileName+str(tmpFilecount),'wb')
        fw.write(buf)
        fw.close()
        pointer+=chunkSize
        tmpFilecount+=1


def cleanupTmp(tmpDirname):
    shutil.rmtree(tmpDirname)


def fileMerger(tmpDirname,finalFileName,parts):
    tmpfileName='part'
    tmpFilecount=0
    while(tmpFilecount < parts):
        fr=open(tmpDirname+'/'+tmpfileName+str(tmpFilecount),'rb')
        buf=fr.read(os.path.getsize(tmpDirname+'/'+tmpfileName+str(tmpFilecount)))
        fw=open(finalFileName,'ab')
        fw.write(buf)
        fw.close()
        fr.close()
        tmpFilecount+=1
    cleanupTmp(tmpDirname)

def printman():
    print("[+] Simple Python File Splitter")
    print("[+] by spl0i7 https://www.ketansingh.me")
    print("[+] To split usage : "+sys.argv[0]+" s <file> <parts> <path to store parts>")
    print("[+] To merge back : "+sys.argv[0]+" m <new filename> <parts> <path of parts>")



def configureDir(dirName):
    try:
        if(os.path.exists(dirName)):
            shutil.rmtree(dirName)
        os.mkdir(dirName)
    except OSError:
        print("Error happened in creating tmp dir")


if len(sys.argv )==5:
    if(sys.argv[1]=="s"):
        fileSplitter(sys.argv[2],int(sys.argv[3]),sys.argv[4])
    elif(sys.argv[1]=="m"):
        fileMerger(sys.argv[4],sys.argv[2],int(sys.argv[3]))
    else :
        printman()
else:
    printman()
