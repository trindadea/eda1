n = int(input())
cont = [0]*(n+1)

def fibonacci(n):
    cont[n] = cont[n] + 1
    
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print('fibonacci(%i) = %i.' %(n, fibonacci(n)))

for i in range(n+1):
    print('%i chamada(s) a fibonacci(%i).' %(cont[i], i))