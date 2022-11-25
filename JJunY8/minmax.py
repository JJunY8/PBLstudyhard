import cv2
import os
import numpy as np
import collections
import sys
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

if __name__ == '__main__':

    # 폴더 내 모든 이미지 가져오기
    path = "./"
    file_list = os.listdir(path)
    img_list = [file for file in file_list if file.endswith(".jpg")]

    for transimg in img_list:

        # 이미지 불러오기
        image = cv2.imread(transimg)  # 이미지 로드
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # RGB로 데이터 변경
        image = image.reshape((image.shape[0] * image.shape[1], 3))  # heignt, width 한 개의 array로 통합

        # scikit-learn의 k-mean 알고리즘으로 이미지를 학습
        # k개의 데이터 평균을 만들어 데이터를 clustering(군집화)함
        k = 5
        clt = KMeans(n_clusters=k)
        clt.fit(image)

        # clustering 된 컬러 값 확인
        for center in clt.cluster_centers_:
            print(center)

        # 각 컬러의 퍼센트 확인
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()
        print(hist)

        # 추출한 값을 그래프로 그리기
        bar = np.zeros((50, 300, 3), dtype="uint8")  # 그래프 초기화
        startX = 0

        for (percent, color) in zip(hist, clt.cluster_centers_):
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
            startX = endX

        plt.axis('off')  # 화면 상의 x축, y축 제거
        # plt.imshow(bar)
        # plt.show()
        plt.imsave('bar_' + transimg, bar)