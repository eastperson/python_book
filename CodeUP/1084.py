r,g,b = map(int, input().split())
sum = 0
for x in range(0, r) :
    for y in range(0, g) :
        for z in range(0, b) :
            print(x,y,z)
            sum += 1
print(sum)
