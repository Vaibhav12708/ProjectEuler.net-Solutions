max_length=0
max_chain=0
for i in range(1,1000000):
    length=collatz(i)
    if length>max_length:
        max_length=length
        max_chain=i
print(max_chain)

max_length=0
max_chain=0
for i in range(1,1000000):
    length=collatz(i)
    if length>max_length:
        max_length=length
        max_chain=i
print(max_chain)
