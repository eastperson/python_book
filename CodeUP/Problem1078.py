str = input()
str.lower()
i = 0
while True :
    if(str[i] == 'q') :
        print("q")
        break
    if(str[i] == ' ') :
        i += 1
        continue
    print(str[i])
    i += 1