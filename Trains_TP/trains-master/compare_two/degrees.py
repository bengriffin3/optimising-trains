from collections import Counter
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
_Y_MAX = 24
LEN = 2
FACTOR = 10


def barplot(data, color=colors):
    bar_width = FACTOR / (_X_MAX - _X_MIN) / LEN
    for i, (d, color_) in enumerate(zip(data, color)):
        c = Counter(d)
        plt.bar([x + i*bar_width for x in c.keys()], c.values(), width=bar_width, color=color_)
        plt.xticks([r + bar_width/2 for r in range(_X_MIN, _X_MAX, 1)], range(_X_MIN, _X_MAX, 1))


def read_graph(path):
    city = np.genfromtxt(path, delimiter=',')
    return nx.DiGraph(city)


def histogram_degrees(Gs, names):
    plt.figure()
    d = []
    for G in Gs:
        degrees = list(map(lambda x: G.degree[x], G.nodes))
        d.append(degrees)
        print(max(degrees))

    barplot(d, color=list(map(lambda x: colors.colors[_NAMES[x]], names)))
    plt.title('Histogram of Degrees before Splitting Stations')
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Number of Nodes')
    plt.xlim((_X_MIN, _X_MAX))
    plt.ylim((_Y_MIN, _Y_MAX))
    plt.legend(names)
    plt.savefig('comparison_of_initial_degrees.svg')


def histogram_degrees_2(Gs, names):
    plt.figure()
    d = []
    for G in Gs:
        degrees = list(map(lambda x: G.degree[x], G.nodes))
        d.append(degrees)
        print(max(degrees))

    barplot(d, color=list(map(lambda x: colors.colors[_NAMES[x]], names)))
    plt.title('Histogram of Degrees after Splitting Stations')
    plt.xlabel('Degree of Nodes')
    plt.ylabel('Number of Nodes')
    plt.xlim((_X_MIN, _X_MAX))
    plt.ylim((_Y_MIN, _Y_MAX))
    plt.legend(names)
    plt.savefig('comparison_of_initial_degrees_splitting.svg')


def main():
    Gm = read_graph('../working_code/data/manhattan/manhattan.csv')
    Gc = read_graph('../working_code/data/chengdu/chengdu.csv')
    Gms = read_graph('../working_code/data/manhattan/manhattan_split.csv')
    Gcs = read_graph('../working_code/data/chengdu/chengdu_split.csv')
    histogram_degrees([Gm, Gc], ['Manhattan', 'Chengdu'])
    histogram_degrees_2([Gms, Gcs], ['Manhattan', 'Chengdu'])


if __name__ == '__main__':
    main()
