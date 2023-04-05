# 0405 파이썬 5주차 수업
"""
#문자열

str ="파이썬수업 씨수업 자바수업 파이썬수업 파이썬수업 "
str2="파이썬수업,씨수업,자바수업,이썬수업,파이썬수업"
#replace
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))


#format
#3+4=7
print(3,"+",4,"=",7)
f1="{} + {} = {}".format(3,4,3+4)
f2="{0} +{1} + ={2},{2},{2},{2}".format(3,4,3+4)
f3="{0:d} +{1:f} = {2:f},{2},{2},{2}".format(3,4.0,3+4)
f4="{0:10d} +{1:10.3f} = {2:f}".format(3,4.0,3+4.0)
print(f3)
print(f4)



#split
print(str.split())
print(str2.split())
print(str2.split(","))
print(str2.split("업"))

#find, index
print("find : ",str.find("씨"),"index : ",str.index("씨"))
print(str.find("AI"))  #없을경우 -1 출력
print(str.index("AI"))  # 없을경우 error 냄

#bool

print(type(True),type(False))
a="Hello"
print(bool("Hello"),bool("hi"),bool(3),bool(1.2))
print(bool(""),bool(0))
print(int(True),int(False),str(True))


#조건문
#기본 형태
if 조건1 :
    실행문1  #참
else :
    실행문2  #거짓

#오전/오후
h=20
if h<12 :
    #h가 12보다 작을때
    print("오전 ", h,"가 12보다 작다.")
elif h<18 :
    print("오후 ",h,"가 12보다 크고 18보다 작아요")
else :
    #실행문 2
    #h가 12보다 크다.
    print("오후 ", h,"는 18보다 크다.")



lunch =input("밥 먹을래? ")

if lunch=="yes" :
    print("밥을 먹고 싶군요 ")
    cafeteria =input("학식?")
    if cafeteria =="yes" : 
        print("8호관 3층으로 가자")

    else :
        print("다른걸 드시는군요")
        subway =input("서브웨이? ")
        if subway =="yes":
            print("8호관 1층으로 가자")

        else : 
            print("오늘 점심은 먹지 않는걸로")
else:            
    print("오늘 점심은 거르는 걸로")



# for,while
# 반복문
# in range
for i in 1,2,3,4,5,6 :
        print("i :",i)

for i in range(2,21,2):
        print("i : ",i)

#1~10까지 합 구하기
sum =0
for i in range(0,11,1):
        sum = i+sum
print(sum)

sum=0
for i in 1,2,3,4,5,6,7,8,9,10 :
        sum +=i
        print(i , "번째 loop입니다. sum은 ",sum," 입니다")

print("range를 사용하였음.")
sum=0
for i in range(1,11,1) :
        sum+=i
        print(i , "번째 loop입니다. sum은 ",sum," 입니다")
else:
        print("else안의 문구 :for 문 종료됨")
print("완전바깥. else밖의 문구 : for 문 종료됨")


#print(i,end='')
#while
while 조건 :
    수행문1
else:
    수행문2"""

#sum,0부터 10까지의 숫자를 찍음
# sum 을 구할것임
sum=0
n=0
while n<11:
    sum+=n
    #print("n: ",n)
    print(n,"번째 sum : ",sum)
    n=n+1
print("while 밖에서 sum의 값 : 0",sum  )

while 0:
    print("실행이 되지 않음")
print("while 0 다음 줄입니다.")
while True :
    print("무한루프")
while False:
    print("실행이 되지 않음")