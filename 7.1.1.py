class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def __contains__(self, n):
        return n in self.vertList
        
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def removeVertex(self, key):
        if key in self.vertList:
            del self.vertList[key]
            self.numVertices = self.numVertices - 1
                       
    def addEdge(self, f, t, weight = 0):
        if f in self.vertList and t in self.vertList:
            self.vertList[f].addNeighbor(self.vertList[t], weight)
            
    def removeEdge(self, f, t):
        if f in self.vertList and t in self.vertList:
            f = self.vertList[f]
            t = self.vertList[t]
            
            if t in f.connectedTo:
                del f.connectedTo[t]
            


grafo = Graph()

for iter in range(int(input())):
    entrada = input().split(' ', 1)
    instrucao = entrada[0]
    dados = entrada[1].split()
    
    if instrucao == 'IV':
        grafo.addVertex(dados[0])
        
    elif instrucao == 'RV':
        for vertice in grafo.vertList.keys():
            grafo.removeEdge(vertice, dados[0])
        grafo.removeVertex(dados[0])
        
    elif instrucao == 'IA':
        grafo.addEdge(dados[0], dados[1], float(dados[2]))
        
    else:
        grafo.removeEdge(dados[0], dados[1])

peso_total = 0
num_arestas = 0

for vertice in grafo.vertList:
    vertice = grafo.vertList[vertice]
    arestas = vertice.connectedTo
    num_arestas = num_arestas + len(arestas)
    for peso in arestas.values():
        peso_total = peso_total + peso
        
print("%i vertice(s), %i aresta(s) e peso total %.2f." %(len(grafo.vertList), num_arestas, peso_total))