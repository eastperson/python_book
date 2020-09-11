radius = int(input("반지름을 입력하시오 : "))
import math
area = radius**2*math.pi
print("반지름이",radius,"인 원의 넓이 = ",math.floor(area*10**4)/10**4)