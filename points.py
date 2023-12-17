from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def APUtil(self, u, visited, ap, parent, low, disc):
        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self.APUtil(v, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def articulationPoints(self):
        visited = [False] * (self.V)
        disc = [float("inf")] * (self.V)
        low = [float("inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                self.APUtil(i, visited, ap, parent, low, disc)

        result = []
        for index, value in enumerate(ap):
            if value:
                result.append(index)
        return result

# Example usage:
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Articulation points in the graph:")
print(g.articulationPoints())
