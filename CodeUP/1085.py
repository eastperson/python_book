num = int(input(), 16)
for a in range(1,16) :
    b = int(a)
    c = num*b
    print(str(format(num,'X'))+"*"+str(format(b,'X'))+"="+str(format(c,'X')))