import math

n = int(input())
tabela = []

for i in range(n):
    entrada = input().split()
    num_pes = int(entrada[0])
    cons = int(entrada[1])
    
    if num_pes == 0:
        tabela.append([0, 0])
    else:
        tabela.append([math.ceil(cons/num_pes), num_pes])
    
    atual = tabela[i]
    j = i
    while j > 0 and tabela[j-1][0] <= atual[0]:
        if tabela[j-1][0] == atual[0]:
            if tabela[j-1][1] < atual[1]:
                break
        tabela[j] = tabela[j-1]
        j = j - 1
    tabela[j] = atual

for i in range(n):
    print(*tabela[i], sep = " / ")