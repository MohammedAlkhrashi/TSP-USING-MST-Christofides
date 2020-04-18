from operator import itemgetter
from Graph import Graph
import Christofid


def KRUSKAL(g):
    parent = {} 
    MST = Graph()
    
    for key,value in g.vertices.items():
        MST.addVertex(key,value[0],value[1])
        parent[key] = key #MAKE - SET (v)
    
    edges =list(g.edges)
    edges.sort(key=itemgetter(2)) ## by w - > (v,u,w) 
    
    for v,u,w in edges:
        if findParent(parent,v) != findParent(parent,u):
            MST.addEdge(v,u,w)
            union(parent,v,u)

    return MST
def union(parent,v,u):
    parentV = findParent(parent,v)
    parentU = findParent(parent,u) ##
    if parentV != parentU:
        parent[parentU] = parentV ## No matter who will be the parent (Xd) , see findParent() and draw the graph to be clear
    

def findParent(parent,v):

    if parent[v] != v :
        return findParent(parent,parent[v])
    else:
        return v


def Christofides(g):
    MST = KRUSKAL(g);     
    
    MWPM = mimumWeightPerfectMatching(g,MST); 

    multiGraph = graphUnion(MST,MWPM)

    eulerianCircut = formEulerCircut(multiGraph); 
    
    hamlitonianCircut = formHamiltonianCircut(eulerianCircut)

    return hamlitonianCircut

def mimumWeightPerfectMatching(g,MST):
    odds = findOdds(MST)
    minWeightPM = Graph() ## minWeightPM : Mim Weight Perfect Matching
    minWeightPM.vertices = g.vertices
    minWeightPM.weights = g.weights
    print(odds)
    while len(odds) > 0 :
        v = odds.pop()
        print("v = ",v)
        minimum = float("inf")
        for u in odds:
            if( (v,u) not in g.weights):
                continue; 
            if g.weight(v,u) < minimum:
                minimum = g.weight(v,u)
                closest = u
          
        minWeightPM.addEdge(closest,v,minimum)
        odds.remove(closest)
        print(odds)
  
        
    return minWeightPM
#function PerfectMatching()
#   Input: odds (list of odd vertices), G (adjacency list)
#   while !odds.empty do
#     v <-- odds.popFront()
#     length <-- ∞
#     for u ∈ odds do
#       if weight(u,v) < length then
#         length <-- weight(u,v)
#         closest <-- u
#       end if
#     end for
#     G.addEdge(closest,v)
#     odds.remove(closest)
#   end while
# end function





def findOdds(g):
    oddVertices = []
    
    vertrices = g.vertices
    edges = g.edges

    counts = {} ##

    for v in vertrices:
        counts[v] = 0; 

    for v,u,w in edges:
        counts[v] += 1
        counts[u] += 1

    for v in counts:
        if(counts[v] %2 == 1):
            oddVertices.append(v)
    return oddVertices

def graphUnion(g1,g2):

    unionGraph = Graph()
   
    vertices1 = g1.vertices
    vertices2 = g2.vertices

    unionGraph.vertices=  g1.vertices
    

    for v,u,w in g1.edges:
        if((u,v) not in unionGraph.weights):
            unionGraph.addEdge(v,u,w)

    for v,u,w in g2.edges:
        if((u,v) not in unionGraph.weights):
            unionGraph.addEdge(v,u,w)
    return unionGraph
        
        

    

    
    



g= Graph()

g.addVertex("A",1,1)
g.addVertex("B",2,2)
g.addVertex("C",3,3)
g.addVertex("D",4,4)
g.addVertex("E",5,5)
# g.addVertex("F",2,1)
# g.addVertex("G",7,3)

g.addEdge("A","B",1)
g.addEdge("A","C",1)
g.addEdge("A","D",2)
g.addEdge("A","E",0)

g.addEdge("C","D",1)
g.addEdge("C","E",0)
g.addEdge("C","B",2)

g.addEdge("B","D",1)
g.addEdge("B","E",0)

g.addEdge("D","E",0)

# g.addEdge("A","D")
# g.addEdge("D","E")
# g.addEdge("B","D")
# g.addEdge("A","B")
# g.addEdge("F","E")
# g.addEdge("F","G")
# g.addEdge("G","E")
# g.addEdge("C","B")
# g.addEdge("B","E")
# g.addEdge("C","E")
# g.addEdge("F","D")

g.printGraph()

MST = KRUSKAL(g)
print
MST.printGraph()
print("------------------- Minimum weight --------------")
MWPM = mimumWeightPerfectMatching(g,MST)
MWPM.printGraph(); 
print("------------------- Union --------------")
uni = graphUnion(MWPM,MST)
uni.printGraph(); 


    