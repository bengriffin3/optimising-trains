from collections import Counter
import pickle
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import colors

_NAMES = {'Manhattan': 'manhattan', 'Chengdu': 'chengdu'}
_X_MIN = 1
_X_MAX = 13
_Y_MIN = 0
_Y_MAX = 90
LEN = 2
FACTOR = 10


def barplot(data):
    bar_width = FACTOR / (_X_MAX - _X_MIN) / LEN
    for i, d in enumerate(data):
        c = Counter(d)
        plt.bar([x + i*bar_width for x in c.keys()], c.values(), width=bar_width)
        plt.xticks([r + bar_width/2 for r in range(_X_MIN, _X_MAX, 1)], range(_X_MIN, _X_MAX, 1))

def load_results(path):
    return pickle.load(open(path, 'rb'))


def histogram_degrees_in_cycles(results_, names):
    plt.figure()

    d = []
    for results in results_:
        G = results['network']
        cycles = [item for sublist in results['cycles'] for item in sublist]
        degrees = list(map(lambda x: G.degree[x], cycles))
        d.append(degrees)
        print(max(degrees))


    barplot(d)
    plt.legend(names)
    plt.title('Degree of Nodes in Critical Circuits')
    plt.xlabel('Degree of Nodes in Critical Circuits')
    plt.ylabel('Number of Nodes in Critical Circuits')

    plt.xlim((_X_MIN, _X_MAX))
    plt.ylim((_Y_MIN, _Y_MAX))

    plt.savefig('degrees_of_nodes_in_critical_circuits.svg')




def main():
    rm = load_results('../working_code/results/manhattan/manhattan.bin')
    rms = load_results('../working_code/results/manhattan/manhattan_split.bin')
    histogram_degrees_in_cycles([rm, rms], ['without Splitting', 'with Splitting'])


if __name__ == '__main__':
    main()
