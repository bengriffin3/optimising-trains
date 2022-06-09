import pickle
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import colors

_NAMES = {'Manhattan': 'manhattan', 'Chengdu': 'chengdu'}


def plot_lambda_decay(results_, names):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

    for results, name in zip(results_, names):
        plt.plot(results[0]['weights']/results[0]['weights'][0], label=name)
        plt.plot(results[1]['weights']/results[0]['weights'][0], label=f'{name} with Splitting')

    plt.ylim((0, 1.05))

    plt.title(r'Comparison of the Decay of $\lambda$')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')
    plt.legend()
    plt.savefig('decay_comparison_of_two_networks_with_splitting.svg')


def main():
    dm = pickle.load(open('../working_code/results/manhattan/manhattan.bin', 'rb'))
    dms = pickle.load(open('../working_code/results/manhattan/manhattan_split.bin', 'rb'))

    plot_lambda_decay([(dm, dms)], ['Manhattan'])


if __name__ == '__main__':
    main()
