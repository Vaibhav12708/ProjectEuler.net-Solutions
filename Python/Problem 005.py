c=0
for x in range(200000000,232792562):  
    for y in range(1,21):
        if x%y==0:
            c+=1
            if c== 20:
                print(x)
        else:
            c=0
