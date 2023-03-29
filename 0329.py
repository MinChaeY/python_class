'''age = input("나이는? ")
print("제 나이는 ", age , "입니다.")
print("아버지의 나이는 ",int(age)+30,"입니다.")

planet = input("원하는 행성은?")
strRadius = input(planet +'반지름은?')
radius = int(strRadius)

length=3*3.14*radius
print(planet,'반지름: ',radius)
print(planet,'둘레길이',length)'''

a="Python"
print(a[0],a[1],"...",a[5])
print("python"[0],"....","python"[1],"....","python"[5])
print("동양미래대학교"[0])
print(len(a))
#a[:]은 문자열에서 특정 구역의 문자열만을 출력한다.
print(a[2:5])
school="동양미래대학교-컴퓨터소프트웨어공학과"
print("school[0:len(school):2] : ",school[0:len(school):2]) #동미대교컴터프웨공과
print("school[8:len(school):2]  : ",school[8:len(school):2])  #컴터프웨공과
print("school[8:len(school)] : ",school[8:len(school)]) #컴퓨터소프트웨어공학과
print("school[:15:4]  : ",school[:15:4]) #동양미래대학교-컴퓨터소프트웨어 4칸씩 뛰기
print('동양미래대학교'[-1:-7:-1])

print("hello \n world")
print("hello \t world")
print("hello\b world")
print("hello \v world")

str_a="하하하"

print(type(str_a))
print(str_a.replace("하","호")) #하를 호로 대체
str_b = str_a.replace("하","호")
print (str_b)
str_c ="안녕하세요. 파이썬 수업입니다. 파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬."
print(str_c.replace("파이썬","자바",5))

#6자리 실수를 입력받는다.
#출력: 실수의 각 자리의 합을 출력한다. 2+2+2+7+8+8 => ??
#input(),int(),str.replace()
num=input("실수 를 입력하시오")
num=num.replace(".","")
print("sum : ",int(num[0])+int(num[1])+int(num[2])+int(num[3])+int(num[4])+int(num[5]))