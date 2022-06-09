import pickle
import sys
import numpy as np
import networkx as nx


def load_results(path):
    return pickle.load(open(path, 'rb'))


def save_adj_matrix(adj, path):
    np.savetxt(path, adj, delimiter=',', fmt='%d')


def get_adj_matrix(results):
    return nx.to_numpy_matrix(results['network'])


def main():
    path_results = sys.argv[1]
    path_matrix = sys.argv[2]
    results = load_results(path_results)
    adj = get_adj_matrix(results)
    save_adj_matrix(adj, path_matrix)


if __name__ == '__main__':
    main()
