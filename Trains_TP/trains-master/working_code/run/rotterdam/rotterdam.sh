#! /bin/bash

#plot original
#python3 plot_graph.py data/rotterdam/rotterdam.csv

#split network
python3 split_network.py data/rotterdam/rotterdam.csv data/rotterdam/rotterdam_split.csv 5

#plot splited
#python3 plot_graph.py data/rotterdam/rotterdam_split.csv

#add nodes
python3 add_nodes.py data/rotterdam/rotterdam.csv 20 results/rotterdam/rotterdam.bin

#write cycles
python3 print_cycles.py results/rotterdam/rotterdam.bin results/rotterdam/rotterdam.txt

#plot histograms
python3 degree_histogram.py results/rotterdam/rotterdam.bin figures/rotterdam/rotterdam_length.svg figures/rotterdam/rotterdam_degrees.svg Rotterdam

#plot initial cycles
python3 initial_degree.py data/rotterdam/rotterdam.csv figures/rotterdam/rotterdam_initial_degrees.svg Rotterdam

#plot lambda
python3 plot_lambda_decay.py results/rotterdam/rotterdam.bin figures/rotterdam/rotterdam_lambda.svg Rotterdam

#save optimised network
python3 adj_matrix.py results/rotterdam/rotterdam.bin data/rotterdam/rotterdam_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/rotterdam/rotterdam_split.csv 20 results/rotterdam/rotterdam_split.bin

#write cycles for splitted network
python3 print_cycles.py results/rotterdam/rotterdam_split.bin results/rotterdam/rotterdam_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/rotterdam/rotterdam_split.bin figures/rotterdam/rotterdam_split_length.svg figures/rotterdam/rotterdam_split_degrees.svg Rotterdam\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/rotterdam/rotterdam_split.csv figures/rotterdam/rotterdam_split_initial_degrees.svg Rotterdam\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/rotterdam/rotterdam_split.bin figures/rotterdam/rotterdam_split_lambda.svg Rotterdam\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/rotterdam/rotterdam_split.bin data/rotterdam/rotterdam_split_optimised.txt
