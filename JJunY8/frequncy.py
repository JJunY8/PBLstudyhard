import cv2
import os
import numpy as np
import collections
from matplotlib import pyplot as plt
import sys

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

#폴더 내의 이미지 경로 불러오기
def importPathImages():

    path = "./extraImage/"
    file_list = os.listdir(path)
    imgfile_list = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png")]
    imgtitle_list = imgfile_list

    index = 0

    for addPath in imgfile_list :
        imgtitle_list[index] = path + '/' + addPath
        index += 1

    return imgfile_list, imgtitle_list

#이미지를 가공할 수 있는 형태로 불러오기
def importImages(imgfile_list):

    decodedImagesArray = []

    for transfile in imgfile_list :
        originImage = np.fromfile(transfile, np.uint8)
        decodedImage = cv2.imdecode(originImage, 0)
        decodedImagesArray.append(decodedImage)

    return decodedImagesArray

#이미지 한 장에 대한 주파수 변환
def transFrequency(decodedImage) :

    frequency = np.fft.fft2(decodedImage)

    return frequency

#이미지 한 장에 대한 필요값 도출
def pickNeededValue(decodedImage) :

    #이미지 한 장에 대한 필요값 정의
    AllmaxPos, AllminPos, Allmax, Allmin, AllListPixcel = [], [], [], [], []
    counted_dict = collections.Counter({})

    #이미지 한 장의 한 줄에 대한 처리
    for imageWidth in decodedImage :

        width = len(imageWidth)
        maxPos, minPos = [], []

        maxValue = max(imageWidth)
        minValue = min(imageWidth)

        setPixcel = set(imageWidth)
        listPixcel = [x for x in setPixcel]
        listPixcel.sort()

        if maxValue == minValue :
            for findPos in range(0, width):
                if imageWidth[findPos] == maxValue:
                    maxPos.append(findPos)
            Allmax.append(maxValue)
            Allmin.append(300)
        else :
            for findPos in range(0, width):
                if imageWidth[findPos] == maxValue:
                    maxPos.append(findPos)
                if imageWidth[findPos] == minValue :
                    minPos.append(findPos)
            Allmax.append(maxValue)
            Allmin.append(minValue)

        #한 줄씩 처리한 것을 모으기(> 한 장)
        AllmaxPos.append(maxPos)
        AllminPos.append(minPos)
        AllListPixcel.append(listPixcel)

        counting_dict = collections.Counter(imageWidth.tolist())
        counted_dict = counted_dict + counting_dict

    sorted_counted_dict = sorted(counted_dict.items())

    #한 장에 대한 값 내보내기
    return Allmax, Allmin, AllmaxPos, AllminPos, AllListPixcel, sorted_counted_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    #폴더 내에 있는 모든 이미지의 프리퀀시 값 저장
    frequencylist = []

    #폴더 내에 있는 모든 이미지의 필요 값 저장
    maxparent, minparent, maxposparent, minposparent, listpixcelparent, sorted_counted_dict_parent = [], [], [], [], [], []

    imagefilelist, imagetitlelist = importPathImages()
    decodedImagesArray = importImages(imagetitlelist)

    #cell은 단위가 한 장
    for cell in decodedImagesArray :
        frequency = [] #메모리 비워주기 위함.
        frequency = transFrequency(cell)
        frequencylist.append(frequency)

    index = 0

    #cell은 단위가 한 장
    for cell in decodedImagesArray :
        maxchild, minchild, \
        maxposchild, minposchild, \
        listpixcelchild, sorted_counted_dict_child = [], [], [], [], [], [] #메모리 비워주기 위함.

        maxchild, minchild, \
        maxposchild, minposchild, \
        listpixcelchild, sorted_counted_dict_child = pickNeededValue(cell)

        maxparent.append(maxchild)
        minparent.append(minchild)
        maxposparent.append(maxposchild)
        minposparent.append(minposchild)
        listpixcelparent.append(listpixcelchild)
        sorted_counted_dict_parent.append(sorted_counted_dict_child)

        sys.stdout = open(imagefilelist[index] + '.txt', 'w')
        print(maxchild)
        print(minchild)
        print(maxposchild)
        print(minposchild)
        print(listpixcelchild)
        print(sorted_counted_dict_child)
        sys.stdout.close()

        index += 1

    '''with open('decodedImages.txt', 'w', encoding='UTF-8') as f :
        index = 0
        for images in decodedImagesArray :
            f.write(str(imagefilelist[index])+' : '+str(images)+'\n')
            index += 1
    f.close()

    with open('frequencyes.txt', 'w', encoding='UTF-8') as f :
        index = 0
        for frequencies in frequencylist :
            f.write(str(imagefilelist[index]) + ' : ' + str(frequencies) + '\n')
            index += 1
    f.close()

    with open('neededValue.txt', 'w', encoding='UTF-8') as f :
        index = 0
        for values in range(0, len(maxparent)) :
            f.write(str(imagefilelist[index])
                    + ' : 최대값들 ' + str(maxparent[values])
                    + '\n 최대값의 각 위치 ' + str(maxposparent[values])
                    + '\n 최소값들 ' + str(minparent[values])
                    + '\n 최소값의 각 위치 ' + str(minposparent[values])
                    + '\n 가로 한 줄 색상 : ' + str(listpixcelparent[values])
                    + '\n')
            index += 1'''
