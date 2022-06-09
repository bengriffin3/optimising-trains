import matplotlib.pyplot as plt
import pickle
import sys


def load_results(path):
    return pickle.load(open(path, 'rb'))


def save_figure(fig, path):
    fig.savefig(path)


def histogram_length_of_cycles(results, name):
    cycles_length = list(map(len, results['cycles']))
    fig = plt.figure()
    plt.hist(cycles_length, bins='auto')
    plt.title(f'Length of Critical Circuits in {name}')
    plt.xlabel('Length of Critical Circuits')
    plt.ylabel('Number of Critical Circuits')
    return fig


def histogram_degrees_in_cycles(results, name):
    G = results['network']
    cycles = [item for sublist in results['cycles'] for item in sublist]
    degrees = list(map(lambda x: G.degree[x], cycles))
    fig = plt.figure()
    plt.hist(degrees, bins='auto')
    plt.title(f'Degree of Nodes in Critical Circuits in {name}')
    plt.xlabel('Degree of Nodes in Critical Circuits')
    plt.ylabel('Number of Nodes in Critical Circuits')
    return fig


def main():
    path_results = sys.argv[1]
    path_save_length = sys.argv[2]
    path_save_degrees = sys.argv[3]
    name = sys.argv[4]
    results = load_results(path_results)
    fig = histogram_length_of_cycles(results, name)
    save_figure(fig, path_save_length)
    fig = histogram_degrees_in_cycles(results, name)
    save_figure(fig, path_save_degrees)


if __name__ == '__main__':
    main()
