import pickle
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import colors

_NAMES = {'Manhattan': 'manhattan', 'Chengdu': 'chengdu', 'London': 'london', 'Rotterdam': 'rotterdam', 'Amsterdam': 'amsterdam', 'Hong Kong': 'hong_kong'}

def plot_lambda_decay(results_, names):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']


    for results, name in zip(results_, names):
        plt.plot(results['weights']/results['weights'][0], color=colors.colors[_NAMES[name]], label=name)

    plt.ylim((0, 1.05))

    handles, _ = plt.gca().get_legend_handles_labels()
    #for name in names:
    #    empty_patch = mpatches.Patch(color='none', label=f'{name} with Splitting')
    #    handles.append(empty_patch)

    plt.title(r'Comparison of the Decay of $\lambda$')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')

    leg = plt.legend(handles=handles)

    for text in leg.get_texts():
        if 'Splitting' in text.get_text():
            plt.setp(text, alpha=0)

    plt.savefig('decay_comparison_of_two_networks.svg')


def plot_lambda_decay_2(results_, names):
    mpl.rcParams['text.usetex'] = True
    mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

    for results, name in zip(results_, names):
        plt.plot(results[0]['weights']/results[0]['weights'][0], color=colors.colors[_NAMES[name]], label=name)
        plt.plot(results[1]['weights']/results[0]['weights'][0], color=colors.colors[_NAMES[name]], linestyle=':')#, label=f'{name} with Splitting')

    plt.ylim((0, 1.05))

    plt.title(r'Comparison of the Decay of $\lambda$')
    plt.xlabel('Number of Trains Added')
    plt.ylabel(r'$\lambda$')
    plt.legend()
    plt.savefig('decay_comparison_of_two_networks_with_splitting.svg')


def main():
    dm = pickle.load(open('../working_code/results/manhattan/manhattan.bin', 'rb'))
    dl = pickle.load(open('../working_code/results/london/london.bin', 'rb'))
    dc = pickle.load(open('../working_code/results/chengdu/chengdu.bin', 'rb'))
    da = pickle.load(open('../working_code/results/amsterdam/amsterdam.bin', 'rb'))
    dr = pickle.load(open('../working_code/results/rotterdam/rotterdam.bin', 'rb'))
    dh = pickle.load(open('../working_code/results/hong_kong/hong_kong.bin', 'rb'))
    dms = pickle.load(open('../working_code/results/manhattan/manhattan_split.bin', 'rb'))
    dls = pickle.load(open('../working_code/results/london/london_split.bin', 'rb'))
    dcs = pickle.load(open('../working_code/results/chengdu/chengdu_split.bin', 'rb'))
    das = pickle.load(open('../working_code/results/amsterdam/amsterdam_split.bin', 'rb'))
    drs = pickle.load(open('../working_code/results/rotterdam/rotterdam_split.bin', 'rb'))
    dhs = pickle.load(open('../working_code/results/hong_kong/hong_kong_split.bin', 'rb'))

    plot_lambda_decay([dl, dc, dh, dm, dr, da], ['London', 'Chengdu', 'Hong Kong', 'Manhattan', 'Rotterdam', 'Amsterdam'])
    plot_lambda_decay_2([(dl, dls), (dc, dcs), (dh, dhs), (dm, dms), (dr, drs), (da, das)], ['London', 'Chengdu', 'Hong Kong', 'Manhattan', 'Rotterdam', 'Amsterdam'])


if __name__ == '__main__':
    main()
