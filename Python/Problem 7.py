def primenum(n):
    list1=[]
    temp=0
    for x in range(2,n+1):
        for y in range(2,n+1):
            if x%y==0:
                temp+=1
                if temp>1:
                    break      
        if temp==1:
            list1.append(x)
        temp=0 
    print(list1)
    print(list1[10000])

n=150000
primenum(n)
