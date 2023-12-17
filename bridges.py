from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, low, disc):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridge_util(v, visited, parent, low, disc)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    print(f"Bridge found: ({u}, {v})")

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_bridges(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [-1] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, parent, low, disc)

# Example usage:
g = Graph(5)  # Create a graph with 5 vertices
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

print("Bridges in the graph:")
g.find_bridges()
