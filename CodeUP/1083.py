n = int(input())
arr = []

i = 1
while i<=n :
    arr.append(i)
    i += 1

for a in arr :
    if(a == 3 or a == 6 or a == 9) :
        print("X", end=" ")
    else :
        print(a, end=" ")
