class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = []
        
    def addNeighbor(self, nbr):
        self.connectedTo.append(nbr)

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
                       
    def addEdge(self,f, t):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t])



def isCiclic(graph):
    for vertice in graph.vertList:
        vertice = graph.vertList[vertice]
        for neighbor in vertice.connectedTo:
            if vertice in neighbor.connectedTo:
                return True
    return False

grafo = Graph()

for i in range(int(input())):
    entrada = input().split()
    if entrada[0] not in grafo.vertList:
        grafo.addVertex(entrada[0])

    for j in range(int(entrada[1])):
        grafo.addEdge(entrada[0], entrada.pop())
        
if isCiclic(grafo):
    print('Hoje tem!')
else:
    print('... que ama ninguem.')