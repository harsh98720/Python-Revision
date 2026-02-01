# using Recursion

def fact_recursion(n):
    if n < 0:
        return "Factorial not defined for negative numbers"

    if n == 0 or n == 1:
        return n
    
    return n * fact_recursion(n-1)

print(fact_recursion(10))

# using loops

def fact_loop(n) :
    if n < 0:
        return "Factorial not defined for negative numbers"

    if n == 0 or n == 1:
        return n

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(fact_loop(10))