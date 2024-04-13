class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.visitado = False
        
    def addNeighbor(self, nbr, weight):
        self.connectedTo[nbr.id] = weight

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
                       
    def addEdge(self, f, t, weight):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        
def criarGrafo(num_vertices):
    grafo = Graph()
    for n in range(num_vertices):
        entrada = input().split()
        chave = entrada[0]
        num_arestas = int(entrada[1])
        vizinhos = entrada[2:]
        
        if chave not in grafo.vertList:
            grafo.addVertex(chave)

        i = 0
        for n in range(num_arestas):
            grafo.addEdge(chave, vizinhos[i+1], vizinhos[i])
            i = i + 2
            
    return grafo

grafo = criarGrafo(int(input()))

def maior_dist(vertice_o, vertice_d):
    
    
for vertice_o in grafo.vertList.values():
    for vertice_d in grafo.vertList.values():
        tabela.append(maior_dist(vertice_o, vertice_d))
    
    