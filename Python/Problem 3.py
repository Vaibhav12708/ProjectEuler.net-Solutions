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
