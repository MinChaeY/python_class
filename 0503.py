#5월 3일 시작

'''
함수이름 - addthree
기능 3을 더함
input : 숫자 1개ㅣ
output 숫자 한개\\,input 숫자에다가 3을 더한 것을 내보냄
'''
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

'''key value pair
cafe function
메뉴=가격
출력해주는 function을 만들자'''

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

print(mul2(d,f))


