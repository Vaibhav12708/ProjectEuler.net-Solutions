n=5
diagnol=[[21,22,23,24,25],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]]
sum1=0
for i in range(0,n):
    sum1+=diagnol[i][i]
print(sum1)
sum2=0
x=n
for i in range(0,n):
    sum2+=diagnol[i][x-1]
    x=x-1
print(sum2)
print(sum1+sum2-diagnol[(n-1)//2][(n-1)//2])
