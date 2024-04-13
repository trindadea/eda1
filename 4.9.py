fibonacci = [0,1]
fibonaocci = []

n = int(input())
fib_len = 0

while fib_len < n:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
    
    i = fibonacci[-2] + 1
    while i < fibonacci[-1]:
        fibonaocci.append(i)
        i = i + 1
        fib_len = fib_len + 1
        if fib_len == n:
            break
print(*fibonaocci, sep=', ')