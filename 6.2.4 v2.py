class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
        

def constituiArvoreBinariaDeBusca(arvore):
    #O programa percorre a árvore em pré-ordem verificando
    if arvore.esq != None:
        if arvore.esq.dado < arvore.dado: #se o filho a esquerda é menor que o pai
            no_esq = constituiArvoreBinariaDeBusca(arvore.esq)
        else:
            return False
    else:
        no_esq = True
        
    if no_esq:
        if arvore.dir != None:
            if arvore.dir.dado > arvore.dado: #e se o filho a direita é maior que o pai
                no_dir = constituiArvoreBinariaDeBusca(arvore.dir)
            else:
                return False #caso contrário, a função retorna False ao parâmetro que a chamou ("no_esq" ou "no_dir")
        else:
            no_dir = True #caso a recursão atinga um nó folha, ela retorna True ao parâmetro que a chamou (nesse caso, "no_dir")
    
    return no_esq and no_dir #a função retorna True ao parâmetro que a chamou apenas no caso em que ambos os nós filhos ("no_esq" e "no_dir") forem True.

raiz = ArvoreBinaria(19, ArvoreBinaria(31, ArvoreBinaria(3, ArvoreBinaria(7, None, None), ArvoreBinaria(29, None, None)), ArvoreBinaria(10, ArvoreBinaria(5, None, None), ArvoreBinaria(14, None, None))), ArvoreBinaria(9, ArvoreBinaria(15, ArvoreBinaria(18, None, None), ArvoreBinaria(21, None, None)), ArvoreBinaria(28, ArvoreBinaria(8, None, None), ArvoreBinaria(17, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(9, ArvoreBinaria(28, ArvoreBinaria(27, ArvoreBinaria(20, None, None), ArvoreBinaria(6, None, None)), ArvoreBinaria(15, ArvoreBinaria(23, None, None), ArvoreBinaria(13, None, None))), ArvoreBinaria(29, ArvoreBinaria(18, ArvoreBinaria(24,
None, None), ArvoreBinaria(14, None, None)), None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(29, ArvoreBinaria(4, None, ArvoreBinaria(18, ArvoreBinaria(11, None, None), ArvoreBinaria(20, None, None))), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(6, None, ArvoreBinaria(31, ArvoreBinaria(22, ArvoreBinaria(8, None, None), None), None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(28, ArvoreBinaria(4, ArvoreBinaria(22, ArvoreBinaria(8, None, None), ArvoreBinaria(16, None, None)), ArvoreBinaria(18, ArvoreBinaria(0, None, None), ArvoreBinaria(20, None, None))), ArvoreBinaria(31, ArvoreBinaria(11, ArvoreBinaria(25, None, None), None), ArvoreBinaria(1, ArvoreBinaria(21, None, None), ArvoreBinaria(9, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(5, None, ArvoreBinaria(31, ArvoreBinaria(22, ArvoreBinaria(19, None, None), ArvoreBinaria(28, None, None)),
None))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(3, None, ArvoreBinaria(17, ArvoreBinaria(11, None, None), ArvoreBinaria(27, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(19, ArvoreBinaria(2, ArvoreBinaria(26, ArvoreBinaria(4, None, None), ArvoreBinaria(14, None, None)), ArvoreBinaria(25, ArvoreBinaria(21, None, None), ArvoreBinaria(13, None, None))), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(25, ArvoreBinaria(8, ArvoreBinaria(29, ArvoreBinaria(7, None, None), ArvoreBinaria(16, None, None)), ArvoreBinaria(30, None, ArvoreBinaria(19, None, None))), ArvoreBinaria(17, ArvoreBinaria(2, ArvoreBinaria(13, None, None), ArvoreBinaria(5, None, None)), ArvoreBinaria(23, ArvoreBinaria(18, None, None), ArvoreBinaria(0, None, None))))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(31, ArvoreBinaria(30, ArvoreBinaria(13, ArvoreBinaria(4, None, None), ArvoreBinaria(18, None, None)), None), None)
print(constituiArvoreBinariaDeBusca(raiz))