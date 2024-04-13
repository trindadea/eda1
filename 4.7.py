sequencia = [0,1]
cont = 0

def fibonacci(n):
    global cont
    cont += 1 #conta o "nível" em que a função está sendo chamada
    
    if n >= len(sequencia):
        sequencia.append(fibonacci(n-2) + fibonacci(n-1))
    
    cont -= 1
    
    if cont != 0: 
        return sequencia[n]
    else: #cont é zero na chamada mais externa da função, ou seja, a última a ser finalizada
        return sequencia[:n]
    
fibonacci(5)