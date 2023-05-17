#0517
#pip install beautifulsoup4
#오른쪽 아래 있는 3.9.13 누르고 base 선택 bs4에 밑줄이 사라지는걸 확인

from bs4 import BeautifulSoup

import requests  #이 모듈은 https 관련해서 요청? 을 하는 모듈임을 짐작 할 수 있음.

#사용자가 url(domain name)을 사용하면 DNS에 그 정보(요청-request)를 input 받아 DNS에서 진짜 사이트 ip 주소를 output(response)해준다.
#사용자가 진짜 ip 주소(숫자)로 기억하기는 힘들기 때문에 인간은 언어적인 주소로 기억하고 DNS에서 진짜 ip 주소를 output 해주는 것이다.

headers={
    "User-Agent" : "DongYang Mirea Univ"
}
'''
webpage =requests.get("https://n.news.naver.com/article/008/0004888290?cds=news_media_pc&type=editn",headers=headers)
print(webpage)
#print(webpage.content)  #입력한 웹페이지의 컨텐츠 확인
soup = BeautifulSoup(webpage.content,"html.parser")
#print(soup)

news=soup.select_one("#dic_area").get_text()
print(news)

webpage2=requests.get("https://www.khgames.co.kr/news/articleView.html?idxno=212859",headers=headers)
soup2=BeautifulSoup(webpage2.content,"html.parser")
news2=soup2.select_one("#article-view-content-div").get_text()
print(news2)
'''


#selenium
#뉴스 가져오기
#pip install selenium
#pip install sebdriver_manager
import time #기본으로 설치되어있는 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
'''
#(1) 뉴스를 가져온다.
driver.get("https://www.naver.com/")
time.sleep(3)

#원하는 버튼을 누르는 명령을 실행한다. --뉴스 버튼을 누른다
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(5)

newsTitle1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div").text

print(newsTitle1)

driver.get("https://m.land.naver.com/search")

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)
rentprice=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print(rentprice)

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/header/div/div[2]/a[1]/i").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("성원상떼빌")
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(1)
buyprice=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[1]/div/div/div[1]/div[4]/div/div/div/dl[1]/dd").text
print(buyprice)

driver.get("https://finance.naver.com/")
time.sleep(1)
subject1=driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a").text
subject2=driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a").text
subject3=driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a").text

print(subject1)
print(subject2)
print(subject3)


lst =[]
for i in range(10) :
    subject=driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
    lst.append(subject)

print(lst)
'''
driver.get("https://finance.naver.com/")
time.sleep(1)
lst1=[]
for i in range(10) :
    subject=driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
    lst1.append(subject)
lst2=[]
for i in range(10) :
    subject=driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[{i+1}]").text
    lst2.append(subject)
lst3=[]
for i in range(10) :
    subject=driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[2]").text
    lst3.append(subject)
lst4=[]
for i in range(10) :
    subject=driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]").text
    lst4.append(subject)

for i in range(10):
    print(lst1[i],lst2[i],lst3[i],lst4[i])