import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

A = [
    [0.000000, 0.0000000, 0.0000000, 0.0000000, 0.05119703, 1.3431599],
    [0.000000, 0.0000000, -0.6088082, 0.4016954, 0.00000000, 0.6132168],
    [0.000000, -0.6088082, 0.0000000, 0.0000000, -0.63295415, 0.0000000],
    [0.000000, 0.4016954, 0.0000000, 0.0000000, -0.29831267, 0.0000000],
    [0.051197, 0.0000000, -0.6329541, -0.2983127, 0.00000000, 0.1562458],
    [1.343159, 0.6132168, 0.0000000, 0.0000000, 0.15624584, 0.0000000],
]

G = nx.from_numpy_matrix(np.array(A))
nx.draw(G, with_labels=True)
plt.show()
