import cv2
import numpy as np
import os

path = "./"
file_list = os.listdir(path)
img_list = [file for file in file_list if file.endswith(".jpg")]
print(img_list)

img_array = []

for img in img_list :
    img_array.append(cv2.imread(img, 1))

temp = np.concatenate((img_array), axis=0) # 배열의 크기가 같아야 한다.


cv2.imwrite('./finish.jpg', temp)
print("이미지 저장이 완료되었습니다.")