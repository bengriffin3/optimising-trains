from collections import Counter
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import pickle



def plot(path):
    city = np.genfromtxt(path, delimiter=',')

    G = nx.DiGraph(city)

    cycles = nx.simple_cycles(G)
    cycles = [int(item)+1 for sublist in cycles for item in sublist]
    plt.hist(cycles, bins='auto')
    plt.show()


def histogram(path):
    d = pickle.load(open(path, 'rb'))

    cycles_length = list(map(len, d['cycles']))
    plt.hist(cycles_length, bins='auto')
    plt.show()


    G = d['network']
    cycles = [item for sublist in d['cycles'] for item in sublist]
    degrees = list(map(lambda x: G.degree[x], cycles))


    plt.figure(2)
    plt.hist(degrees, bins='auto')
    plt.show()


#plot('manhattan.csv')
histogram('histogram_results.txt')
#manhattan
#london
#chengdu

#roterdam
#amsterdam
#hong kong

#degree distribution
#degree distribution and histogram
