class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = False
        
    def addNeighbor(self, nbr):
        self.connectedTo[nbr.id] = nbr

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
                       
    def addEdge(self, f, t):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])
        
def criarGrafo(num_vertices):
    grafo = Graph()
    for n in range(num_vertices):
        entrada = input().split()
        chave = entrada[0]
        num_arestas = int(entrada[1])
        vizinhos = entrada[2:]
        
        if chave not in grafo.vertList:
            grafo.addVertex(chave)
        for vizinho in vizinhos:
            grafo.addEdge(chave, vizinho)
    return grafo

def eRubroNegro(grafo):
    for vertice in grafo.vertList.values():
        if vertice.color == 'R':
            for vizinho in vertice.connectedTo.values():
                if not vizinho.color:
                    vizinho.color = 'B'
                elif vizinho.color == 'R':
                    return False   
                    
        elif vertice.color == 'B':
            for vizinho in vertice.connectedTo.values():
                if not vizinho.color:
                    vizinho.color = 'R'
                elif vizinho.color == 'B':
                    return False
                    
        else:
            vertice.color = 'R'
            for vizinho in vertice.connectedTo.values():
                if not vizinho.color:
                    vizinho.color = 'B'
                elif vizinho.color == 'R':
                    return False 
                
    return True
    
grafo = criarGrafo(int(input()))

if eRubroNegro(grafo):
    print('Lerei "O Vermelho e o Negro".')
else:
    print('Mais cor, por favor!')