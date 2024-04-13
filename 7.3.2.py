class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.dist = False
        self.visitado = False
        
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
        
def criarGrafo(num_vertices):
    grafo = Graph()
    for n in range(num_vertices):
        entrada = input().split()
        chave = entrada[0]
        num_arestas = int(entrada[1])
        vizinhos = entrada[2:]
        
        if chave not in grafo.vertList:
            grafo.addVertex(chave)
        for a in range(num_arestas):
            grafo.addEdge(chave, vizinhos[a])
            
    return grafo

grafo = criarGrafo(int(input()))
entrada = input().split()
Eu = entrada[0]; Mussum = entrada[1]

def menor_dist(grafo, origem, destino, dist = 0):
    vertice = grafo.vertList[origem]
    if not vertice.dist:
        vertice.dist = dist
    else:
        if dist <= vertice.dist:
            vertice.dist = dist
            vertice.visitado = False
    
    if vertice.visitado:
        return
    
    vertice.visitado = True

    for contato in vertice.connectedTo:
        menor_dist(grafo, contato, destino, dist+1)
    return grafo.vertList[destino].dist

achou = menor_dist(grafo, Eu, Mussum)

if achou:
    print(achou-1)
else:
    print('Forevis alonis...')