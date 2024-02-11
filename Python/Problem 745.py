list1=[]
x=100000000000000
for i in range(1,x):
    list1.append(i*i)
    
sum1=0
for i in range(1,x+1):
    max=0
    for j in range(0,len(list1)):
        if i%list1[j]==0:
            max=list1[j]
    sum1+=max
print(sum1)
