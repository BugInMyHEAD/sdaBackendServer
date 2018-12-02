from konlpy.tag import Kkma
from konlpy.utils import pprint
from operator import eq
import os
kkma = Kkma()

#텍스트 파일 오픈
r = open('.\\log\\log.txt',mode='r',encoding='utf-8-sig')
line = r.read()

#샌드위치 이름
sandwich = ['로티세리','풀드포크','에그마요','비엠티','비엘티','미트볼','햄','참치','로스트','스테이크','터키','베지','랜치','데리야끼','클럽','멜트','스파이시','웨스턴']
sandlen = len(sandwich)
add = ['더블업','에그마요','오믈렛','아보카도','베이컨','페퍼로니','더블치즈']
addlen = len(add)
bread = ['오트','하티','위트','파마산','화이트','플랫','플렛']
breadlen = len(bread)
veg = ['양상추','토마토','오이','피망','양파','피클','올리브','할라피뇨']
veglen = len(veg)
cheese = ['아메리칸','슈레드']
cheeselen = len(cheese)
sauce = ['시저','랜치','렌치','마요네즈','어니언','머스터드','머스타드','칠리','사우스','디쉬','아일랜드','이탈리안','오일','식초','소금','후추','스모그']
saucelen = len(sauce)

#'''로 자름
splitline = line.split('\'\'\'')

#총 list의 길이 쓸데 없이 \n이 배열 원소에 포함되어있음
alllen = len(splitline)

cnt=0
#레시피가 아닌 원소들 정제
for i in range(0,alllen):
    recipe_cnt=0
    sandwich_name=''
    #레시피라고 부를 수 있는 트윗을 1차 거름
    for k in range(0,sandlen):
        #샌드위치 이름이 한 번이라도 언급되면 레시피
        if sandwich[k] in splitline[i]:
            if not eq(sandwich[k],sandwich_name):
                # 다른 레시피에 에그마요 추가한 경우
                if not eq(sandwich[k],'에그마요'):
                        recipe_cnt=recipe_cnt+1
                        sandwich_name=sandwich[k]
                        k=0
            
    #한 트윗에 두 개 이상의 레시피를 설명하는 경우 제거
    if recipe_cnt==1:
        cnt=cnt+1
    

#1차 거른 레시피를 저장할 배열 생성
recipe=[]
#배열 초기화
for i in range(0,cnt):
    recipe.append(0)

index=0
#걸러진 레시피를 배열에 저장
for i in range(0,alllen):
    recipe_cnt=0
    sandwich_name=''
    for k in range(0,sandlen):
        if sandwich[k] in splitline[i]:
            if not eq(sandwich[k],sandwich_name):
                # 다른 레시피에 에그마요 추가한 경우
                if not eq(sandwich[k],'에그마요'):
                        recipe_cnt=recipe_cnt+1
                        sandwich_name=sandwich[k]
                        k=0

    if recipe_cnt==1:
        recipe[index]=splitline[i]
        index=index+1

#걸러진 레시피만 들어있는 배열 프린트
#for i in range(0,cnt):
#    print(recipe[i])
#    print('---------------------------------------')
#print(cnt)

for j in range(0,cnt):
    splitrecipe=''
    splitrecipe=recipe[j].split()
    print(splitrecipe)
    recipelen = len(splitrecipe)

    #샌드위치 초기화
    recipe_sand = ''
    recipe_add=[]
    recipe_bread = ''
    recipe_veg = []
    recipe_cheese = []
    recipe_sauce = []

    for i in range(0,recipelen):
        #한 개 찾으면 바로 나옴
        if eq(recipe_sand,''):
            for k in range(0,sandlen):
                #어떤 샌드위치인지 체크
                if sandwich[k] in splitrecipe[i]:      
                    #만약 로스트라면
                    if eq(sandwich[k],'로스트'):
                        #같은 문자열에 치킨이 있다면 로스트 치킨
                        if '치킨' in splitrecipe[i]:
                            recipe_sand = '로스트치킨'
                            break
                        #같은 문자열에 비프가 있다면 로스트 비프
                        elif '비프' in splitrecipe[i]:
                            recipe_sand = '로스트비프'
                            break
                        #다음 문자열에 치킨이 있다면 로스트 치킨
                        elif '치킨' in splitrecipe[i+1]:
                            recipe_sand = '로스트치킨'
                            break
                        #다음 문자열에 비프이 있다면 로스트 비프
                        elif '비프' in splitrecipe[i+1]:
                            recipe_sand = '로스트비프'
                            break
                    if eq(sandwich[k],'터키'):
                        #만약 터키라면 일단 터키 넣어줌
                        recipe_sand = '터키'
                        #같은 문자열에 베이컨도 있다면 일단 터키베이컨 넣어줌
                        if '베이컨' in splitrecipe[i]:
                            recipe_sand = '터키베이컨'
                            #같은 문자열에 아보카도도 있다면 터베아 
                            if '아보카도' in splitrecipe[i]:
                                recipe_sand = '터키베이컨아보카도'
                                break
                            #다음 문자열에 아보카도도 있다면 터베아
                            elif '아보카도' in splitrecipe[i+1]:
                                recipe_sand = '터키베이컨아보카도'
                                break
                            #아보카도 없다면 터키베이컨
                            break
                        #다음 문자열에 베이컨도 있다면 일단 터키베이컨 넣어줌
                        elif '베이컨' in splitrecipe[i+1]:
                            recipe_sand = '터키베이컨'
                            #다음 문자열에 아보카도도 있다면 터베아
                            if '아보카도' in splitrecipe[i+1]:
                                recipe_sand = '터키베이컨아보카도'
                                break
                            #그다음 문자열에 아보카도도 있다면 터베아
                            elif '아보카도' in splitrecipe[i+2]:
                                recipe_sand = '터키베이컨아보카도'
                                break
                            #아니라면 터키베이컨
                            break
                        #아니라면 터키
                        break
                    #그 외 모든 1대1 대응하는 샌드위치들
                    if sandwich[k] in splitrecipe[i]:
                            recipe_sand = sandwich[k]
                            break
    #추가 찾기
    for i in range(0,recipelen):
        for k in range(0,addlen):
            if add[k] in splitrecipe[i]:
                # 에그마요, 아보카도, 베이컨 예외 설정
                if eq(add[k],'에그마요') or eq(add[k],'아보카도') or eq(add[k],'베이컨'):
                    try:
                        if '추가' in splitrecipe[i] or '추가' in splitrecipe[i+1]:
                            recipe_add.append(add[k])
                    except:
                        recipe_add.append(add[k])
                else:
                    recipe_add.append(add[k])

    #빵 찾기
    for i in range(0,recipelen):
        if eq(recipe_bread,''):
            for k in range(0,breadlen):
                if bread[k] in splitrecipe[i]:
                    recipe_bread = bread[k]
                    break

    #채소 찾기
    for i in range(0,recipelen):
        for k in range(0,veglen):
            if veg[k] in splitrecipe[i]:
                # 올리브 예외 설정
                if eq(veg[k],'올리브'):
                    try:
                        if not '오일' in splitrecipe[i] or '오일' in splitrecipe[i+1]:
                            if '빼' in splitrecipe[i] or '빼' in splitrecipe[i+1]:
                                 pass
                            else:
                               recipe_veg.append(veg[k])
                    except: 
                            recipe_veg.append(veg[k])
                else:
                    try:
                         if '빼' in splitrecipe[i] or '빼' in splitrecipe[i+1]:
                             pass
                         else:
                            recipe_veg.append(veg[k])
                    except:
                        recipe_veg.append(veg[k])

    #치즈 찾기
    for i in range(0,recipelen):
        for k in range(0,cheeselen):
            if cheese[k] in splitrecipe[i]:
                recipe_cheese.append(cheese[k])

    #소스 찾기
    for i in range(0,recipelen):
        for k in range(0,saucelen):
            if sauce[k] in splitrecipe[i]:
                # 랜치 드레싱과 베이컨 랜치 구분
                if eq(sauce[k],'랜치') or eq(sauce[k],'렌치'):
                    if not '베이컨' in splitrecipe[i-1] or '베이컨' in splitrecipe[i]:
                        recipe_sauce.append(sauce[k])
                #이탈리안 비엠티, 스파이시 이탈리안과 이탈리안 드레싱을 구분
                elif eq(sauce[k],'이탈리안'):
                    if not '스파이시' in splitrecipe[i-1] or '스파이시' in splitrecipe[i] or '비엠티' in splitrecipe[i] or '비엠티' in splitrecipe[i+1]:
                        recipe_sauce.append(sauce[k])
                #머스타드와 허니 머스타드 구분
                elif eq(sauce[k],'머스터드') or eq(sauce[k],'머스타드'):
                    if '허니' in splitrecipe[i-1] or '허니' in splitrecipe[i]:
                        recipe_sauce.append('허니머스터드')
                    else:
                        recipe_sauce.append('머스타드')
                #핫 칠리와 스위트 칠리 구분
                elif eq(sauce[k],'칠리'):
                    if '핫' in splitrecipe[i-1] or '핫' in splitrecipe[i]:
                        recipe_sauce.append('핫칠리')
                    else:
                        recipe_sauce.append('스위트칠리')
                #그 외 문제 없는 것들
                else:
                    recipe_sauce.append(sauce[k])

    #샌드위치 이름 출력
    print('샌드위치 : ',recipe_sand)
    print('추가 : ',recipe_add)
    print('빵 : ',recipe_bread)
    print('야채 : ',recipe_veg)
    print('치즈 : ',recipe_cheese)
    print('소스 : ',recipe_sauce)
    print('---------------------------------')

print(cnt)
r.close()
os.system("pause")