#dictionary

#key -value

#carDict={key1:value1,key2:value2,key3:value3}
'''
carDict={'j101':('2020','1800'),'k102':('2022','1500'),'b203':('2023','2500'),'b105':('2022','4500')}

print(carDict.keys())#dict_keys(['j101', 'k102', 'b203', 'b105']) 키만 출력
print(carDict.values())#dict_values([('2020', '1800'), ('2022', '1500'), ('2023', '2500'), ('2022', '4500')]) value만 출력
print(carDict.items())#dict_items([('j101', ('2020', '1800')), ('k102', ('2022', '1500')), ('b203', ('2023', '2500')), ('b105', ('2022', '4500'))]) 아이템들 그대로 출력

for i,k in carDict.items():
    print(i,k)

print('=========================================================')

for item in carDict.items():
    print(item[0],item[1])

print('=========================================================')

for key in carDict.keys():
    print(key,carDict[key])

print('=========================================================')

yearList=[]

for value in carDict.values():
    yearList.append(int(value[0]))

print(yearList)

year = int(input("생산년도를 입력하시오>>"))
print(year,"년도에 생산된 자동차는",yearList.count(year))

members={'홍':'111','박':'222','정':'333'}
members['최']='555'
members.update({'강':'666'})
members['김']='777'
members.update({'최':'888'})
print(members)

# 7.3 zip

#list,tuple,문자열 여러개를 순서대로 묶어주는것

l1=[1,2,3,4,5]
l2=['a','b','c','d','e']

a=list(zip(l1,l2))
print(a)

sport=['축구','야구','농구','배구']
num=[11,9,5,6]

b=dict(zip(sport,num))'''
'''zip으로 묶고 input 으로 종목이름을 입력받아서 선수 수를 for문을 이용해서 출력하고 quit을 만나면 종료한다.
   다른동목이 들어오면 "몰라요" 다시 입력받기
   continue,break 활용하기

while 1 :
    s=input("종목 이름을 입력하십시오>>")
    if s=="quit":
        print("quit 을 입력하였습니다. 종료합니다.")
        break
    if s in b.keys():
        print("인원은 " ,b[s] , "입니다")
    else :
        print("존재하지 않는 종목입니다. 다시 입력하여 주십시오")
        continue


filter 와 lambda를 사용하여 리스트 [1,-2,3,-5,8,-3]에서 음수를 모두 제거해보자

map,filter
map(함수,input list )=>리스트
map(addone,[0,1,2]) => [addone(0),addone(1),addone(2)]
filter(func,[10,20,30])=>[10,30]

def positive1(x):
    return x>0

print(list(filter(positive1, [1,-2,3,-5,8,-3])))

print(list(filter(lambda x : x>0, [1,-2,3,-5,8,-3])))

#리스트 두개를 받음
#각각 첫번째는 첫번째끼리 두번째는 두번째끼리 더하는 함수를 만들어라
#lambda 사용

list1=[10,20,30,40,50]
list2=[100,200,300,400,500]

print(list(map(lambda x:x[0]+x[1],list(zip(list1,list2)))))
'''

#9 module

import random
#이부분 중요
#__name__ => 여러개의 파이썬 코드가 존재할 때 실제로 메인이 되는 파이썬 코드