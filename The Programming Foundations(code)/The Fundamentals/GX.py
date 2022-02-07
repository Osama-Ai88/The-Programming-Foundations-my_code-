# libraries
import ast
import random
import networkx as nx
import matplotlib.pyplot as plt

# Code Run
class Graph(object):
    def __init__(self, n_Node):

        self.graph = []
        self.n_Node = n_Node
        self.vertices = []
        self.wight = dict()
        self.n_Edge = []

        self.verf = []
        for i in range(self.n_Node):
            self.graph.append([0 for i in range(self.n_Node)])

    def Add_vertex(self, element):

        self.wight[element] = 0
        self.vertices.append(element)

    def Add_edge(self, v1, v2):

        self.n_Edge.append(1)

        if v1 not in self.vertices:
            print("the ", v1, " Node is not exists")

        if v2 not in self.vertices:
            print("the ", v2, " Node is not exists")

        else:

            row = self.vertices.index(v1)
            col = self.vertices.index(v2)

            self.verf.append([v1, v2])

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

            self.wight[self.verf[v][0]] += 1

        for Dedge in self.wight:

            print("The Vertex: ", Dedge, " the Degree of Node : ", self.wight[Dedge])

    def Degree_Edge_In(self):

        for v in range(len(self.verf)):

            self.wight[self.verf[v][1]] += 1

        for Dedge in self.wight:

            print("The Vertex: ", Dedge, " the Degree of Node : ", self.wight[Dedge])

    def Draw_Graph(self):

        GraphD = nx.DiGraph()
        for node in self.vertices:

            GraphD.add_node(node)

        for nodes in self.verf:
            L = [1, 2, 3, 4, 5]
            GraphD.add_edge(nodes[0], nodes[1], weight=random.choice(L))

        PX = nx.spring_layout(GraphD)

        nx.draw(
            GraphD,
            PX,
            with_labels=True,
            node_size=1500,
            node_color=["y", "r", "g", "b"],
        )

        nx.draw_networkx_edge_labels(
            GraphD,
            PX,
            font_size=25,
            edge_labels=nx.get_edge_attributes(GraphD, "weight"),
        )

        plt.show()

    def NumberOfNode(self):

        return self.n_Node

    def NumberOfEdge(self):

        return len(self.n_Edge)


# Open File and read The Input from it
FileGraph = open("inputGraph.txt", "r")


# convert text file to dictionary Data.
GraphDic = ast.literal_eval(FileGraph.read())

G1 = Graph(len(GraphDic))

# close File


# Add Nodes to space of adjacency matrix
for node in GraphDic:
    G1.Add_vertex(node)


for node in GraphDic:

    for Enode in GraphDic[node]:

        G1.Add_edge(node, Enode)


# output
print("The number of nodes: ", G1.NumberOfNode())
print("\n")
print("The number of edges: ", G1.NumberOfEdge())
print("\n")
G1.Degree_Edge_Out()
print("\n")
G1.Degree_Edge_In()
print("---------------------------------------------------------------")
G1.Draw_Graph()

# libraries
import ast
import random
import networkx as nx
import matplotlib.pyplot as plt

# Code Run
class Graph(object):
    def __init__(self, n_Node):

        self.graph = []
        self.n_Node = n_Node
        self.vertices = []
        self.wight = dict()
        self.n_Edge = []

        self.verf = []
        for i in range(self.n_Node):
            self.graph.append([0 for i in range(self.n_Node)])

    def Add_vertex(self, element):

        self.wight[element] = 0
        self.vertices.append(element)

    def Add_edge(self, v1, v2):

        self.n_Edge.append(1)

        if v1 not in self.vertices:
            print("the ", v1, " Node is not exists")

        if v2 not in self.vertices:
            print("the ", v2, " Node is not exists")

        else:

            row = self.vertices.index(v1)
            col = self.vertices.index(v2)

            self.verf.append([v1, v2])

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

            self.wight[self.verf[v][0]] += 1

        for Dedge in self.wight:

            print("The Vertex: ", Dedge, " the Degree of Node : ", self.wight[Dedge])

    def Degree_Edge_In(self):

        for v in range(len(self.verf)):

            self.wight[self.verf[v][1]] += 1

        for Dedge in self.wight:

            print("The Vertex: ", Dedge, " the Degree of Node : ", self.wight[Dedge])

    def Draw_Graph(self):

        GraphD = nx.DiGraph()
        for node in self.vertices:

            GraphD.add_node(node)

        for nodes in self.verf:
            L = [1, 2, 3, 4, 5]
            GraphD.add_edge(nodes[0], nodes[1], weight=random.choice(L))

        PX = nx.spring_layout(GraphD)

        nx.draw(
            GraphD,
            PX,
            with_labels=True,
            node_size=1500,
            node_color=["y", "r", "g", "b"],
        )

        nx.draw_networkx_edge_labels(
            GraphD,
            PX,
            font_size=25,
            edge_labels=nx.get_edge_attributes(GraphD, "weight"),
        )

        plt.show()

    def NumberOfNode(self):

        return self.n_Node

    def NumberOfEdge(self):

        return len(self.n_Edge)


# Open File and read The Input from it
FileGraph = open("inputGraph.txt", "r")


# convert text file to dictionary Data.
GraphDic = ast.literal_eval(FileGraph.read())

G1 = Graph(len(GraphDic))

# close File


# Add Nodes to space of adjacency matrix
for node in GraphDic:
    G1.Add_vertex(node)


for node in GraphDic:

    for Enode in GraphDic[node]:

        G1.Add_edge(node, Enode)


# output
print("The number of nodes: ", G1.NumberOfNode())
print("\n")
print("The number of edges: ", G1.NumberOfEdge())
print("\n")
G1.Degree_Edge_Out()
print("\n")
G1.Degree_Edge_In()
print("---------------------------------------------------------------")
G1.Draw_Graph()
