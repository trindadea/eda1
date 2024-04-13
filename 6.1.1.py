class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
arvere = ArvoreBinaria(1, ArvoreBinaria(2, None, None), ArvoreBinaria(3, None, ArvoreBinaria(4, None, None)))

def mostra(no):
    def busca(no):
        if no == None:
            return ()
        raiz = no.dado
        no_esq = busca(no.esq)
        no_dir = busca(no.dir)
        
        return '(%s %s %s)' %(raiz, no_esq, no_dir)
    
    print(busca(no))

mostra(arvere)