entrada = input().split()
obj_paulo = int(entrada[0])
disc_paulo = int(entrada[1])
idade_paulo =  int(entrada[3])
pont_paulo = (2*obj_paulo + 3*disc_paulo + int(entrada[2]))

n = int(input())
posicao = 1

for i in range(n):
    entrada = input().split()
    obj_atual = int(entrada[0])
    disc_atual = int(entrada[1])
    idade_atual = int(entrada[3])
    pont_atual = (2*obj_atual + 3*disc_atual + int(entrada[2]))
    
    if pont_atual < pont_paulo:
        pass
    elif pont_atual > pont_paulo:
        posicao = posicao + 1
    else:
        if (idade_atual >= 60 and idade_paulo >=60) or (idade_atual < 60 and idade_paulo < 60):
            if disc_atual >= disc_paulo:
                if disc_atual == disc_paulo:
                    if obj_atual >= obj_paulo:
                        if obj_atual == obj_paulo:
                            if idade_atual >= idade_paulo:
                                if idade_atual == idade_paulo:
                                    pass    
                                else:
                                    posicao = posicao + 1
                            else:
                                pass
                        else:
                            posicao = posicao + 1
                    else:
                        pass
                else:
                    posicao = posicao + 1
            else:
                pass
            
        elif (idade_atual >= 60 and idade_paulo < 60):
            posicao = posicao + 1
        else:
            pass
        
print(posicao)