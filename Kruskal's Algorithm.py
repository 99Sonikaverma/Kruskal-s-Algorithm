# Kruskal's algorithm in Python
class Graphs:
    def __init__(self, vertices):
        self.Vertex = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parents, i):
        if parents[i] == i:
            return i
        return self.find(parents, parents[i])

    def apply_union(self, parents, rank, m, n):
        mroot = self.find(parents, m)
        nroot = self.find(parents, n)
        if rank[mroot] < rank[nroot]:
            parents[mroot] = nroot
        elif rank[mroot] > rank[nroot]:
            parents[nroot] = mroot
        else:
            parents[nroot] = mroot
            rank[mroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algorithm(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parents = []
        rank = []
        for node in range(self.Vertex):
            parents.append(node)
            rank.append(0)
        while e < self.Vertex - 1:
            u, v, w = self.graph[i]
            i = i + 1
            m = self.find(parents, u)
            n = self.find(parents, v)
            if m != n:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parents, rank, m, n)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graphs(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algorithm()