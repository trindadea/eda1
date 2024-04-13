class ArvoreBinaria():
    def __init__(self, dado, esquerda = None, direita = None):
        self.dado = dado
        self.esq = esquerda
        self.dir = direita
 
def ver_caminho(raiz, v1, v2, caminho):
    global found
    if found < 2:
        if raiz == None:
            return
        
        dado = raiz.dado
        caminho = caminho + str(dado) + ' '
           
        if dado == v1 or dado == v2:
            caminhos.append(caminho)
            found = found + 1
            
        ver_caminho(raiz.esq, v1, v2, caminho)
        ver_caminho(raiz.dir, v1, v2, caminho)
        
    return caminhos
    
def verificaPontuacao(raiz, v1, v2):
    global caminhos
    global found
    caminhos = []
    
    if v1 == v2:
        found = 1
        caminhos = 2*ver_caminho(raiz, v1, v2, '')
    else:
        found = 0
        caminhos = ver_caminho(raiz, v1, v2, '')
        
    caminhos[0] = caminhos[0].split(); caminhos[1] = caminhos[1].split()
    
    if len(caminhos[0]) > len(caminhos[1]):
        caminhos[0], caminhos[1] = caminhos[1], caminhos[0]
        
    for e in range(len(caminhos[0]), 0, -1):
        if caminhos[0][e-1] in caminhos[1]:
            return caminhos[0][e-1]

raiz = ArvoreBinaria(17, ArvoreBinaria(19, ArvoreBinaria(16, ArvoreBinaria(10, None, None), ArvoreBinaria(7, None, None)), ArvoreBinaria(5, ArvoreBinaria(8, None, None), ArvoreBinaria(3, None, None))), ArvoreBinaria(21, ArvoreBinaria(18, None, ArvoreBinaria(12, None, None)), ArvoreBinaria(0, ArvoreBinaria(22, None, None), ArvoreBinaria(20, None, None))))
print(verificaPontuacao(raiz, 21, 0))
print(verificaPontuacao(raiz, 3, 10))
print(verificaPontuacao(raiz, 7, 21))
print(verificaPontuacao(raiz, 17, 3))
print(verificaPontuacao(raiz, 21, 22))