cont = 0

def Fib(n):
    global cont
    cont = cont + 1
    
    if n < 2:
        return n
    else:
        return Fib(n-2) + Fib(n-1)

n = int(input())

print ('Fib(%i) = %i (%i chamadas)'%(n, Fib(n), cont))