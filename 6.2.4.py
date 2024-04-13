class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
def ver_no_esq(no, raiz):
        if no == None:
            return
        if no.dado > raiz.dado:
            return False
        return True
    
def ver_no_dir(no, raiz):
    if no == None:
            return
    if no.dado < raiz.dado:
        return False
    return True

def constituiArvoreBinariaDeBusca(arvore):
    no_esq = ver_no_esq(arvore.esq, arvore)
    no_dir = ver_no_dir(arvore.dir, arvore)
    
    if no_esq and no_dir:
        return constituiArvoreBinariaDeBusca(arvore.esq) and constituiArvoreBinariaDeBusca(arvore.dir)
    elif no_esq == None and no_dir:
        return constituiArvoreBinariaDeBusca(arvore.dir)
    elif no_esq and no_dir == None:
        return constituiArvoreBinariaDeBusca(arvore.esq)
    elif no_esq == False or no_dir == False:
        return False
    else:
        return True

raiz = ArvoreBinaria(19, ArvoreBinaria(2, ArvoreBinaria(26, ArvoreBinaria(4, None, None), ArvoreBinaria(14, None, None)), ArvoreBinaria(25, ArvoreBinaria(21, None, None), ArvoreBinaria(13, None, None))), None)
print(constituiArvoreBinariaDeBusca(raiz))
    