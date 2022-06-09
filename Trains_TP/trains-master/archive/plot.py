import networkx as nx
import pickle
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def weight(k, G):
    return [sum(G.get_edge_data(k[i-1], k[i])['weight'] for i in range(len(k))), len(k)]

def cycle_to_edges(G, cycle):
    edges = []
    for ndx in range(len(cycle)):
        edges.append(list(G.edges).index(((cycle[ndx-1], cycle[ndx]))))
    return edges

def edge_get_weight(G, e):
    u, v =list(G.edges)[e]
    return G.get_edge_data(u, v)['weight']

def optimal_edge(max_cycle, all_cycles, G):
    all_cycles = [item for sublist in all_cycles for item in sublist]
    return max(max_cycle, key=lambda x: (all_cycles.count(x), edge_get_weight(G, x)))

def add_node_on_edge(G, edge):
    n = G.number_of_nodes()
    G.add_node(n)
    u, v = list(G.edges)[edge]
    w = G.get_edge_data(u, v)['weight']
    G.remove_edge(u, v)
    G.add_edge(u, n, weight=0)
    G.add_edge(n, v, weight=w)


def plot(path, n):
    city = np.genfromtxt(path, delimiter=',')

    G = nx.DiGraph(city)
    max_lambda = np.zeros([n])

    bigest_cycles = []

    for i in range(n):
        cycles = nx.simple_cycles(G)
        cycles = list(cycles)
        cycles.sort(reverse=True, key=lambda x:
                (lambda a: a[0]/a[1])(weight(x, G)))

        bigest_cycles.append(cycles[0])

        max_lambda[i] = (lambda x: (lambda a: a[0]/a[1])(weight(x, G)))(cycles[0])

        cycles_edges = list(map((lambda x: cycle_to_edges(G, x)), cycles))

        best_edge = optimal_edge(cycles_edges[0], cycles_edges[1:n+1], G)
        add_node_on_edge(G, best_edge)

    np.savetxt('output.csv', np.array(max_lambda), delimiter=',')
    histogram_results = {'cycles': bigest_cycles, 'network': G,
            'weights': max_lambda}

    with open('histogram_results.txt', 'wb') as f:
        pickle.dump(histogram_results, f)

plot('manhattan.csv', 100)
