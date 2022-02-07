# Osama Alessa
# 2019901021


# Liabires
import ast
import random


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
            # self.graph[col][row] = 1

    def print_graph(self):

        for v in range(len(self.verf)):

            self.wight[self.verf[v][0]] += 1

        for i in range(self.NumberOfNode):
            for j in range(self.NumberOfNode):
                if self.graph[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j])
                    # print(" edge weight for Node : ", self.vertices[i], self.wight[self.vertices[i]])

    def print_edge(self):

        for i in range(len(self.verf)):

            print(self.verf[i], end=",")

    def DrwaGraph(self):

        pass


# Open File and read The Input from it
FileGraph = open("inputGraph.txt", "r")


G1 = Graph(6)


# convert text file to dictionary Data.
GraphDic = ast.literal_eval(FileGraph.read())


print(GraphDic)
# close File
FileGraph.close()

# Add Node to space of adjacency matrix
# for node in GraphDic:
#     G1.Add_vertex(node)


# for node in GraphDic:

#     for Enode in GraphDic[node]:

#         G1.Add_edge(node, Enode)


# for node in GraphDic:

#     for EdgeNode in range(len(node)):

#         # G1.Add_edge(node,GraphDic[node[EdgeNode]])

#         print(GraphDic[node[0]])


# # output
G1.print_graph()


# G1.print_edge()

# foo = ['A', 'B', 'C', 'D', 'E',"D"]
# print(random.choice(foo))
# Add edge
# for r in range(len(L)):

#     G1.Add_edge(L[r][0], L[r][1])


# output Graph

# G1.print_graph()
# G1.print_edge()

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

# G1.Add_edge('A', 'C')
# G1.Add_edge('B', 'C')
# G1.Add_edge('C', 'A')
# G1.Add_edge('C', 'B')
# G1.Add_edge('C', 'D')


# # output
# G1.print_graph()
# G1.print_edge()
