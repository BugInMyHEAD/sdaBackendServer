from bs4 import BeautifulSoup
from selenium import webdriver 
import time
import datetime as dt
import re
import platform
import sys

# 경로
sysname = platform.system()
if sysname == 'Linux':
    path_d="./crawling/chromedriver"
elif sysname == 'Windows':
    path_d='.\\crawling\\chromedriver.exe'
else:
    print("Your system doesn't seem to be Linux or Windows.")
    sys.exit()
path_f="./log/log.txt"

# 브라우저 옵션
options=webdriver.ChromeOptions()
options.add_argument('--headless')

# chrome을 통해 크롤링
browser=webdriver.Chrome(executable_path=path_d, options=options)

# 시간
startdate=dt.date(year=2018,month=11,day=20) 
untildate=dt.date(year=2018,month=11,day=21) 
enddate=dt.date(year=2018,month=11,day=30) 

# 파일 생성
f = open(path_f,mode='w', encoding='utf8')

while not enddate==startdate: 
    url='https://twitter.com/search?q=서브웨이레시피%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=eg' 
    browser.get(url)

    # 스크롤을 내림으로서 트윗을 업데이트함
    while True:
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 스크롤을 내려도 업데이트가 되지 않아 올렸다가 다시내림
        browser.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        newHeight = browser.execute_script("return document.body.scrollHeight") 
        if newHeight == lastHeight:
            break

    html = browser.page_source
    soup=BeautifulSoup(html,'html.parser') 
    tweets=soup.find_all("p", {"class": "TweetTextSize"})

    # write
    for element in tweets:
        # 태그 제거
        element=re.sub('<.+?>', '', str(element), 0).strip()
        try:
            f.write('\'\'\'' + element + '\'\'\'\n')
        except UnicodeEncodeError:
            element.encode("utf8")
            f.write('\'\'\'' + element + '\'\'\'\n')
    
    # 시간 계산
    startdate=untildate 
    untildate+=dt.timedelta(days=1)

f.close()
