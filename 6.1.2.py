class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        
arvere = ArvoreBinaria(2, None, None)

def altura(no):
    global altura_max
    altura_max = 0
    
    def nivel(no, altura):
        global altura_max
        if no != None:
            if no.esq == None   and no.dir == None   and altura > altura_max:
                altura_max = altura
                return
        else:
            return
        
        nivel(no.esq, altura + 1)
        nivel(no.dir, altura + 1)
        
    nivel(no, altura_max)
    
    return altura_max
    
altura(arvere)