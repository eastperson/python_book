a,b,c = map(int, input().split())
i = 1
while True :
    if(i == c) :
        print(a)
        break
    a *= b
    i += 1