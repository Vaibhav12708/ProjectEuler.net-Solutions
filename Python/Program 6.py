def sum_of_square(n):
    sum1=0
    for x in range(1,n+1):
        y=x*x
        sum1=sum1+y
    return sum1

def square_of_sum(n):
    sum2=0
    for x in range(1,n+1):
        sum2=sum2+x
    return sum2*sum2

n=int(input())
print(sum_of_square(n))
print(square_of_sum(n))
print(square_of_sum(n)-sum_of_square(n))
