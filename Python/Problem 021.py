def amicable(n):
    list1 = []
    list2 = []
    for x in range(1, n):
        if n % x == 0:
            list1.append(x)

    a = sum(list1)

    for x in range(1, a):
        if a % x == 0:
            list2.append(x)

    b = sum(list2)
    if n==a:
        return 0
    else:
        if n == b:
            return n
        else:
            return 0  

def main():
    sum1 = 0
    for x in range(1, 10000):
        value = amicable(x)
        sum1 += value
    print(sum1)

if __name__ == "__main__":
    main()
