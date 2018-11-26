from konlpy.tag import Okt
import re

# 경로
path_f=".\\konlpy\\log.txt"

# 패턴
p=re.compile('^\'\'\'.*\'\'\'$')
p_s=re.compile('^\'\'\'')
p_e=re.compile('\'\'\'$')

# 파일 읽기
with open(path_f, mode='r', encoding='utf-8-sig') as f:
    text=f.readlines()

# 데이터 분류
data=[ ]
for line in text:
    if p.search(line):
        line=re.sub(p_s,'',line,0)
        data.append(re.sub(p_e,'',line,0))
        continue
    
    if p_s.search(line):
        temp=''
        line=re.sub(p_s,'',line,0)
    
    temp+=line
    
    if p_e.search(line):
        temp=re.sub(p_e,'', temp, 0)
        data.append(temp)

