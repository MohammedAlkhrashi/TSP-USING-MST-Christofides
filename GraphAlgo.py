
def union(parent,v,u):
    parentV = findParent(v)
    parentU = findParent(u) ##
    if parentV != parentU:
        parent[parentU] = parentV ## No matter who will be the parent (Xd) , see findParent() and draw the graph to be clear
    

def findParent(parent,v):

    if parent[v] != v :
        return findParent(parent[v])
    else:
        return v

def KRUSKAL(graph):
    parent = {} 
    MST = set()
    for v in graph["vertices"]:
        parent[v] = v #MAKE - SET (v)
    
    edges =list(graph["edges"])
    edges.sort(key=itemgetter(2)) ## by w - > (v,u,w) 
    
    for v,u,w in edges:
        if findParent(v) != findParent(u):
            MST.add((v,u,w))
            union(v,u)

    return MST



    
def if __name__ == "__main__":
    main(); 
