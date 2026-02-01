n = 100

def check_prime(n) :
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

prime_nums = []
    
for k in range(2, n+100):
    if check_prime(k) :
        prime_nums.append(k)

print(prime_nums)