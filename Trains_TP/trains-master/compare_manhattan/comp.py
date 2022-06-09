import pickle
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_lambda_decay(results1, results2):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

    plt.plot(results1['weights']/results1['weights'][0])
    plt.plot(results2['weights']/results2['weights'][0])
    plt.title('Comparison of $\\lambda$ Decay')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')
    plt.legend(['Manhattan', 'Chengdu'])
    plt.savefig('comparison.svg')


def plot_lambda_decay_2(results1, results2, results3, results4):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

    plt.plot(results1['weights']/results1['weights'][0])
    plt.plot(results2['weights']/results1['weights'][0])
    plt.plot(results3['weights']/results3['weights'][0])
    plt.plot(results4['weights']/results3['weights'][0])

    plt.title('Comparison of $\\lambda$ Decay')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')
    plt.legend(['Manhattan', 'Manhattan after Splitting', 'Chengdu', 'Chengdu after Splitting'])
    plt.savefig('comparison_splitting.svg')


def main():
    dm =pickle.load(open('../working_code/results/manhattan/manhattan.bin', 'rb'))
    dc =pickle.load(open('../working_code/results/chengdu/chengdu.bin', 'rb'))
    dms =pickle.load(open('../working_code/results/manhattan/manhattan_split.bin', 'rb'))
    dcs =pickle.load(open('../working_code/results/chengdu/chengdu_split.bin', 'rb'))

    plot_lambda_decay_2(dm, dms, dc, dcs)



if __name__ == '__main__':
    main()
