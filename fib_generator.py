def fib_generator(n):
    a, b = 0, 1
    fibonacci = [a, b]
    while True:
        a, b = b, a + b
        fibonacci.append(b)
        if b >= n:
            break
    print(fibonacci)
    

fib_generator(20)
