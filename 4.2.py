def hanoi(altura, p_esquerda, p_direita, p_meio):
    if altura == 0: #caso base
        return None
    else:
        hanoi(altura-1, p_esquerda, p_meio, p_direita) #mover torre de altura n-1 de p_esquerda para p_meio
        print('Mover de %s para %s.' %(p_esquerda, p_direita)) #mover disco de p_esquerda para p_direita
        hanoi(altura-1, p_meio, p_direita, p_esquerda) #mover torre de altura n-1 de p_meio para p_direita

entrada = input()
entrada = entrada.split()

hanoi(int(entrada[0]), entrada[1], entrada[2], entrada[3])