
import math

class Graph:


    def __init__(self):
        # self.adjMatrix = [[]]
        # self.V = {}
        # self.graph = {"vertices":{},"edges":set([]),"weights":{} }
        self.vertices = {}
        self.edges = set()
        self.weights = {}

    def addEdge(self,v,u,w=-1): 
        vertixV = self.vertices[v]; 
        vertixU = self.vertices[u]; 
        if(w==-1):
            weight = self.dist(vertixV,vertixU)
            self.edges.add((v,u,weight))
        else:
            weight = w 
            self.edges.add((v,u,w)) 

        self.weights[(u,v)] = weight; 
        self.weights[(v,u)] = weight; 
        
        

    def addVertex(self,name,x,y): ## each vertex is defined by (name,x,y).
 
        self.vertices[name] = (x,y) ## save each vertex by it's name as KEY, with value of x,y cooridnates. 
        # self.vertices.append(name)

    def dist(self,v,u):
        return math.sqrt( (v[0]-u[0])**2 + ( v[1]-u[1])**2 ) ## compute euclidean distance, because we have a metric graph. 
    
    def weight(self,v,u) :
        return self.weights[ (v,u) ]
       


    def printGraph(self):
        print("vertices = ",self.vertices)
        print("Edges = " , self.edges); 
        print("--------------------------------------------------------------------------------")

    def toMatrix(self):    
        gMatrix = {}
        adj =[]
        
        

        for v in self.vertices.keys():
            gMatrix[v] = {}
            for u in self.vertices.keys():
                if((v,u) not in self.weights):
                    gMatrix[v][u] = 0
                else:
                    gMatrix[v][u] = self.weights[(v,u)]

    
        edgesList = list(gMatrix.values())
        
        for i in edgesList:
            adj.append(list(i.values()))
        return adj , gMatrix; 

        
        




      

    def toGraph(self,adjMatrix):
        pass

# g = Graph()
# g.addVertex("A",2,2) 
# g.addVertex("B",3,5) 
# g.addVertex("C",5,8) 
# g.addVertex("D",2,1) 
# g.addVertex("F",11,5)

# g.addEdge("D",'F') 
# g.addEdge("C",'B')
# g.addEdge("A",'B')  
# g.addEdge("C",'A')
# g.addEdge("B",'D')
# g.addEdge("C",'F')
# g.addEdge("D",'C')
# g.addEdge("D",'A')

# g.printGraph(); 

# g.toMatrix(); 

# print("------------------------------------------------------------------")