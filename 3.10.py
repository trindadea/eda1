entrada = None
matriz = []
lista = []
index = 0

while True:
    entrada = input()
    if entrada == 'f':
        break
    
    else:
        entrada = entrada.split()
        if entrada[0] == 'r':
            entrada[1] =  int(entrada[1])
            index = index + 1
            
            for i in range(len(matriz)):
                if matriz[i] != None:
                    if matriz[i][0] == entrada[1]:
                        matriz[i] = None
        else:
            c = int(entrada[1])
            j = int(entrada[2])
            
            matriz.append([c, j, index])
            index = index + 1
            
pos = 0

for i in range (len(matriz)):
    if matriz[i] != None:
        matriz[i].append(pos)
        pos = pos + 1
        
        linha = matriz[i-matriz[i][1]]
        if linha != matriz[i] and linha != None:
            lista.append('[%i,%i,%i]' %(matriz[i][0], matriz[i][2], linha[3]))
        else:
            lista.append('[%i,%i]' %(matriz[i][0], matriz[i][2]))
            
if lista:
    print(' '.join(str(char) for char in lista))
else:
    print('-1')