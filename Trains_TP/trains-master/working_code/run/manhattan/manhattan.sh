#! /bin/bash

#plot original
#python3 plot_graph.py data/manhattan/manhattan.csv

#split network
python3 split_network.py data/manhattan/manhattan.csv data/manhattan/manhattan_split.csv 10

#plot splited
#python3 plot_graph.py data/manhattan/manhattan_split.csv

#add nodes
python3 add_nodes.py data/manhattan/manhattan.csv 20 results/manhattan/manhattan.bin

#write cycles
python3 print_cycles.py results/manhattan/manhattan.bin results/manhattan/manhattan.txt

#plot histograms
python3 degree_histogram.py results/manhattan/manhattan.bin figures/manhattan/manhattan_length.svg figures/manhattan/manhattan_degrees.svg Manhattan

#plot initial cycles
python3 initial_degree.py data/manhattan/manhattan.csv figures/manhattan/manhattan_initial_degrees.svg Manhattan

#plot lambda
python3 plot_lambda_decay.py results/manhattan/manhattan.bin figures/manhattan/manhattan_lambda.svg Manhattan

#save optimised network
python3 adj_matrix.py results/manhattan/manhattan.bin data/manhattan/manhattan_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/manhattan/manhattan_split.csv 20 results/manhattan/manhattan_split.bin

#write cycles for splitted network
python3 print_cycles.py results/manhattan/manhattan_split.bin results/manhattan/manhattan_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/manhattan/manhattan_split.bin figures/manhattan/manhattan_split_length.svg figures/manhattan/manhattan_split_degrees.svg Manhattan\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/manhattan/manhattan_split.csv figures/manhattan/manhattan_split_initial_degrees.svg Manhattan\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/manhattan/manhattan_split.bin figures/manhattan/manhattan_split_lambda.svg Manhattan\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/manhattan/manhattan_split.bin data/manhattan/manhattan_split_optimised.txt
