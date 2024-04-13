entrada = input().split()
a = int(entrada[0])
t = int(entrada[1])
tabela = [] 

for i in range(a):
    dados = input().split(' ', 1)
    IRA = dados[0]
    nome = dados[1]
    tabela.append((IRA, nome))
    
    atual = tabela[i]
    j = i
    while j > 0 and float(tabela[j-1][0]) <= float(atual[0]):
        if float(tabela[j-1][0]) == float(atual[0]):
            if tabela[j-1][1] > atual[1]:
                break
            
        tabela[j] = tabela[j-1]
        j = j - 1
    tabela[j] = atual

for i in range(t):
    n = (int(input()) - 1)
    print('%s (%s)'%(tabela[n][1], tabela[n][0]))