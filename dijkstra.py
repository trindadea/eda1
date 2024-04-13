from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
        
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0
    
        pq = PriorityQueue()
        pq.put((0, start_vertex))
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
    
            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
    
g = Graph(6)
g.add_edge(1, 2, 10)
g.add_edge(1, 5, 5)
g.add_edge(2, 1, 10)
g.add_edge(2, 3, 1)
g.add_edge(2, 5, 4)
g.add_edge(3, 2, 1)
g.add_edge(3, 4, 1)
g.add_edge(4, 2, 8)
g.add_edge(4, 3, 1)
g.add_edge(4, 5, 1)
g.add_edge(5, 1, 5)
g.add_edge(5, 2, 4)
g.add_edge(5, 4, 1)

print(g.dijkstra(2))