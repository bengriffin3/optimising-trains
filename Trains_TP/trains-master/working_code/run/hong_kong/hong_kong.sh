#! /bin/bash

#plot original
#python3 plot_graph.py data/hong_kong/hong_kong.csv

#split network
python3 split_network.py data/hong_kong/hong_kong.csv data/hong_kong/hong_kong_split.csv 5

#plot splited
#python3 plot_graph.py data/hong_kong/hong_kong_split.csv

#add nodes
python3 add_nodes.py data/hong_kong/hong_kong.csv 20 results/hong_kong/hong_kong.bin

#write cycles
python3 print_cycles.py results/hong_kong/hong_kong.bin results/hong_kong/hong_kong.txt

#plot histograms
python3 degree_histogram.py results/hong_kong/hong_kong.bin figures/hong_kong/hong_kong_length.svg figures/hong_kong/hong_kong_degrees.svg Hong Kong

#plot initial cycles
python3 initial_degree.py data/hong_kong/hong_kong.csv figures/hong_kong/hong_kong_initial_degrees.svg Hong Kong

#plot lambda
python3 plot_lambda_decay.py results/hong_kong/hong_kong.bin figures/hong_kong/hong_kong_lambda.svg Hong Kong

#save optimised network
python3 adj_matrix.py results/hong_kong/hong_kong.bin data/hong_kong/hong_kong_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/hong_kong/hong_kong_split.csv 20 results/hong_kong/hong_kong_split.bin

#write cycles for splitted network
python3 print_cycles.py results/hong_kong/hong_kong_split.bin results/hong_kong/hong_kong_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/hong_kong/hong_kong_split.bin figures/hong_kong/hong_kong_split_length.svg figures/hong_kong/hong_kong_split_degrees.svg Hong Kong\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/hong_kong/hong_kong_split.csv figures/hong_kong/hong_kong_split_initial_degrees.svg Hong Kong\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/hong_kong/hong_kong_split.bin figures/hong_kong/hong_kong_split_lambda.svg Hong Kong\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/hong_kong/hong_kong_split.bin data/hong_kong/hong_kong_split_optimised.txt
