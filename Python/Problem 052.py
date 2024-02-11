for n in range(100000,1000000):
    a1=sorted(str(n))
    a2=sorted(str(2*n))
    a3=sorted(str(3*n))
    a4=sorted(str(4*n))
    a5=sorted(str(5*n))
    a6=sorted(str(6*n))
    if a2==a3 and a2==a4 and a2==a5 and a2==a6:
        print(n)
