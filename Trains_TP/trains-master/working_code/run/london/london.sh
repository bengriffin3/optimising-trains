#! /bin/bash

#plot original
#python3 plot_graph.py data/london/london.csv

#split network
python3 split_network.py data/london/london.csv data/london/london_split.csv 10

#plot splited
#python3 plot_graph.py data/london/london_split.csv

#add nodes
python3 add_nodes.py data/london/london.csv 20 results/london/london.bin

#write cycles
python3 print_cycles.py results/london/london.bin results/london/london.txt

#plot histograms
python3 degree_histogram.py results/london/london.bin figures/london/london_length.svg figures/london/london_degrees.svg London

#plot initial cycles
python3 initial_degree.py data/london/london.csv figures/london/london_initial_degrees.svg London

#plot lambda
python3 plot_lambda_decay.py results/london/london.bin figures/london/london_lambda.svg London

#save optimised network
python3 adj_matrix.py results/london/london.bin data/london/london_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/london/london_split.csv 20 results/london/london_split.bin

#write cycles for splitted network
python3 print_cycles.py results/london/london_split.bin results/london/london_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/london/london_split.bin figures/london/london_split_length.svg figures/london/london_split_degrees.svg London\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/london/london_split.csv figures/london/london_split_initial_degrees.svg London\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/london/london_split.bin figures/london/london_split_lambda.svg London\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/london/london_split.bin data/london/london_split_optimised.txt
