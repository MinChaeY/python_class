#5월 3일 시작

'''
함수이름 - addthree
기능 3을 더함
input : 숫자 1개ㅣ
output 숫자 한개,input 숫자에다가 3을 더한 것을 내보냄

def addthree(num):
    return num+3

result = addthree(100)
print(result)
#함수의 정의는 반드시 함수 호출 앞에 있어야 한다.

#function1 사라미이름 두개 를 입력받아 안녕 사람1,안녕 사람2 출력

def name(p1 = '민',p2='박'):
    print("사람 1 :",p1,"사람 2 : ",p2)

name('1','2')
name()
#function2 숫자 두개 입력받아 두개의 합 리턴

def sum(n1,n2):
    return n1+n2
a=sum(100,220)
print(a)

#sum2 인자는 몇개가 들어올지 모름, 모든 인자의 값의 합을 리턴하는 함수 작성

def sum2(*numbers):
    result2=0
    for num2 in numbers:
        result2 = result2+num2
    
    return result2

b= sum2(1,2,3,4,5,6,4,78,8)
print(b)

list1 =[1,2,3,4,5,6,7,8,9,10]
list2=[10,11,12,13,14,15,16,17]
print(sum2(*list1))
print(sum2(*list2))
'''
'''key value pair
cafe function
메뉴=가격
출력해주는 function을 만들자

def cafe(**keyvalue):
    #수행문 menu와 가격을 출력하라.
    for key in keyvalue:
        print(key,keyvalue[key])

cafe(아메=2000,라떼=3000,핫쵸코=5000)
print('====================================')
cafe(아메=2500,라떼=4000)
print('====================================')
cafe(아메=2000)
print('====================================')

menu = {"아메리카노":2000,"라떼":3000,"쉐이크":3000}
cafe(**menu)

#lambda function
#짧고 간결하게, 그리고 이름 짓기 싫어서 개발된 함수임. 수행문이 한줄로 간결하다. 일회용이댜.
print(addthree(100))

print((lambda num3 : num3+3)(100))

#1)숫자 입력받고 10을 곱해서 return - lambda로 작성
c=int(input("숫자를 입력하세요 >>"))
print((lambda num4 : num4*10)(c))

#위 람다 함수를 그냥 함수로도 작성
def mul1(c):
    return c*10

print(mul1(c))
#2) 숫자를 두개 입력.두개를 곱해서 return -lambda 로 작성
d=int(input("첫번째 숫자를 입력하세요 >"))
f= int(input("두번째 숫자를 입력하세요 >"))
print((lambda num5,num6: num5*num6)(d,f))
#위 람다 함수를 그냥 함수로 작성
def mul2(d,f):
    return d*f

print(mul2(d,f))'''
'''
#map, filter
map(function,list)
map(function,[1,2,3,4,5])
[function(1),function(2),function(3),...,function(5)]

print(list(map(addthree,[10,20,30,40,50])))

print(list(map(lambda x: x+3,[10,20,30,40,50])))
'''
'''
[addthree(10),addthree(20),addthree(30),addthree(40),addthree(50)]
[13,23,33,43,53]
input -function,list
output list하나

list3=[1,2,3,4,5,6]
#5배를 하고 10을 더해서 결과를 list 로 출력
def sumul(g):
    return g*5+10
print(list(map(sumul,list3)))

#lambda로
print(list(map(lambda x: x*5+10,list3)))
'''
#두개의 리스트를 하나씩 뽑아서 두개를 더해 하나의 리스트를 만들어라
lst10 =[10,20,30,40,50]
lst11=[1,2,3,4,5]

def mysum(n1,n2):
    return n1+n2
print(list(map(mysum,lst10,lst11)))

print(list(map(lambda n1,n2:n1+n2,lst10,lst11)))

#filter
#조건을 만족하면 결과에 포함, 만족하지 않으면 포함x
#map과 마찬가지로 리스트를 입력받아 그걸 매번 체크하여 포함시킴
#filter(function,list)
def positive(n):
    if n > 0:
        return True
    else:
        return False
print(list(filter(positive,[10,2,-3,5,-9])))

print(list(filter(lambda x: x>0,[10,2,-3,5,-9])))