class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
def rotaciona_esquerda(raiz):
    if raiz == None or raiz.dir == None:
        return raiz
    
    aux = ArvoreBinaria(raiz.dado, raiz.esq, raiz.dir.esq)
    raiz = raiz.dir
    raiz.esq =  aux
    return raiz


raiz = ArvoreBinaria('a', ArvoreBinaria('b'), ArvoreBinaria('c'))
print(rotaciona_esquerda(None))