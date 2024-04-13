class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
        

def mostra(arvore, pref):
    print(arvore.dado)
    
    def mostra0(arvore, pref):
        for no in range(len(arvore.filhos)):
            print(pref + arvore.filhos[no].dado)
            mostra0(arvore.filhos[no], pref + pref_ini)
            
    pref_ini = pref
    mostra0(arvore, pref)

arvore = Arvore('A')
arvore.filhos.append(Arvore('B'))
arvore.filhos.append(Arvore('C'))
arvore.filhos[0].filhos.append(Arvore('D'))
arvore.filhos[0].filhos.append(Arvore('E'))
arvore.filhos[0].filhos.append(Arvore('F'))
arvore.filhos[1].filhos.append(Arvore('G'))
arvore.filhos[1].filhos.append(Arvore('H'))

mostra(arvore, '   ')