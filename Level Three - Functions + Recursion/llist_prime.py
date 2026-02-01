def prime_nums(arr):
    primes = []

    for n in arr:
        if n <= 1:
            continue

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            primes.append(n)

    return primes
