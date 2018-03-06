#!/usr/bin/python
import os
import re

def ListFilesToTxt1(dir1):
    files = os.listdir(dir1)
    fileNames = list()
    for file in files:
        fileName = re.findall('([^<>/\\\|:""\*_?]+)\.\w+$',file)
        fileNames.append(fileName)
    return fileNames

def ListFilesToTxt2(dir2):
    files = os.listdir(dir2)
    fileNames = list()
    for file in files:
        fileName = re.findall('([^<>/\\\|:""\*_?]+)_.+\.\w+$',file)
        fileNames.append(fileName)
    return fileNames


def DelFilesFromList(dir2, rmlist, objlist):
    os.chdir(dir2)
    files = os.listdir(dir2)
    dic = dict(zip(files, objlist))
    for dickey, dicvalue in dic.items():
        if dicvalue in rmlist:
            print("Will delete this file:" ,dickey)
#            os.remove(dickey)
#            print('Done')

def Del():
    dir1 = "D:/GitHub_repo/fileDel - 副本/2014_del"
    dir2 = "D:/GitHub_repo/fileDel - 副本/2014"
    dir3 = "/home/xiaob6/dehaze/dehazenet/ClearImages/TrainImages/clear_images" #training clear
    dir4 = "/home/xiaob6/dehaze/dehazenet/HazeImages/TrainImages/OTS"  # training haze
    dir5 = "/home/xiaob6/dehaze/dehazenet/ClearImages/TestImages "  # test clear
    dir6 = "/home/xiaob6/dehaze/dehazenet/HazeImages/TestImages "  # test haze
    rmlist = ListFilesToTxt1(dir3)
    objlist = ListFilesToTxt2(dir4)
    DelFilesFromList(dir4, rmlist, objlist)

Del()