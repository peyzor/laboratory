class GraphMatrix:
    def __init__(self, num_of_vertices):
        self.graph = [[False for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]

    def add_edge(self, u, v):
        if u < 0 or u >= len(self.graph) or v < 0 or v >= len(self.graph):
            raise ValueError('invalid input')

        self.graph[u][v] = True
        self.graph[v][u] = True


class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()

        if v not in self.graph:
            self.graph[v] = set()

        self.graph[u].add(v)
        self.graph[v].add(u)

    def edge_exists(self, u, v):
        pass
