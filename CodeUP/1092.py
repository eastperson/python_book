a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min = min(a,b,c)
day = min
while not((day % a == 0) and (day % b ==0) and (day % c == 0)) :
    day += min
print(day)