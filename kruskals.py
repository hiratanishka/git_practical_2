class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}


        for vertex in vertices:
            self.parent[vertex] = vertex


    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])


        return self.parent[node]


    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)


        if root_u != root_v:
            self.parent[root_v] = root_u




def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])


    ds = DisjointSet(vertices)


    mst = []
    total_cost = 0


    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight


    return mst, total_cost




vertices = ['A', 'B', 'C', 'D']


edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8)
]


mst, cost = kruskal(vertices, edges)


print("Minimum Spanning Tree:")
print(mst)
print("Total cost:", cost)
