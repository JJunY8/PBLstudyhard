import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import sys
from pprint import pprint



np.set_printoptions(threshold=sys.maxsize)

#6~8줄 폴더 내 jpg파일 불러오는 코드
path = "./"
file_list = os.listdir(path)
img_list = [file for file in file_list if file.endswith(".jpg")]

#빈 파일을 먼저 생성
'''sys.stdout = open('stdout.txt', 'w')

#각 이미지마다 나눠서 텍스트 파일 저장
def write_file(src, count, lines): #src: 경로, count: 분할 파일에 붙일 인덱스, lines: 저장할 문자열
    origName = src.replace('.txt', '') #.txt 빼고 제목만 추출 (원본 파일)
    newName = origName + '_' + str(count) + '.txt' #제목 뒤에 붙이기 (분할 파일)

    with open(newName, 'w', encoding='utf8') as fw:
        fw.write('\ufeff')  # UTF-8 BOM 타입으로 파일을 저장
        fw.write("\n".join(lines))
        fw.close()

# 구분자를 만나면 구분자 전까지의 문자열을 저장하기 위해 write_file 함수를 호출한다.
def split_file(src, delimeter, startIndex):  # src: 경로, delimeter: 구분자, startIndex: 분할 파일에 붙일 인덱스
    lineList = []

    with open(src, 'r', encoding='utf-8') as orig_file:
        try:
            for line in orig_file:
                line = line.strip()
                if line.startswith(delimeter):  # 구분자를 만났을 때
                    write_file(src, startIndex, lineList)
                    lineList = []
                    lineList.append(line.split(delimeter)[1])
                    startIndex += 1
                else:  # 구분자가 있는 line은 제외하고 텍스트 추가
                    lineList.append(line)
        except Exception as e:
            print(e)

        if lineList:
            write_file(src, startIndex, lineList)'''

for transfile in img_list :
    img_array = np.fromfile(transfile, np.uint8) #kr 대응하기 위해 np로 불러옵니다.
    img = cv2.imdecode(img_array, 0) #flag 1:gray, cv2.IMREAD_COLOR:COLOR

    f = np.fft.fft2(img) #두 가지 옵션이 있습니다. -> np.fft.fft2(), np.fft.fft()

    sys.stdout = open('img_max_min' + transfile + '.txt', 'a')

    index = 0

    for i in img :


        maxPos = []
        minPos = []
        maxValue = 0
        minValue = 0
        width = 0

        maxValue = max(i)
        minValue = min(i)
        width = len(i)
        setImg = set(i)
        setImg = list(setImg)

        for k in range(0, width) :
            if i[k] == int(maxValue) :
                maxPos.append(k)
            if i[k] == int(minValue) :
                minPos.append(k)

        print("검사하는 라인 " + str(index))
        print("배열을 이루는 값 " + str(setImg))
        print("배열을 이루는 값의 개수 " + str(len(setImg)))
        print("가장 큰 값 " + str(maxValue))
        print("가장 큰 값의 위치 " + str(maxPos))
        print("가장 작은 값 " + str(minValue))
        print("가장 작은 값의 위치 " + str(minPos))
        print()
        index += 1

    print(index)
    sys.stdout.close()
    #위에서 만들어진 빈 파일에 행렬을 덧붙임


    '''sys.stdout = open('img'+ transfile + '.txt', 'a')
    pprint(img)
    sys.stdout.close()'''

    #실행
    '''split_file('stdout.txt', 'array', 1)'''

    #fshift = np.fft.fftshift(f) #shift연산이 없으면 순서대로 보이고, shift연산이 있으면 영역이 4>3>2>1로 보입니다. shift연산이 있는 편이 패턴은 더 잘 보입니다.

    '''magnitude_spectrum = 20*np.log(np.abs(f)) #이거 왜 하는지 아직 이해 못 함. 아시는 분 있으면 주석 달아주세요.

    index = 0

    for i in magnitude_spectrum:
        print(max(i))
        print(min(i))
        print()
        index += 1'''
    '''sys.stdout = open('magnitude_spectrum_max_min' + transfile + '.txt', 'a')

    for i in img:
        print(max(magnitude_spectrum[i]))
        print(min(magnitude_spectrum[i]))

    sys.stdout.close()
    print()'''
    '''sys.stdout = open('magnitude_spectrum' + transfile + '.txt', 'a')
    pprint(magnitude_spectrum)
    sys.stdout.close()'''


    '''plt.subplot(121), plt.imshow(img.astype(np.uint8), cmap = 'gray') #cmap에서 옵션을 정해줄 수 있습니다. gray로 하는 게 패턴 찾긴 좋음. 그냥 이미지로 저장하기 위한 코드입니다.
    plt.title('Input Image'), plt.xticks([]), plt.yticks([]) #이미지에 타이틀 달기
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.savefig('trans_0_fft2'+transfile.strip(".jpg")) # imshow로 띄운 이미지를 한 장으로 저장.'''


