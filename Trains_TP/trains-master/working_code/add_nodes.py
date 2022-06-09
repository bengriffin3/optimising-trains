import pickle
import sys
import networkx as nx
import numpy as np
import copy


def read_graph(path):
    city = np.genfromtxt(path, delimiter=',')
    return nx.DiGraph(city)


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


def update_cycles_from_edge(G, edge, cycles, edges_cycles):
    u, v = list(G.edges)[edge]
    edges_index = list(filter(lambda x: edge in x[1], enumerate(edges_cycles)))
    for index in map(lambda x: x[0], edges_index):
        pos = cycles[index].index(u)
        cycles[index].insert(pos + 1, len(G))



def update(G, cycles, n):
    cycles_edges = list(map((lambda x: cycle_to_edges(G, x)), cycles))
    best_edge = optimal_edge(cycles_edges[0], cycles_edges[1:n+1], G)
    update_cycles_from_edge(G, best_edge, cycles, cycles_edges)
    add_node_on_edge(G, best_edge)


def save_results(results, path):
    with open(path, 'wb') as f:
        pickle.dump(results, f)


def add_nodes(G, n):
    max_lambda = np.zeros([n])
    bigest_cycles = []

    cycles = list(nx.simple_cycles(G))

    for i in range(n):
        print(i)
        cycles.sort(reverse=True, key=lambda x:
                (lambda a: a[0]/a[1])(weight(x, G)))
        bigest_cycles.append(copy.deepcopy(cycles[0]))
        max_lambda[i] = (lambda x: (lambda a: a[0]/a[1])(weight(x, G)))(cycles[0])
        update(G, cycles, n)

    results = {'cycles': bigest_cycles, 'network': G, 'weights': max_lambda}
    return results


def main():
    path_graph = sys.argv[1]
    n = int(sys.argv[2])
    path_save =sys.argv[3]
    save_results(add_nodes(read_graph(path_graph), n), path_save)


if __name__ == '__main__':
    main()
