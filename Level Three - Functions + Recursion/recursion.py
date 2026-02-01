import math

# sum of digits
def digit_sum(n):
    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)

# reverse Numbers
def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)
    
    

print(reverse_num(123))

# count digits
def digit_count(n):
    if n < 10:
        return 1
    return 1 + digit_count(n // 10)

print(digit_count(0))