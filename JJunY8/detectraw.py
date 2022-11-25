'''import shutil
from PIL import Image
from pytesseract import *
import cv2
import os

def getPath(path):
    try :
        if os.path.isdir(path) :

    except NotADirectoryError as e :

    folder_list = os.listdir(path)
    folderPath_list = []
    for i in folder_list :
        k = path + os.sep + i
        folderPath_list.append(k)
    return folderPath_list

def getFilePath(path):

    try :

        file_list = os.listdir(path)
        filePath_list = []
        for i in file_list:
            k = path + os.sep + i
            filePath_list.append(k)
        return file_list, filePath_list

    except NotADirectoryError as e :
        print(e)

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def ocrtostr(full_path, filename, lang='kor'):
    img = Image.open(full_path)#이미지 경로
    #추출
    outText = image_to_string(img, lang=lang, config= '--psm 1 -c preserve_interword_spaces=25')
    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인
    #psm = 페이지 세그먼트 모드.

    #출력
    print('File : ', filename, '\n')
    print(outText)

    return outText


#메인 시작
if __name__ == "__main__":

    root_paths = '.\Webtoon\Original'
    result = []
    #OCR 추출 작업 메인(result에 추출한 글자를 담아서 result의 길이가 0이 아니면 TextImage에 넣어서 따로 분류)
    for root, dirs, files in os.walk(root_paths):
        for f_name in files:
            fullName = os.path.join(root, f_name)
            print(fullName)
            #한글+영어 추출(kor, eng , kor+eng)
            result = ocrtostr(fullName, f_name,'kor+eng')

            #얘가 잘못된건가 result 배열에 넣는거?
            if len(result) != 0:
                if os.path.isdir('.\Webtoon\TextImage') == False:
                    os.mkdir('.\Webtoon\TextImage')
                    shutil.copy(fullName, '.\Webtoon\TextImage'+ os.sep + f_name)
                else :
                    shutil.copy(fullName, '.\Webtoon\TextImage' + os.sep + f_name)

                #Original을 오리지널 폴더에 담긴 사진으로 고치기'''