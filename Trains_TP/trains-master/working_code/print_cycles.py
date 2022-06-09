import pickle
import sys


def load_results(path):
    return pickle.load(open(path, 'rb'))


def save_cycles(results, path):
    print('\n'.join(str(x) for x in results['cycles']), file=open(path, 'w'))


def main():
    path_results = sys.argv[1]
    path_cycles = sys.argv[2]
    results = load_results(path_results)
    save_cycles(results, path_cycles)


if __name__ == '__main__':
    main()
