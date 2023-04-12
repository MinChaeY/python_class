#0412 시작
# 0412
# 자료형 - 리스트, 튜플, 딕셔너리, 집합
# "김밥", "떡볶이", "돈까스"

'''
# 리스트
["김밥","떡볶이","돈까스"]

#튜플
("김밥","떡볶이","돈까스")

딕셔너리 - 사전, apple - 동그란 빨간 과일
{k1:v1, k2:v2}
adress = {"홍길동":"구로구", "김길동":"부천", "박길동":"인천"}

<json 형식>
key:value
"국어":100
"사회:80
'''

#1. 빈 리스트를 만들어서, 하나씩 원소를 추가하는 방식
lst = []
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
lst.append("탕수육") #append라는 메소드를 이용하여 리스트에 추가함. append:요소추가 메소드
print(lst)
lst.append("파스타")
print(lst)
lst.insert(0,"고구마피자") #리스트에 요소 삽입 insert(a,b)는 리스트의 a번째 위치에 b를 삽입.
print(lst)
lst.insert(0,"서브웨이")
print(lst)
print("리스트에서 3번째에 있는 값을 출력합니다: ", lst[2])
#lst.append("해장국","감자탕") #오류 발생, 한개씩만 더하기 가능

#점심메뉴 출력하기
for i in range(len(lst)):
           print(lst[i])
#점심메뉴 출력하기2
for item in lst :
        print(item)

print(lst)
lst.count("탕수육") #리스트에 탕수육이라는 단어가 많을시 탕수육이 몇 번 나왔는지 알려줌

print(lst)
print('lst.count("탕수육")',lst.count("탕수육"))

#slicing
'''
lst[start:end:step] #-> 전체 출력
lst[0,10,1] : 0~(10-1),step수만큼 뛰어 넘어라.
'''
print(lst[::]) #전체 출력
print(lst[0:len(lst):1])
print(lst[0:8:2])
print(lst[3:7:1])
print(lst[::-1])
print(lst[0:6:3])

lst.append("김밥")
lst.append("라볶이")
lst.append("김밥")
print(lst)
lst.remove("김밥")
print(lst)

#lst.remove("커피") #커피가 리스트 안에 존재하지 않아 오류발생함
lst.append("커피")
item1="커피"
if item1 in lst:
        lst.remove(item1)
        print("커피 존재함",lst)
else:
        print("커피 존재 안함",lst)

print(lst)
print("lst.pop():",lst.pop())
print(lst)

print("lst.pop():",lst.pop(0))
print(lst)

dessert =["케잌","커피","우유","와플"]
print(dessert)
lst.extend(dessert)

print(lst)

x="15"
print(type(x))
#x를 숫자로 변환. +1
print(int(x)+1)
print(type(x)) 

#sort vs sorted
l1=["orange","apple","mango","kiwi","banana"]
print(l1)
print(sorted(l1))
print(l1)

l1.reverse()
print(l1)

l1.clear()
print(l1)

del l1
print(l1) #위에서 l1을 삭제했으므로 l1이 정의되지 않아 오류 발생함