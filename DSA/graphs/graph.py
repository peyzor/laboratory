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

    def bfs(self, start):
        visited = []
        queue = [start]
        while queue:
            v = queue.pop(0)
            visited.append(v)

            for neighbour in sorted(self.graph[v]):
                if neighbour in visited or neighbour in queue:
                    continue

                queue.append(neighbour)

        return visited


def main():
    graph = GraphAdjList()
    for u, v in [(1, 2), (1, 4), (1, 5), (2, 3), (3, 4)]:
        graph.add_edge(u, v)

    print(graph.bfs(1))


if __name__ == '__main__':
    main()
