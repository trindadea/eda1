entrada_1 = input()
T = int(entrada_1.split()[0])
N = int(entrada_1.split()[1])

if N == 0:
    print('0 - [x]')
    
else:    
    entrada_2 = input()
    chaves = entrada_2.split()
        
    for i in range(N):
        chaves[i] = int(chaves[i])
        
    matriz = []

    for i in range (T):
        matriz.append([])

    for chave in chaves:
        matriz_ind = chave%T
        
        if len(matriz[matriz_ind]) >= 1:
            matriz[matriz_ind].append(' -> ')
        
        matriz[matriz_ind].append(chave)

    for i in range (T):
        if matriz[i] == []:
            print('%i - [x]' %i)
        else:
            matriz[i] = ''.join(map(str,matriz[i]))
            print('%i - %s' %(i, matriz[i]))