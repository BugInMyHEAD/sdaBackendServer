from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary 
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities 
import time 
from selenium.webdriver.common.keys import Keys 
import datetime as dt 

# firefox를 통해서 크롤링
binary=FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe') 
browser=webdriver.Firefox(executable_path='D:\\inu\\Database Project\\geckodriver.exe',firefox_binary=binary) 

# 시간
startdate=dt.date(year=2018,month=9,day=1) 
untildate=dt.date(year=2018,month=9,day=2) 
enddate=dt.date(year=2018,month=11,day=5) 

# 파일 생성
f = open(".\\log.txt",'w')
totalfreq=[]
while not enddate==startdate: 
    url='https://twitter.com/search?q=서브웨이레시피%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=eg' 
    browser.get(url) 
    html = browser.page_source 
    soup=BeautifulSoup(html,'html.parser') 
     
    lastHeight = browser.execute_script("return document.body.scrollHeight") 

    while True: 
            dailyfreq={'Date':startdate} 

            #i=0 i는 페이지수 
            wordfreq=0 
            tweets=soup.find_all("p", {"class": "TweetTextSize"})
            wordfreq+=len(tweets)

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            time.sleep(1) 
        
            newHeight = browser.execute_script("return document.body.scrollHeight") 
            # print(tweets) #프린트
            f.write(str(tweets)+'\n')
            if newHeight != lastHeight: 
                html = browser.page_source 
                soup=BeautifulSoup(html,'html.parser') 
                tweets=soup.find_all("p", {"class": "TweetTextSize"}) 
                wordfreq=len(tweets) 
            else: 
                dailyfreq['Frequency']=wordfreq 
                wordfreq=0 
                totalfreq.append(dailyfreq) 
                startdate=untildate 
                untildate+=dt.timedelta(days=1) 
                dailyfreq={} 
                break 
            #i+=1 
            lastHeight = newHeight
f.close()