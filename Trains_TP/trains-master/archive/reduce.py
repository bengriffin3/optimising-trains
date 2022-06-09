import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx

def reduce(path, central, distance, save_path):
    df = pd.read_excel(path)
    df = df.iloc[3:-2]
    A = df.values
    A[A != A] = 0

    central_node = [v[0] for v in A].index(central)
    A = A[:, 2:-1]
    A = [[int(a) for a in r] for r in A]
    A = np.array(A)
    A = 1/2 * (A + A.T)
    G = nx.DiGraph(A)

    paths = nx.all_pairs_dijkstra(G)
    paths = (list(paths)[central_node][1][0])

    to_remove = [k for k in paths.keys() if paths[k] > distance]
    for n in to_remove:
        G.remove_node(n)

    A = nx.to_numpy_matrix(G)
    A = np.ceil(A/60)
    A = A.astype(int)

    np.savetxt(save_path, A, delimiter=",")


reduce('new_york.xlsx', '96 st', .75*60*60, 'manhattan.csv')
