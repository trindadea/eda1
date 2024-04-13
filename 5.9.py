entrada = list(map(int, input().split()))
n = entrada[0]
k = entrada[1]
lista = []

for i in range (n):
    num = int(input())
    if num < 0:
        lista.append((num, -(abs(num)%k)))
    else:
        lista.append((num, num%k))
    
    atual = lista[i]
    j = i
    troca = True
    while j > 0 and lista[j-1][1] <= atual[1]:
        if lista[j-1][1] == atual[1]: #se módulo acima (na lista) for igual ao módulo que se está avaliando
            if lista[j-1][0]%2 == 0: #se número acima (na lista) for par
                if atual[0]%2 == 0: #se número cujo módulo se está avaliando for par
                    if lista[j-1][0] > atual[0]: #se número acima (na lista) for maior que o número que se está avaliando
                        troca = False #não trocar
                else:
                    troca = False
            
            else: #se número acima (na lista) for ímpar
                if atual[0]%2 != 0: #se número cujo módulo se está avaliando for ímpar
                    if lista[j-1][0] < atual[0]: #se número acima (na lista) for menor que o número que se está avaliando
                        troca = False #não trocar
                
        if troca:     
            lista[j] = lista[j-1]
            j = j - 1
        else:
            troca = True
            break
        
    lista[j] = atual
        
for i in range(n):
    print(lista[i][0], end = ' ')