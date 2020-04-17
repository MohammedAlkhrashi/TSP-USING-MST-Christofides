
from operator import itemgetter
class Graph:


    def __init__(self):
        # self.adjMatrix = [[]]
        # self.V = {}
        self.graph = {"vertices":[],"edges":set([])}
        self.parent={}

    def addEdge(self,v,u,w):
        # self.V[v].append(u,w)
        # self.V[u].append(v,w)
        # self.edges.append(V[v],V[u])
        self.graph["edges"].add((v,u,w))

    def addVertex(self,v):
        # if v in self.V:
            # return
        # self.V[v] = [(None,None)]
        self.graph["vertices"].append(v)
        

    def union(self,v,u):
        parentV = self.findParent(v)
        parentU = self.findParent(u)
        if parentV != parentU:
            self.parent[parentU] = parentV ## No matter who will be the parent (Xd) , see findParent() and draw the graph to be clear
        

    def findParent(self,v):
        if self.parent[v] != v :
            return self.findParent(self.parent[v])
        else:
            return v

    def KRUSKAL(self):
        MST = set()
        for v in self.graph["vertices"]:
            self.parent[v] = v #MAKE - SET (v)
        
        edges =list(self.graph["edges"])
        edges.sort(key=itemgetter(2)) ## by w - > (v,u,w) 
        
        for v,u,w in edges:
            if self.findParent(v) != self.findParent(u):
                MST.add((v,u,w))
                self.union(v,u)

        return MST


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("F")

g.addEdge("D",'F',10) 
g.addEdge("C",'B',1)
g.addEdge("A",'B',3)  
g.addEdge("C",'A',2)
g.addEdge("B",'D',7)
g.addEdge("C",'F',8)
g.addEdge("D",'C',1)
g.addEdge("D",'A',2)

print(g.graph)
print("------------------------------------------------------------------")
print(g.KRUSKAL())
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