"""import random

from random import randint  #random안에 있는 randint라는 모듈을 사용한다는 뜻
print(randint(0,10))"""

#놀이동산 놀이기구 탑승 문제
# 총 정원 4명
#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 ㅌ탈 수 있음
#사람들에게 키를 물어보고 탑승시키시오
#150이상 4명 되면 놀이기구 시작
count=0
member=0
while True:
    height = int(input("키가 몇이신가요?"))
    if height>=150:
        count+=1
        print("현재 정원 수는 ",count,"입니다")
        continue
    elif height <150:
        print("신장 제한에 걸립니다")
    elif count==4:
        print("정원이 다 찼습니다. 놀이기구 출발합니다.")
        break