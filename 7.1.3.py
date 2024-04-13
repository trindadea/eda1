class painel:
    def __init__(self, valor, correto):
        self.valor = valor
        self.correto = correto
        self.acoes_rest = 20
    
    def VerificaPainel(self):
        return self.valor
    
    def verificaAcoesRestantes(self):
        return self.acoes_rest
    
    def incrementarValor(self):
        if self.acoes_rest > 0:
            self.valor = self.valor + 1
            self.acoes_rest = self.acoes_rest - 1
            return True
        return False
    
    def dobrarValor(self):
        if self.acoes_rest > 0:
            self.valor = self.valor * 2
            self.acoes_rest = self.acoes_rest - 1
            return True
        return False
    
    def inverterValor(self):
        if self.acoes_rest > 0:
            aux = self.valor
            aux = list(str(aux))
            aux.reverse()
            self.valor = int(''.join(aux))
            self.acoes_rest = self.acoes_rest - 1
            return True
        return False  
    
def destravarPainel(painel, origem, objetivo):

        
ORIGEM = 835
DESTINO = 761
painel = painel(ORIGEM, DESTINO)
destravarPainel(painel, ORIGEM, DESTINO)