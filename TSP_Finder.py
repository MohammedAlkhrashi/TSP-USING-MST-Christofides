from Graph import Graph
import GraphAlgo
import random
import time 
# def main():
#     g = Graph(); 
#     fillGraph(g)

#     solve(g)



def solve(g,root):
    sol  = GraphAlgo.Christofides(g,root)
    return sol
    



def fillGraph():
    pass


def generate_random(size):
    randomGraph = Graph()
    for i in range(size):
        x = random.randint(10,600)
        y = random.randint(10,600)
        randomGraph.addVertex(randomGraph.getChar(i),x,y)
    
    for v in randomGraph.vertices:
        for i in range(size):
            u = randomGraph.getChar(i)
            if v is u:
                continue
            randomGraph.addEdge(v,u)

    return randomGraph

def test_data():
    size = 5
    for i in range(10):  ## test each graph 10 times.... to get average time 
        curGraph= generate_random(size)
        start = time.time()
        # solve(curGraph,)   ### 10 20 30 40 50 60 70 80 90 100 




g = generate_random(20);
print(solve(g,"A")); 


