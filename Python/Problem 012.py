def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            if len(divisors)==374:
                print(n,end=' ')
                break
    return divisors


temp=0
for x in range(0,80000000):
    temp+=x
    find_divisors(temp)

