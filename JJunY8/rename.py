import sys
import os

def getfolderPath(path):

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


'''
def importPathImages():
    path = "./"
    file_list = os.listdir(path)
    imgfile_list = [file for file in file_list if file.endswith(".jpg") or file.endswith(".png")]

    inputvalue = int(input('입력하시오 : '))

    for name in imgfile_list :
        intinputvalue = str(inputvalue)
        src = os.path.join(path, name)
        dst = 'extra_image' + intinputvalue + '.jpg'
        dst = os.path.join(path, dst)
        os.rename(src, dst)
        inputvalue += 1
'''

if __name__ == '__main__':

    sourcepath = input("원본 절대경로 입력 : ")
    destinationpath = input("옮길 곳 절대경로 입력 : ")
    indexstart = input("시작 번호 : ")


    folderPath_list = getfolderPath(sourcepath)
    filePath_list = []

    print(folderPath_list)

    index = 0
    index2 = int(indexstart)

    for folderpath in folderPath_list :
        try:
            k = os.listdir(folderpath)
            src = folderpath + os.sep
            dst = destinationpath + os.sep
            for file in k :
                os.rename(src + file, dst + str(index2) + '.jpg')
                index2 += 1
            #os.replace(src + k[index], dst + k[index])

        except NotADirectoryError as e:
            pass
        index = 0




        '''k = getFilePath(folderpath)
        filePath_list.append(k)'''

    '''index = 0
    for path in filePath_list :
        for path2 in filePath_list[index] :
            src = path2
            dst = destinationpath


        index = 0'''