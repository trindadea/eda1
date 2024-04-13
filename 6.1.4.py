class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
arvere = ArvoreBinaria(5, None, ArvoreBinaria(4, None, ArvoreBinaria(3, None, ArvoreBinaria(2, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))))

def mostra_nivel(no, nivel):
    def busca(no):
            if no == None:
                return ()
            raiz = no.dado
            no_esq = busca(no.esq)
            no_dir = busca(no.dir)
            
            return '(%s %s %s)' %(raiz, no_esq, no_dir)
        
    def busca_nivel(no, nivel, nivel_atual):      
        if nivel == nivel_atual:
            subarv = busca(no)
            if not subarv:
                return
            
            return print(subarv)
        
        if no != None:
            busca_nivel(no.esq, nivel, nivel_atual + 1)
            busca_nivel(no.dir, nivel, nivel_atual + 1)
        
    busca_nivel(no, nivel, 0)
        
mostra_nivel(arvere, 5)