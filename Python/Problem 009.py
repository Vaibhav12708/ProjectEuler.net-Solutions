import math
z=0
for x in range(1,1000):
    for y in range(1,1000):
        a=x*x
        b=y*y
        c=a+b
        z=int(math.sqrt(a+b))
        if z*z==c:
            if x+y+z==1000:
                print(x*y*z)
