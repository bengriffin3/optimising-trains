import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys


def read_graph(path):
    city = np.genfromtxt(path, delimiter=',')
    return nx.DiGraph(city)


def save_figure(fig, path):
    fig.savefig(path)


def histogram_degrees(G, name):
    degrees = list(map(lambda x: G.degree[x], G.nodes))
    fig = plt.figure()
    plt.hist(degrees, bins='auto')
    plt.title(f'Degree of Nodes in {name}')
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Number of Nodes')
    return fig


def main():
    path_graph = sys.argv[1]
    path_save = sys.argv[2]
    name = sys.argv[3]
    G = read_graph(path_graph)
    fig = histogram_degrees(G, name)
    save_figure(fig, path_save)


if __name__ == '__main__':
    main()
