

class Graph:


    def __init__():
        self.adjMatrix = [[]]
        self.V = {}

    def addEdge(self,v,u,w):
        self.V[v].append(u,w)
        self.V[u].append(v,w)

        self.edges.append(V[v],V[u])

    def addVertex(self,v):
        if v in self.V:
            return
        V[v] = [(None,None)]
# MST- KRUSKAL (G, w)
#  1. A ← ∅
#  2. for each vertex v ∈ V [G]
#  3. do MAKE - SET (v)
#  4. sort the edges of E into non decreasing order by weight w
#  5. for each edge (u, v) ∈ E, taken in non decreasing order by weight
#  6. do if FIND-SET (μ) ≠ if FIND-SET (v)
#  7. then A  ←  A ∪ {(u, v)}
#  8. UNION (u, v)
#  9. return A