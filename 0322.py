# 2023-03-22

'''
이것은
여러줄짜리
주석입니다'''
a='오늘은 파이썬 수업입니다.'
print('오늘은 파이썬 수업입니다.')
print('hello!!')
print(type('오늘은 파이썬 수업입니다.'))
print(2)
print(type(2))
print(5.5)
print(type(5.5))

print("Hello " + " Python")
print("213호 " *3)
print("hello " , " hi ", " 213")
print("hello " + " hello" , 213, " ", 1111)
print("hello" ,33)

print(1,2,-5,3,14,2.71828)
print("Hi","Python")
print("23000원은" ,' 5000원 ?개',' 1000원 ?개')
print("5000원",23000//5000,"개")
print("1000원 " , (23000%5000)//1000,"개")

print("3+8")
print(3+8)
print("3+8 = ",3+8)


# eval함수를 이용하여 계산 가능함. 
var ='3+8'
print(eval(var))
print(var)

print(1+62-3*52)
var2 = '256*553-152'
print(eval(var2))
print((162353290930//539253)+(162353290930%539253))

price=78000
a=78000//50000
b=78000%50000
c=b//10000
d=b%10000
if(d>5000):
        e=d//5000+1

print("78000원 내기")
print("50000원 짜리 지폐는 " , a ,"장 필요하고, 10000원짜리 지폐는 " ,c,"장 필요하다" )
print("그리고 5천원짜리 지폐는 " ,e, "장 필요하다")
print("거스름돈은 " ,50000*a+10000*c+5000*e-price,"원 이다.")