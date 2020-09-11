r, g, b = input().split()
w = int(r)
h = int(g)
b = int(b)

result = round(w*h*b/8/1024/1024*100)/100
print('%.2f' % result, end=" MB")