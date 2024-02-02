def fibonacci_sum(limit):
    fib_sequence = [1, 2]
    while fib_sequence[-1] <= limit:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    even_sum = sum(term for term in fib_sequence if term % 2 == 0)
    return even_sum

limit = 4000000
sum_of_even_terms = fibonacci_sum(limit)
print(sum_of_even_terms)
