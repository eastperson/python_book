a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
i = 1
while True :
    if(i == d) :
        print(a)
        break
    a *= b
    a += c
    i += 1