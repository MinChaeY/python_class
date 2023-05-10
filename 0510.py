#모듈 0510

import random

 #10~100까지의 숫자 중 랜덤 한개
print("random.randint(10,100) : ",random.randint(10,100))

import math as m #math를 m으로 줄여쓴다.
#괄호 안의 숫자를 전부 더한다
m.fsum([2,2,2,2,2,2,2])
print("math.fsum([2,2,2,2,2,2,2]) : ",m.fsum([2,2,2,2,2,2,2]))

m.pow(10,3) #10**3
print("m.pow(10,3) : ",m.pow(10,3))

from math import pow as p #math 안에 있는 pow 함수를 p로 줄여쓴다.
print(p(10,3))

import ya
print("============================")


ya.helloya()

print("__name in ya.py",__name__)