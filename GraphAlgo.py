
from operator import itemgetter
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
import json

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


def Christofides(g,root):
    MST = KRUSKAL(g);     
    
    print("MST:")
    print(MST.printGraph())

    MWPM = mimumWeightPerfectMatching(g,MST); 

    print("MWPM")
    print(MWPM.printGraph())
    multiGraph = graphUnion(MST,MWPM)

    print("MultiGraph")
    print(multiGraph.edges())
    eulerianCircut = formEulerCircut(multiGraph,root); 
    print(eulerianCircut)
    hamlitonianCircut = formHamiltonianCircut(eulerianCircut)
    print(hamlitonianCircut)
    TSP_Graph = finalTSPgraph(hamlitonianCircut,g.weights)

    return TSP_Graph

def finalTSPgraph(hPath, weights):
    
    TSP_graph = nx.Graph();
    cost = 0; 

    for i in range(len(hPath)-1):
        v = hPath[i]
        u = hPath[i+1]
        w = weights[(u,v)]
        cost+= w; 
        TSP_graph.add_edge(hPath[i],hPath[i+1], weight = w)

    return TSP_graph,cost

def mimumWeightPerfectMatching(g,MST):
    odds = findOdds(MST)
    minWeightPM = Graph() ## minWeightPM : Mim Weight Perfect Matching
    minWeightPM.vertices = g.vertices
    minWeightPM.weights = g.weights
    while len(odds) > 0 :
        v = odds.pop()
        minimum = float("inf")
        for u in odds:
            if( (v,u) not in g.weights):
                continue; 
            if g.weight(v,u) < minimum:
                minimum = g.weight(v,u)
                closest = u
          
        minWeightPM.addEdge(closest,v,minimum)
        odds.remove(closest)
  
        
    return minWeightPM





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

    multiGraph = nx.MultiGraph();
    
    

    # multiGraph = Graph()
   
    vertices1 = g1.vertices
    vertices2 = g2.vertices
    

    for v,u,w in g1.edges:
            multiGraph.add_edge(v,u,weight = w)

    for v,u,w in g2.edges:
            multiGraph.add_edge(v,u,weight = w)
    
    # multiGraph.add_weighted_edges_from(g1.edges)
    # multiGraph.add_weighted_edges_from(g2.edges)
    # multiGraph.add_edge("B","D",weight = 11)
    return multiGraph

        
        
def formEulerCircut(multiGraph,root):

    curVertex = root; 
    stack = [curVertex]
    path = []
    while len(stack) != 0:
        
        curNeighbors = list(multiGraph.neighbors(curVertex)) ## Takes first neighbor as nextVertex 
        if (len(curNeighbors) == 0): ## if curVertex has no neighbouurs 
             path.append(curVertex)
             curVertex = stack.pop()
             continue;
        nextVertex = curNeighbors[0]; ## take first neighbor as nextVertex 
        multiGraph.remove_edge(curVertex,nextVertex)
        stack.append(curVertex)
        curVertex = nextVertex;
    
    return path; 
        

    

def formHamiltonianCircut(euler_path):

    TSP_path = []
    visted = set() 
    
    for v in euler_path:
        if(v not in visted):
            TSP_path.append(v)
            visted.add(v)

    TSP_path.append(TSP_path[0])

    return TSP_path
    

    
def readJson(inp):
    g = Graph()
    for v in inp["vl"]:
        print(v)
        g.addVertex(v,inp["vl"][v]["x"],inp["vl"][v]["y"])

    for v in  inp["vl"]:
        for u in inp["vl"]:
            if(u != v):
                g.addEdge(v,u)
    return g;



# g= Graph()

# g.addVertex("A",1,1)
# g.addVertex("B",2,2)
# g.addVertex("C",3,3)
# g.addVertex("D",4,4)
# g.addVertex("E",5,5)
# # g.addVertex("F",2,1)
# # g.addVertex("G",7,3)

# g.addEdge("A","B",1)
# g.addEdge("A","C",1)
# g.addEdge("A","D",2)
# g.addEdge("A","E",0)

# g.addEdge("C","D",1)
# g.addEdge("C","E",0)
# g.addEdge("C","B",2)

# g.addEdge("B","D",1)
# g.addEdge("B","E",0)

# g.addEdge("D","E",0)

# # g.addEdge("A","D")
# # g.addEdge("D","E")
# # g.addEdge("B","D")
# # g.addEdge("A","B")
# # g.addEdge("F","E")
# # g.addEdge("F","G")
# # g.addEdge("G","E")
# # g.addEdge("C","B")
# # g.addEdge("B","E")
# # g.addEdge("C","E")
# # g.addEdge("F","D")

# g.printGraph()


# MST = KRUSKAL(g)
# MST.printGraph()
# print("------------------- Minimum weight --------------")
# MWPM = mimumWeightPerfectMatching(g,MST)
# MWPM.printGraph(); 
# print("------------------- Union --------------")
# uni = graphUnion(MWPM,MST)

# print([ (u,v,edata['weight']) for u,v,edata in uni.edges(data=True) if 'weight' in edata ])

# # for u,v,edata in uni.edges(data =True):
# #     print((u,v,edata))


# eulerPath = formEulerCircut(uni,"E")
# print("This is euler path" , eulerPath)

# # uni.printGraph();   

# # gMatrix = g.toMatrix()[1]
# # tester.minimum_weight_matching(MST.toMatrix[1],gMatrix,findOdds(MST));


# # nx.draw_circular(uni,with_labels = True); 
# # plt.savefig("multi.png")

# print("This is uni", uni.edges);

# TSP_path = hamlitonianCircut(eulerPath)
# print(TSP_path)

# adjMatrix = [[0 ,5 ,8 ,4 ,5],
#             [5 ,0 ,7 ,4 ,5],
#             [8 ,7 ,0 ,8 ,6],
#             [4 ,4 ,8 ,0 ,8],
#             [5 ,5 ,6 ,8 ,0]]
# g = toGraph(adjMatrix)
# g.printGraph()




# inp ={"vl":{"0":{"x":260,"y":20},"1":{"x":60,"y":300},"2":{"x":560,"y":280},"3":{"x":100,"y":80},"4":{"x":480,"y":100},"5":{"x":60,"y":200},"6":{"x":380,"y":300},"7":{"x":300,"y":60}},"el":{}}

# g = readJson(inp)

# sol,cost = Christofides(g,"0"); 
# nx.draw_circular(sol,with_labels = True);     
# plt.savefig("sol.png")
# print(sol); 
# print(cost); 

