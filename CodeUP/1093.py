import math
from random import random

dic = {}
for a in range(1,24) :
    dic[a] = 0
num = int(input())
list = []
list.append(int(input().split()))

i = 0
while True :
    i+=1
    dic[i] += 1
    if(i == num) :
        break
i = 1
while True :
    print(dic[i], end=" ")
    if(len(dic)  == i) :
        break
    i += 1
