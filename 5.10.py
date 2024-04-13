n = int(input())
lista = []

for i in range (n):
    entradas = input().split()
    nome = entradas[0]; sobrenome = entradas[1]; altura = int(entradas[2]); peso = int(entradas[3])
    
    lista.append(['%s, %s' %(sobrenome, nome), abs(180 - altura), 75 - peso])
   
    atual = lista[i]
    j = i
    troca = True
    comparar_pesos = False
    
    while j > 0 and lista[j-1][1] >= atual[1]:
        nome_acima = lista[j-1][0]       #nome do pretendente acima (na lista)
        altura_acima  = lista[j-1][1]    #diferenca absoluta entre a altura ideal e a altura do pretendente acima (na lista)
        peso_acima = lista[j-1][2]       #diferenca entre o peso ideal e o peso do pretendente acima (na lista)
#                                             se > 0, ele é mais leve
#                                             se == 0, ele tem o peso ideal
#                                             se < 0, ele é mais pesado

        if altura_acima == atual[1]:
            if peso_acima >= 0 and atual[2] >= 0:
                if peso_acima >= atual[2]:
                    if peso_acima == atual[2]:
                        if nome_acima < atual[0]:
                            troca = False
                else:
                    troca = False
                    
                    
                    
            elif peso_acima < 0 and atual[2] < 0:
                if peso_acima <= atual[2]:
                    if peso_acima == atual[2]:
                        if nome_acima < atual[0]:
                            troca = False
                else:
                    troca = False
                   
                   
                   
            elif peso_acima >= 0 and atual[2] < 0:
                troca = False
                
        if troca:     
            lista[j] = lista[j-1]
            j = j - 1
        else:
            troca = True
            break
        
    lista[j] = atual
        
for i in range(n):
    print(lista[i][0])