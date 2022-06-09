import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def weight(k, london):
    return sum(london_distance[k[i-1], k[i]] for i in range(len(k)))/len(k)

london = np.genfromtxt('london_matr.txt', delimiter=',')
london_distance = deepcopy(london)
london[london == -np.infty] = 0
london[london != 0] = 1
G = nx.DiGraph(london)
cycles = nx.simple_cycles(G)
max_cycle = max(cycles, key=lambda k: weight(k, london))

print(max_cycle)
print(weight(max_cycle, london))

colors = ['blue' if n in max_cycle else 'red' for n in G]
nx.draw(G, node_color=colors)
plt.show()

