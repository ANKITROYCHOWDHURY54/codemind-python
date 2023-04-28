import math
a=int(input())
sq=math.isqrt(a)
if a%sq==0:
    print("True")
else:
    print("False")