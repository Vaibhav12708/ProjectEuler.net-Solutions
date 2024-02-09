import math
math=[]
for x in range(2,101):
    for y in range(2,101):
        a=pow(x,y)
        math.append(a)

math1=list(set(math))
math1.sort()
print(math1)
print(len(math1))
