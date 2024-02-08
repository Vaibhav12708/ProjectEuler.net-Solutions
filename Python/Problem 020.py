n=100
sum1=1
sum2=0
for i in range(1,n+1):
    sum1=sum1*i
x=str(sum1)
for i in range(0,len(x)):
    sum2=sum2+int(x[i])
print(sum2)
