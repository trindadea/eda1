n = int(input())
lista = input().split()
tabela_disp = [None]*n
pecas_dup = 0

for i in range(n):
    index = (ord(lista[i][0]) + int(lista[i][1]))%n
    
    if tabela_disp[index] == None:
        tabela_disp[index] = lista[i]
    else:
        j = index
        while tabela_disp[j] != None:
            if tabela_disp[j] == lista[i]:
                pecas_dup = pecas_dup + 1
                break
            else:
                j = j + 1
                if j == n:
                    j = 0
        tabela_disp[j] = lista[i]
print(pecas_dup)