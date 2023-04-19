#0419

l1=[1,2,3,4,5]
#tuple
t1=(1,2,3,4,5,2,2,2,2,2,2,2,2)
print(l1)
print(t1)  #li은 리스트 t1은 튜플이다. 튜플은 수정이 불가하며 수정할 때는 리스트로 변경해서 수정한다.
print(t1.count(2))
print(t1.index(2))

#커피숍 프로그램
menu=("아메","라떼","유자차")
#아이스티를 추가하자
menu1 = list(menu)
menu1.append("아이스티")
menu=tuple(menu1)
print(menu)

lst=[10,20,30,44,5,6,1,1]
#lst.sort() ->작동되지 않음
t3=1074,205,3,40,50
print("sorted(t3) : ",sorted(t3))


#dictionary

#d1={k1:v1,k2:v2,k3:v3}  #내부 키 중복 불가
d1={}
d2=dict()
#사전에 값을 추가하자
#1) 추가방법 1
student={}
student[101]="홍"
student[102]='김'
student[103]='박'
print(student)

lec={}
lec['강좌명']='파이썬'
lec['개설년도']=2023
lec['수강생']=['홍','김','박','고']
lec['인원']=35
print(lec)

lec['인원']=20
print(lec)
lec.update({'인원':15})
print(lec)

lec.update({'강의실':213,"교수":'이희진'})
print(lec)


#월
month={ 'a':"1월",'b':"2월",'c':"3월",'d':"4월",'e':"5월",'f':"6월",'g':"7월",'h':"8월",'i':"9월",'j':"10월",'k':"11월",'l':"12월"}
'''for key in range(1,13):
    print(month[key])
for key in 1,2,3,4,5,6,7,8,9,10,11,12:
    print(month[key])
'''
print(month.keys())
print(month.values())
print(month.items())


print("#3")
#month.key()
for k in month.keys() :
    #month[key] => value
    print(month[k])

print("#4")
for v  in month.values():
    print(v)

print("#5")

for item in month.items():
    print(item)

print("#6")
for item in month.items():
    print("key : ", item[0])
    print("value : ", item[1])
    print("    ")

for hoho in month:
    print(hoho)
'''
print(month.get("a"))
print(month.get("k1"))  #get에서는 해당 값이 존재하지 않을 경우 none 결과를 출력하지만 month[]형태에서는 오류 메세지를 출력한다. 그러므로 get을 쓰는 편이 낫다.
print(month["a"])
print(month['k1'])

#dictionary 삭제,
month.pop()
month.popitem()'''

print(month)
print(month.pop("a")) #지정한 값 삭제
print(month)
print(month.popitem())  #마지막 값 삭제
print(month)