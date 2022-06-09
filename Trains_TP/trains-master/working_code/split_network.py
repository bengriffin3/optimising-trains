import networkx as nx
import numpy as np
import sys


def read_graph(path):
    city = np.genfromtxt(path, delimiter=',')
    return nx.DiGraph(city)


def save_graph(G, path):
    A = nx.to_numpy_matrix(G)
    np.savetxt(path, A, delimiter=',', fmt='%d')


def split_stations(G, n):
    for _ in range(n):
        index = max(G.nodes, key=lambda x: G.degree[x])
        edges_in = [(x, G.get_edge_data(x[0], x[1])['weight']) for x in G.in_edges(index)]
        edges_out = [(x, G.get_edge_data(x[0], x[1])['weight']) for x in G.out_edges(index)]

        edges_in.sort(key=lambda x: x[1])
        edges_out.sort(key=lambda x: x[1], reverse=True)

        edges = [v for pair in zip(edges_in, edges_out) for v in pair]

        partial_edges = edges[:len(edges)//2]

        node = len(G)
        G.add_node(node)

        for edge in partial_edges:
            G.remove_edge(edge[0][0], edge[0][1])
            u, v = (node, edge[0][1]) if index == edge[0][0] else (edge[0][0], node)
            G.add_edge(u, v, weight=edge[1])

    return G


def main():
    path_graph = sys.argv[1]
    path_save = sys.argv[2]
    n = int(sys.argv[3])
    G = read_graph(path_graph)
    G = split_stations(G, n)
    save_graph(G, path_save)


if __name__ == '__main__':
    main()
