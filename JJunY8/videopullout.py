#프레임 추출기 라이브러리
from ast import Break
import cv2
import os

#유튜브 무한 스크롤러 라이브러리


#유튜브 다운로더 라이브러리
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())

#무한 스크롤러 코드
def scroll():
    try:
        # 페이지 내 스크롤 높이 받아오기
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            # 임의의 페이지 로딩 시간 설정
            # PC환경에 따라 로딩시간 최적화를 통해 scraping 시간 단축 가능
            pause_time = random.uniform(1, 2)
            # 페이지 최하단까지 스크롤
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            # 페이지 로딩 대기
            time.sleep(pause_time)
            # 무한 스크롤 동작을 위해 살짝 위로 스크롤(i.e., 페이지를 위로 올렸다가 내리는 제스쳐)
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight-50)")
            time.sleep(pause_time)
            # 페이지 내 스크롤 높이 새롭게 받아오기
            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
            # 스크롤을 완료한 경우(더이상 페이지 높이 변화가 없는 경우)
            if new_page_height == last_page_height:
                print("스크롤 완료")
                break

            # 스크롤 완료하지 않은 경우, 최하단까지 스크롤
            else:
                last_page_height = new_page_height

    except Exception as e:
        print("에러 발생: ", e)

#검색 키워드 input

SEARCH_KEYWORD = input('검색어를 입력하세요 : ').replace(' ', '+')

driver = webdriver.Chrome(service=service)
# 스크래핑 할 URL 세팅
URL = "https://www.youtube.com/results?search_query=" + SEARCH_KEYWORD
# 크롬 드라이버를 통해 지정한 URL의 웹 페이지 오픈
driver.get(URL)
# 웹 페이지 로딩 대기
time.sleep(3)
# 무한 스크롤 함수 실행
scroll()

# 페이지 소스 추출
html_source = driver.page_source
soup_source = BeautifulSoup(html_source, 'html.parser')

# 모든 콘텐츠 정보
content_total = soup_source.find_all(class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
# 콘텐츠 제목만 추출
content_total_title = list(map(lambda data: data.get_text().replace("\n", ""), content_total))
# 콘텐츠 링크만 추출
content_total_link = list(map(lambda data: "https://youtube.com" + data["href"], content_total))
# 딕셔너리 포맷팅
content_total_dict = {'title' : content_total_title, 'link': content_total_link}






#유튜브 다운로더 코드
DOWNLOAD_FOLDER = './VideoFile./'
url = content_total_link[0]
while True:

    yt = YouTube(url)

    title = yt.title

    try:
        yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = './VideoFile./')
        filename = title + ".mp4" #제목도 크롤링해서 동영상 제목으로 넣는코드로 개선
        print("유튜브 다운로드 완료")
    except:
        print("Youtube Download Error")


    if url == 'q' :
        break

#프레임 추출기 코드
    path = "/VideoFile/"
    file_list = os.listdir(path)
    video_list = [file for file in file_list if file.endswith(".mp4")]

    while True : #기존에 디렉토리가 있으면 넘어가기 위해 while문에 넣음

        title = video_list[index]#index 구현 안 함. 해줘야해용.->???ㅠㅠ?


        if title[:4] in file_list : #폴더 이름 생성 규칙에 따라서 검사 코드 짜

            for videofile in video_list :
                video = cv2.VideoCapture(videofile)

            if not video.isOpened():
                print("Could not Open :", videofile)
                exit(0)

            length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = video.get(cv2.CAP_PROP_FPS)

        #프레임을 저장할 디렉토리를 생성
            try:
                if not os.path.exists(videofile[:4]):
                    os.makedirs(videofile[:4])
            except OSError:
                print ('Error: Creating directory. ' +  videofile[:-4])

            count = 0

            while(video.isOpened()):
                ret, image = video.read()
                if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
                    cv2.imwrite(videofile[:-4] + "/frame%d.jpg" % count, image)
                    print('Saved frame number :', str(int(video.get(1))))
                    count += 1

            video.release()

        else :
            continue