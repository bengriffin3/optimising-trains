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
_Y_MAX = 14
LEN = 2
FACTOR = 10


def barplot(data, color=colors):
    bar_width = FACTOR / (_X_MAX - _X_MIN) / LEN
    for i, (d, color_) in enumerate(zip(data, color)):
        c = Counter(d)
        plt.bar([x + i*bar_width for x in c.keys()], c.values(), width=bar_width, color=color_)
        plt.xticks([r + bar_width/2 for r in range(_X_MIN, _X_MAX, 1)], range(_X_MIN, _X_MAX, 1))


def load_results(path):
    return pickle.load(open(path, 'rb'))


def histogram_length_of_cycles(results_, names):
    plt.figure()
    d = []
    for results in results_:
        cycles_length = list(map(len, results['cycles']))
        d.append(cycles_length)
        print(max(cycles_length))

    barplot(d, color=list(map(lambda x: colors.colors[_NAMES[x]], names)))

    plt.legend(names)
    plt.title('Length of Critical Circuits without Splitting')
    plt.xlabel('Length of Critical Circuits')
    plt.ylabel('Number of Critical Circuits')
    plt.xlim((_X_MIN, _X_MAX))
    plt.ylim((_Y_MIN, _Y_MAX))

    plt.savefig('length_of_critical_circuits.svg')


def histogram_length_of_cycles_2(results_, names):
    plt.figure()
    d = []
    for results in results_:
        cycles_length = list(map(len, results['cycles']))
        d.append(cycles_length)
        print(max(cycles_length))

    barplot(d, color=list(map(lambda x: colors.colors[_NAMES[x]], names)))

    plt.legend(names)
    plt.title('Length of Critical Circuits with Splitting')
    plt.xlabel('Length of Critical Circuits')
    plt.ylabel('Number of Critical Circuits')
    plt.xlim((_X_MIN, _X_MAX))
    plt.ylim((_Y_MIN, _Y_MAX))

    plt.savefig('length_of_critical_circuits_splitting.svg')


def main():
    rm = load_results('../working_code/results/manhattan/manhattan.bin')
    rc = load_results('../working_code/results/chengdu/chengdu.bin')
    rms = load_results('../working_code/results/manhattan/manhattan_split.bin')
    rcs = load_results('../working_code/results/chengdu/chengdu_split.bin')
    histogram_length_of_cycles([rm, rc], ['Manhattan', 'Chengdu'])
    histogram_length_of_cycles_2([rms, rcs], ['Manhattan', 'Chengdu'])

if __name__ == '__main__':
    main()
