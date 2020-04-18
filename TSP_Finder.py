import Graph
import GraphAlgo

def main():
    g = Graph(); 
    fillGraph(g)

    solve(g)



def solve(g):
    gMST = GraphAlgo.KRUSKAL(g) ## Convert to MST using KRUSKAL
    sol  = GraphAlgo.Christofides(gMST); 
    



def fillGraph():
    pass



