import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import distances


def load_city(path, city):
    return pd.read_excel(pd.ExcelFile(path), city)

def plot_graph(city):
    df = city.iloc[3:-2]
    df = df.drop(df.columns[[0, 1,-1]], axis=1)

    A = df.values
    A[A!=A] = 0

    G = nx.DiGraph(A)
    print(list(nx.simple_cycles(G)))
    nx.draw(G)
    plt.show()

def compute_distances(city, city_name):
    df = city.iloc[3:-2]
    for index, row in df.iterrows():
        source = row[0]
        for station, connection in enumerate(row[2:-1]):
            if connection == 1:
                destination = df.iloc[station][0]
                dist = distances.distance(source, destination, city_name)
                print(source, destination, dist)
                city.set_value(index, city.columns[[station+2]], dist)

    return city

def main():
    new_york = load_city('adjacency.xls', 'NewYork')
    plot_graph(new_york)
    #new_york_distances = compute_distances(new_york, 'New York, NY')
    #new_york_distances.to_excel('new_york.xlsx')

main()
