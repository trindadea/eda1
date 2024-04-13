parentes = int(input())
casas = list(map(int, input().split()))
distancias = [0] #o 0 é adicionado para efeito de comparação do primeiro elemento adicionado em distancias 

for i in range(parentes):
    soma = 0
    for j in range(parentes):
        soma = soma + (abs(casas[i] - casas[j]))
    distancias.append(soma)

    k = i + 1
    while k > 0 and soma > distancias[k - 1]:
        distancias[k] = distancias[k - 1]#essa comparação
        k = k - 1
    distancias[k] = soma
distancias.pop() #pop 0 que, após a ordenação, deve estar no último indice
print(distancias.pop())