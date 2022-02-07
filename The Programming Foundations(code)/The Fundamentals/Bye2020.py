# Osama Alessa
# 2019901021


# Liabires
import ast
import random
import networkx as nx
import matplotlib.pyplot as plt

# Code Run


class Graph(object):
    def __init__(self, NumberOfNode):

        self.graph = []
        self.NumberOfNode = NumberOfNode
        self.vertices = []
        self.wight = dict()

        self.verf = []
        for i in range(self.NumberOfNode):
            self.graph.append([0 for i in range(self.NumberOfNode)])

    def Add_vertex(self, element):

        self.wight[element] = 0
        self.vertices.append(element)

    def Add_edge(self, v1, v2):

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
        for i in range(self.NumberOfNode):
            for j in range(self.NumberOfNode):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j])
                    # print(" edge weight for Node : ", self.vertices[i], self.wight[self.vertices[i]])

    def print_edge(self):

        for i in range(len(self.verf)):

            print(self.verf[i], end=",")

    def Degree_Edge(self):
        print("Degree of each vertex")
        print()
        for v in range(len(self.verf)):

            self.wight[self.verf[v][0]] += 1

        for Dedge in self.wight:

            print("The Vertex: ", Dedge,
                  "a Degree of Node : ", self.wight[Dedge])

    def Draw_Graph(self):

        GraphD = nx.Graph()
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
G1.print_graph()
print()
G1.Degree_Edge()
print()
G1.Draw_Graph()

print("---------------------------------------------------------------")
# ----------------------------------------------------------------------
# # input
# print("--"*30)
# G1 = Graph(6)

# G1.Add_vertex('A')
# G1.Add_vertex('B')
# G1.Add_vertex('C')
# G1.Add_vertex('D')
# G1.Add_vertex('E')
# G1.Add_vertex('F')

# # link between nodes

# # G1.Add_edge('A', 'C')
# # G1.Add_edge('B', 'C')
# G1.Add_edge('C', 'A')
# G1.Add_edge('C', 'B')
# G1.Add_edge('C', 'D')


# # output
# G1.print_graph()
# print()
# G1.Degree_Edge()
# print()
# G1.Draw_Graph()
