class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
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
            
        for vertice in vizinhos:
            grafo.addEdge(chave, vertice)
            
    return grafo

grafo_1 = criarGrafo(int(input()))
input() #linha em branco
grafo_2 = criarGrafo(int(input()))

def eSub(grafo_1, grafo_2):
    for vertice in grafo_2.vertList:
        if vertice in grafo_1.vertList: #se vertice do grafo_2 estiver no grafo_1
            vertice_1 = grafo_1.vertList[vertice]
            vertice_2 = grafo_2.vertList[vertice]
            
            for vizinho in vertice_2.connectedTo:
                if vizinho not in vertice_1.connectedTo: #se algum vizinho desse vertice no grafo_2 não for vizinho também no grafo_1.
                    return False
        else:
            return False
    return True

if eSub(grafo_1, grafo_2):
    print('Sub-sub!')
else:
    print('Ue? Ue? Ue?')