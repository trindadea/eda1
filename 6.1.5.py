def ArvoreBin(raiz):
    return [raiz, [], []]

def inserirNo(raiz, no):
    if no < raiz[0]:
        inserirEsq(raiz, no)
    else:
        inserirDir(raiz, no)
        
def inserirEsq(raiz, no):
    if len(raiz[1]) != 0:
        return inserirNo(raiz[1], no)
    raiz[1] = ArvoreBin(no)
    return raiz

def inserirDir(raiz, no):
    if len(raiz[2]) != 0:
        return inserirNo(raiz[2], no)
    raiz[2] = ArvoreBin(no)
    return raiz

def preordem(arvore):
    if arvore == []:
        return
    print(arvore[0], end = ' ')
    preordem(arvore[1])
    preordem(arvore[2])
    
def ordem(arvore):
    if arvore == []:
        return
    ordem(arvore[1])
    print(arvore[0], end = ' ')
    ordem(arvore[2])

def posordem(arvore):
    if arvore == []:
        return
    posordem(arvore[1])
    posordem(arvore[2])
    print(arvore[0], end = ' ')

criar_arvore = True
while True:
    comando = input()
    
    if comando == 'quack':
        break
    
    if comando == 'pre':
        if not criar_arvore:
            preordem(arvore)
        print('')
            
    elif comando == 'in':
        if not criar_arvore:
            ordem(arvore)
        print('')
        
    elif comando == 'pos':
        if not criar_arvore:
            posordem(arvore)
        print('')
        
    else:
        if criar_arvore:
            arvore = ArvoreBin(int(comando))
            criar_arvore = False
        else:
            inserirNo(arvore, int(comando))