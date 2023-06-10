import math
n=int(input())
square=pow(n,2)
mod=square%pow(10,len(str(n)))
if mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")