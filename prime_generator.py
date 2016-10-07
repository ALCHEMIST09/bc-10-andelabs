def generate_primes(n):
    """
        Function to generate prime numbers
        from zero to n
    """
    primes = [2]
    start = 3
    while True:
        for divisor in range(2, int(start**0.5) + 1, 2):
            if start % divisor == 0:
                break
        else:
            primes.append(start)
        start += 1
        if start == n:
            break
    return primes


print(generate_primes(20))

