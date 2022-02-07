




# libraries
import ast
import random
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Code Run
class Graph(object):
    
    
    def __init__(self, n_Node):

        self.graph = []
        self.n_Node = n_Node
        self.vertices = []
        self.inDeg = dict()
        self.outDeg=dict()
        self.n_Edge=[]
        
        self.visited = set()
        self.verf = []
        for i in range(self.n_Node):
            self.graph.append([0 for i in range(self.n_Node)])

    def Add_vertex(self, element):
        
        self.inDeg[element]=0
        self.outDeg[element]=0
        
        self.vertices.append(element)
        

    def Add_edge(self, v1, v2,w):
        
        self.n_Edge.append(1)
        
        if v1 not in self.vertices:
            print("the ", v1, " Node is not exists")

        if v2 not in self.vertices:
            print("the ", v2, " Node is not exists")

        else:

            row = self.vertices.index(v1)
            col = self.vertices.index(v2)            
            self.verf.append([v1, v2,w])

            self.graph[row][col] = 1
            self.graph[col][row] = 1
            
            
            
            
            
            
            
         
            

    def print_graph(self):
        print("Relationships between the vertices")
        print()
        for i in range(self.n_Node):
            for j in range(self.n_Node):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j])




    def print_edge(self):

        for i in range(len(self.verf)):

            print(self.verf[i], end=",")
            
            

    def Degree_Edge_Out(self):
        
        
        for v in range(len(self.verf)):

           self.outDeg[self.verf[v][0]] += 1
           
           
      
        for Dedge in self.outDeg:
          
           print("The Vertex: ", Dedge, " the Degree of Node : ", self.outDeg[Dedge])
        
    def Degree_Edge_In(self):
        
        
       for v in range(len(self.verf)):

          self.inDeg[self.verf[v][1]] += 1
          
          
     
       for Dedge in self.inDeg:
         
          print("The Vertex: ", Dedge, " the Degree of Node : ", self.inDeg[Dedge])
             
            

         
    
    def Longest_Path(self):
        
        
        G1= nx.DiGraph()
        
        G1 = nx.read_edgelist("Graphtext.txt",create_using=nx.DiGraph())
        
        print("The longest path of length: ",nx.dag_longest_path_length(G1))

        print("The longest Path :")
        
        for i in  nx.dag_longest_path(G1):
            
            print(i,end="-->")
            
            
       
        
        
        
     
       
                
        
        
        
        
            
            
    
    def Draw_Graph(self):

        GraphD = nx.DiGraph()
       
        for nodes in self.verf:
            
            GraphD.add_edge(nodes[0], nodes[1],weight=nodes[2])
        
        

        PX = nx.spring_layout(GraphD)

        nx.draw(
            GraphD,
            PX,
            with_labels=True,
            node_size=600,
            node_color="Green",
        )

        nx.draw_networkx_edge_labels(
            GraphD,
            PX,
            font_size=8,
            edge_labels=nx.get_edge_attributes(GraphD, "weight"),
        )
        
        plt.show()
        
        

    def NumberOfNode(self):

        return self.n_Node
    
    def NumberOfEdge(self):
        
    
        
        return len(self.n_Edge)
    
    
   

    def DFS(self,ele):
        
        
        FGraph= open("inputGraph.txt", "r")    
        GraphList = ast.literal_eval(FGraph.read())
        
        def dfs(adjacencyList, vertex, visitedSet = None, path = None):
            
            if visitedSet is None:
                visitedSet = set()
            if path is None:
                path = []
                
            visitedSet.add(vertex)
            path.append(vertex)
            if vertex in adjacencyList:
                for neighbor in adjacencyList[vertex]:
                    if neighbor not in visitedSet:
                        dfs(adjacencyList, neighbor, visitedSet, path)
            return path
        
        L=dfs(GraphList,ele)
        
        for i in L:
            
            print(i,end=" --> ")
            
            
    def BFS(self,ele):
        
         
        FGraph= open("inputGraph.txt", "r")    
        GraphList = ast.literal_eval(FGraph.read())
        
        visited = [] 
        queue = []    
        def bfs(visited, graph, node): #function for BFS
          visited.append(node)
          queue.append(node)
          while queue:          # Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " --> ") 

            for neighbour in graph[m]:
              if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
                
        bfs(visited,GraphList,ele)
        
    
    
    def Draw_DFS(self,ele):
        
        
        GraphDFS= nx.DiGraph()
        
        GraphDFS= nx.read_edgelist("Graphtext.txt",create_using=nx.DiGraph())
       
        
        DFS=nx.depth_first_search.dfs_tree(GraphDFS,ele)
        
       
    
        nx.draw(DFS,with_labels=True,node_size=600,node_color='yellow')
        
        plt.show()
    
    def Draw_BFS(self,ele):
        
        
        GraphBFS= nx.DiGraph()
        
        GraphBFS= nx.read_edgelist("Graphtext.txt",create_using=nx.DiGraph())
        
        
        BFS=nx.breadth_first_search.bfs_tree(GraphBFS,ele)
        plt.Figure()

        
        nx.draw(BFS,with_labels=True,node_size=600,node_color='blue')
        
        
        plt.show()
        
    def MST(self):
        
        
        
        mst = []
        usedVertices= set()

        with open("GraphtextWL.txt") as F:
            
    

            Number_Of_Vertices = 6
    
    
    
            edges=[ [] for i in range(Number_Of_Vertices)]
    
   
    
            for line in F.readlines():

                edge = tuple(map(int,line.split(" ")))
        
        
                if edge[0]==edge[1]:continue
        
        
                heapq.heappush(edges[edge[0]],(edge[2],edge[1]))
                heapq.heappush(edges[edge[1]],(edge[2],edge[0]))
        
        cost,dest= 0,1

    
        while len(usedVertices)<Number_Of_Vertices:
            
            verticesSmall = 0 
    
            for vertex in usedVertices:
        
                while(len(edges[vertex]) > 0 and edges[vertex][0][dest] in usedVertices ):
            
                    heapq.heappop(edges[vertex])
            
        
                if len(edges[vertex])==0:continue
        
        
                if len(edges[verticesSmall])==0 or edges[vertex][0][cost] <  edges[verticesSmall][0][cost]:
            
            
                    verticesSmall = vertex
            
    

            edge = heapq.heappop(edges[verticesSmall])

            mst.append((verticesSmall ,edge[dest],edge[cost]))
    

            usedVertices.add(verticesSmall)
            usedVertices.add(edge[dest])
            
        
        for item in mst:
            
            print("The Vertex  ",item[0]," With the Vertex  ",item[1], " Cost: ",item[2])
        
        
    


       
        
     
        
        
    def Draw_MST(self):
        
       
        GraphMST= nx.DiGraph()
        
        GraphMST= nx.read_weighted_edgelist("GraphtextWL.txt",delimiter=" ")

     
        MST=nx.minimum_spanning_tree(GraphMST)
        
        plt.Figure()
        
        PX = nx.spring_layout(GraphMST)
    
        plt.subplot(121)
        
        nx.draw(GraphMST,PX,with_labels=True,node_size=600,node_color="yellow",)
        
        nx.draw_networkx_edge_labels(
            GraphMST,
            PX,
            font_size=9,
            edge_labels=nx.get_edge_attributes(GraphMST, "weight"),
        )
        
        plt.subplot(122)
        nx.draw(MST,with_labels=True,node_size=600, node_color="r")
        
        plt.show()


       
    
    

      
    
    
    
#===================================================================
# Open File and read The Input from it


#1.	Read a Graph from a file
FileGraph = open("inputGraph.txt", "r")


# convert text file to dictionary Data .
GraphDic = ast.literal_eval(FileGraph.read())
G1 = Graph(len(GraphDic))




# Add Nodes to space of adjacency matrix
for node in GraphDic:
    G1.Add_vertex(node)


for node in GraphDic:
   
    for Enode in GraphDic[node]:
        
        G1.Add_edge(node, Enode,GraphDic[node][Enode])
       



#===================================================================
# output-----------------------------------------------
#
#2.Draw the input Graph


print("---------------------------------------------------------------\n")

#3.	The number of nodes
print("The number of nodes: ",G1.NumberOfNode())
print("\n")

#4.	The number of edges
print("The number of edges: ",G1.NumberOfEdge())
print("\n")

#5.	The node degree for each node
print("The Number degree out for each node")
G1.Degree_Edge_Out()
print("\n")
print("The Number degree in for each node")
G1.Degree_Edge_In()

print("---------------------------------------------------------------")


#6.	The Diameter of the network (longest path length
G1.Longest_Path()
print()
print("----------------------------")


#7.Apply DFS (Depth First search).
print("This is  Depth First Search traversal from starting vertex")
print()
G1.DFS("B")

print("\n")
#--------------------------------------------------------------
#8.	Apply BFS (Breadth First search).
print("This is  breadth-first search traversal from starting vertex")
print()
G1.BFS("B")

#9.	Find the MST(Minimum Spanning Tree).
print("\n\n")
print(" the  Minimum Spanning Tree for each Nodes")
G1.MST()

#Draws of the Graphs
print("#"*30)
print("The Draws ")
G1.Draw_Graph()

G1.Draw_DFS("B")


G1.Draw_BFS("B")

#
G1.Draw_MST()

