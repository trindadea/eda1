class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
def nivel(raiz, no):
    def ver_nivel(raiz, no, nivel):
        global found
        
        if found:
            return -1
        else:
            if raiz == None:
                return -1
            
            if raiz.dado == no:
                found = True
                return nivel
    
            return max(
                ver_nivel(raiz.esq, no, nivel+1),
                ver_nivel(raiz.dir, no, nivel+1))
        
    global found
    found = False
    return ver_nivel(raiz, no, 0)
            
arvere = ArvoreBinaria(None, None, None)
            
print(nivel(arvere, 3))