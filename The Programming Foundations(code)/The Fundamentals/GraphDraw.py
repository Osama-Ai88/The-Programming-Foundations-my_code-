# libraries
import ast
import random
import networkx as nx
import matplotlib.pyplot as plt


G1 = nx.Graph()




G1 = nx.read_edgelist("Graphtext.txt",create_using=nx.DiGraph())
# G1 = nx.read_edgelist("InputGraph.txt",create_using=nx.DiGraph())
print(G1.number_of_nodes())




print(G1.number_of_edges())

DFS= nx.depth_first_search.dfs_tree(G1,"C")

nx.draw(DFS, with_labels=True,node_color="g")

plt.figure()


Bfs = nx.breadth_first_search.bfs_tree(G1,"C")

nx.draw(Bfs, with_labels=True,node_color="y")

plt.figure()

nx.draw(G1, with_labels=True)


plt.figure()



G1 = nx.read_weighted_edgelist("GraphtextW.txt",delimiter=" ")


MST = nx.minimum_spanning_tree(G1)
plt.Figure()

plt.subplot(121)
nx.draw(MST,with_labels=True,node_size=600, node_color="r")

plt.subplot(122)

nx.draw(G1,with_labels=True,node_size=600, node_color="y")

plt.show()