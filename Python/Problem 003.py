##static code
#Example 1

def largest_prime_factor(number):
    factor = 2
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
    if number > 1:
        return number
    return factor

number = 600851475143
largest_prime = largest_prime_factor(number)
print(largest_prime)





## dynamic code
#Example 2

import math
n=int(input())
list1=[]
while n%2==0:
	list1.append(2)
	n=n/2
for i in range(3,int(math.sqrt(n))+1,2):
	while n%i==0:
		list1.append(i)
		n=n/i
print(list1)
