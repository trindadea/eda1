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
    
    def removeVertex(self, key):
        if key in self.vertList:
            del self.vertList[key]
            self.numVertices = self.numVertices - 1
                       
    def addEdge(self, f, t):
        if f in self.vertList and t in self.vertList:
            if self.vertList[t] not in self.vertList[f].connectedTo:
                self.vertList[f].addNeighbor(self.vertList[t])
                self.vertList[t].addNeighbor(self.vertList[f])
    
    def removeEdge(self, f, t):
        if f in self.vertList and t in self.vertList:
            f = self.vertList[f]
            t = self.vertList[t]
            
            for i in range(len(f.connectedTo)):
                if f.connectedTo[i] == t:
                    del f.connectedTo[i]
                    break
            for i in range(len(t.connectedTo)):
                if t.connectedTo[i] == f:
                    del t.connectedTo[i]
                    break
            
        
def criarGrafo(num_vertices):
    grafo = Graph()
    for n in range(num_vertices):
        entrada = input().split()
        instrucao = entrada[0]
        dados = entrada[1:]
        
        if instrucao == 'IV':
            grafo.addVertex(dados[0])
            
        elif instrucao == 'RV':
            for vertice in grafo.vertList.keys():
                grafo.removeEdge(vertice, dados[0])
            grafo.removeVertex(dados[0])
            
        elif instrucao == 'IA':
            grafo.addEdge(dados[0], dados[1])
            
        else:
            grafo.removeEdge(dados[0], dados[1])
        
    return grafo

grafo = criarGrafo(int(input()))
menor_grau = 0
menor_grau_local = float('inf')

for vertice in grafo.vertList.values():
    grau = len(vertice.connectedTo)
    if grau < menor_grau_local:
        menor_grau_local = grau
        menor_grau = grau
print(menor_grau)