lista = []
dados_paulo = (list(map(int, input().split())))
pont_paulo = (2*dados_paulo[0] + 3*dados_paulo[1] + dados_paulo[2])

dados_paulo.append(pont_paulo); lista.append(dados_paulo)

n = int(input())
posicao = 1

for i in range(1, n+1):
    dados_atual = (list(map(int, input().split())))
    pont_atual = (2*dados_atual[0] + 3*dados_atual[1] + dados_atual[2])
    
    if pont_atual < pont_paulo:
        pass
    elif pont_atual > pont_paulo:
        posicao = posicao + 1
    else:
        dados_atual.append(pont_atual); lista.append(dados_atual)
        
        atual = lista[-1]
        j = len(lista) - 1
        troca = True
        
        while j > 0 and lista[j-1][4] <= atual[4]:
            anterior = lista[j-1]
            
            if anterior[4] == atual[4]:
                if (anterior[3] >= 60 and atual[3] >= 60) or (anterior[3] < 60 and atual[3] < 60):
                    if anterior[1] >= atual[1]:
                        if anterior[1] == atual[1]:
                            if anterior[0] <= atual[0]:
                                if anterior[0] == atual[0]:
                                    if anterior[3] >= atual[3]:
                                        troca = False
                            else:
                                troca = False
                        else:
                            troca = False
                                
                elif anterior[3] >= 60 and atual[3] < 60:
                    troca = False
                                
            if troca:     
                lista[j] = anterior
                j = j - 1
            else:
                troca = True
                break
            
        lista[j] = atual
