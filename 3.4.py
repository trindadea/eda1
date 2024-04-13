entrada_1 = input()
m = int(entrada_1.split()[0])
n = int(entrada_1.split()[1])

entrada_2 = input()
P = entrada_2.split()

for i in range (m):
    P[i] = int(P[i])
    
soma = 0

for i in range (m - n + 1):
    soma = P[i:i+n]
    print(sum(soma)//n)


    
