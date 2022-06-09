import pickle
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl


def load_results(path):
    return pickle.load(open(path, 'rb'))


def save_figure(fig, path):
    fig.savefig(path)


def plot_lambda_decay(results, name):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
    fig = plt.figure()
    plt.plot(results['weights'])
    plt.title(f'Decay of $\\lambda$ in {name}')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')
    return fig


def main():
    path_results = sys.argv[1]
    path_figure = sys.argv[2]
    name = sys.argv[3]
    results = load_results(path_results)
    fig = plot_lambda_decay(results, name)
    save_figure(fig, path_figure)


if __name__ == '__main__':
    main()
