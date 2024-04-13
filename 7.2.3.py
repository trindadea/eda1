class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
        
    def insere_v(self, id, dado):
        self.vertices[id] = dado
    
    def insere_a(self, id_o, id_d):
        if id_o in self.vertices and id_d in self.vertices:
            self.arestas.append((id_o, id_d))
    
    def remove_v(self, id):
        if id in self.vertices:
            del self.vertices[id]
            
            i = 0
            while i < len(self.arestas):
                if id in self.arestas[i]:
                    del self.arestas[i]
                else:
                    i = i+1

    def remove_a(self, id_o, id_d):
        if (id_o, id_d) in self.arestas:
            self.arestas.remove((id_o, id_d))
    
    def grau_saida(self, id):
        grau = 0
        if id in self.vertices:
            for par in self.arestas:
                if par[0] == id:
                    grau = grau + 1
        return grau
    
    def grau_entrada(self, id):
        grau = 0
        if id in self.vertices:
            for par in self.arestas:
                if par[1] == id:
                    grau = grau + 1
        return grau
    
    def alcancavel(self, id_u, id_v, visitados = []):
        if id_u in self.vertices and id_v in self.vertices and id_u not in visitados:
            for par in self.arestas:
                if par[0] == id_u:
                    if id_u not in visitados:
                        visitados.append(id_u)
                    if par[1] == id_v:
                        return True
                    else:
                        if self.alcancavel(par[1], id_v, visitados):
                            return True
        return False
            
grafo = Grafo()
grafo.insere_v('A', 'VerticeA')
grafo.insere_v('B', 'VerticeB')
grafo.insere_v('C', 'VerticeC')
grafo.insere_v('D', 'VerticeD')
grafo.insere_v('E', 'VerticeE')
grafo.insere_a('A', 'B')
grafo.insere_a('A', 'C')
grafo.insere_a('A', 'D')
grafo.insere_a('B', 'C')
grafo.insere_a('C', 'D')
grafo.insere_a('D', 'A')
grafo.insere_a('D', 'B')
grafo.insere_a('D', 'C')

grafo.alcancavel('A', 'E')