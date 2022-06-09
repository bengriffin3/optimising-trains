#! /bin/bash

#plot original
#python3 plot_graph.py data/amsterdam/amsterdam.csv

#split network
python3 split_network.py data/amsterdam/amsterdam.csv data/amsterdam/amsterdam_split.csv 5

#plot splited
#python3 plot_graph.py data/amsterdam/amsterdam_split.csv

#add nodes
python3 add_nodes.py data/amsterdam/amsterdam.csv 20 results/amsterdam/amsterdam.bin

#write cycles
python3 print_cycles.py results/amsterdam/amsterdam.bin results/amsterdam/amsterdam.txt

#plot histograms
python3 degree_histogram.py results/amsterdam/amsterdam.bin figures/amsterdam/amsterdam_length.svg figures/amsterdam/amsterdam_degrees.svg amsterdam

#plot initial cycles
python3 initial_degree.py data/amsterdam/amsterdam.csv figures/amsterdam/amsterdam_initial_degrees.svg amsterdam

#plot lambda
python3 plot_lambda_decay.py results/amsterdam/amsterdam.bin figures/amsterdam/amsterdam_lambda.svg amsterdam

#save optimised network
python3 adj_matrix.py results/amsterdam/amsterdam.bin data/amsterdam/amsterdam_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/amsterdam/amsterdam_split.csv 20 results/amsterdam/amsterdam_split.bin

#write cycles for splitted network
python3 print_cycles.py results/amsterdam/amsterdam_split.bin results/amsterdam/amsterdam_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/amsterdam/amsterdam_split.bin figures/amsterdam/amsterdam_split_length.svg figures/amsterdam/amsterdam_split_degrees.svg amsterdam\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/amsterdam/amsterdam_split.csv figures/amsterdam/amsterdam_split_initial_degrees.svg amsterdam\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/amsterdam/amsterdam_split.bin figures/amsterdam/amsterdam_split_lambda.svg amsterdam\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/amsterdam/amsterdam_split.bin data/amsterdam/amsterdam_split_optimised.txt
