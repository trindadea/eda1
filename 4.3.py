sequencia = [0,1]

def fibonacci(n): #função implementada com PD para poupar recursos
    if n >= len(sequencia):
        sequencia.append(fibonacci(n-2) + fibonacci(n-1))
   
    return sequencia[n]