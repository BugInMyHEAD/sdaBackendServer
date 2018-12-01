from konlpy.tag import Okt
import re

# 경로
path_f=".\\log\\log.txt"

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
        line=re.sub(p_s, '', line)
        data.append(re.sub(p_e, '', line))
        continue
    
    if p_s.search(line):
        temp=''
        line=re.sub(p_s, '', line)
    
    temp+=line
    
    if p_e.search(line):
        temp=re.sub(p_e, '', temp)
        data.append(temp)

if __name__ == '__main__':
    with open("./konlpy/readLogResult.txt", mode='w', encoding='utf-8') as f:
        for twit in data:
            f.write(',..,')
            f.write(twit)
