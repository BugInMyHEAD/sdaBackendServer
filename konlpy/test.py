from ckonlpy.tag import Twitter
from operator import eq

# twitter : 사용자 정의 사전 사용
twitter = Twitter()
# log 파일 경로
path='.\\log\\log.txt'

#텍스트 파일 읽기
with open(path,mode='r', encoding='utf-8-sig') as r:
    line = r.read()

#샌드위치 이름 모두 대응중
menu = ['로티세리','풀드포크','에그마요','비엠티','비엘티','미트볼','햄','참치','로스트','로스트치킨','로스트비프','스테이크','터키','베지','랜치','데리야끼','클럽','멜트','스파이시','웨스턴']
bread = ['허니오트', '하티', '위트', '화이트', '플랫', '파마산', '오레가노']
vegetable = ['양상추', '토마토', '오이', '피망', '양파', '피클', '올리브', '할라피뇨', '아보카도']
cheese = ['아메리칸', '슈레드']
souce = ['리치시저', '랜치드레싱', '마요네즈', '스위트어니언', '허니머스터드', '스위트칠리', '핫칠리', '사우스웨스트', '머스타드', '홀스래디쉬', '사우전아일랜드', '이탈리안드레싱', '올리브오일', '레드와인식초', '소금', '후추', '스모크바비큐']
negative = ['빼']

# 사용자 정의 사전 생성
userDict=[]
userDict.extend(menu)
userDict.extend(bread)
userDict.extend(vegetable)
userDict.extend(cheese)
userDict.extend(souce)
userDict.extend(negative)
for e in userDict:
    twitter.add_dictionary(e, 'Noun')

#'''로 자름
splitline = line.split('\'\'\'')
for element in splitline:
    if element == '' or element == '\n':
        del splitline[splitline.index(element)]

print('수집한 트윗 : ', len(splitline))

twits=[]
#레시피가 아닌 원소들 정제
for twit in splitline:
    recipe_cnt=0
    recipe_egg=0
    twit_split = twitter.nouns(twit)

    # 레시피라고 부를 수 있는 트윗을 1차 거름
    for word in twit_split:
        # 트윗에서 레시피 언급
        if word in menu:
            # 에그마요를 언급
            if eq(word,'에그마요'):
                recipe_egg+=1
            recipe_cnt+=1
        
    # 1차 거른 트윗들 리스트에 추가
    if recipe_cnt==1 or (recipe_cnt==2 and recipe_egg==1):
        twits.append(twit)

print('정제된 트윗 : ', len(twits))

recipes=[]
for twit in twits:
    recipe=[]
    recipe_egg = 0
    twit_split = twitter.nouns(twit)

    for word in twit_split:
        if word in userDict:
            recipe.append(word)

    # 터키
    if '터키' in recipe:
        if '터키베이컨' in twit or '터키 베이컨' in twit:
            recipe[recipe.index('터키')] = '터키베이컨'
        elif '터키베이컨아보카도' in twit or '터키 베이컨아보카도' in twit or '터키베이컨 아보카도' in twit or '터키 베이컨 아보카도' in twit:
            recipe[recipe.index('터키')] = '터키베이컨아보카도'
    # 위트
    if '위트' in recipe:
        if '스위트어니언' in twit or '스위트 어니언' in twit:
            recipe[recipe.index('위트')] = '스위트어니언'
        elif '스위트칠리' in twit or '스위트 칠리' in twit:
            recipe[recipe.index('위트')] = '스위트칠리'
    # 랜치 (에그마요가 메뉴, 랜치가 메뉴)
    if '랜치' in recipe:
        flag=0
        for word in menu:
            if not eq('랜치',word) and word in recipe:
                recipe[recipe.index('랜치')] = '랜치드레싱'
                break
    # 올리브??
    if '올리브' in recipe:
        if '올리브오일' in twit or '올리브 오일' in twit:
            recipe[recipe.index('올리브')] = '올리브오일'
    # 로스트
    if '로스트' in recipe:
        if '로스트비프' in twit or '로스트 비프' in twit:
            recipe[recipe.index('로스트')] = '로스트비프'
        elif '로스트치킨' in twit or '로스트 치킨' in twit:
            recipe[recipe.index('로스트')] = '로스트치킨'

    # 부정적인것 ??
    if '빼' in recipe:
        for word in vegetable:
            if word in recipe:
                del recipe[recipe.index(word)]
        del recipe[recipe.index('빼')]


    recipes.append(recipe)
    print('ㅡ'*40)
    print(twit+'\n\n', recipe)

# for l in recipes:
#     print(l)
    

print('최종 레시피 개수 : ' + str(len(recipes)))