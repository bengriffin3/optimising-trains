import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sys


def read_graph(path):
    city = np.genfromtxt(path, delimiter=',')
    return nx.DiGraph(city)


def plot_network(G):
    nx.draw(G)
    plt.show()


def main():
    path_graph = sys.argv[1]
    G = read_graph(path_graph)
    plot_network(G)


if __name__ == '__main__':
    main()
