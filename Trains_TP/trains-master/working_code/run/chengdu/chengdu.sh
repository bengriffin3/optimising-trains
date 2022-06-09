#! /bin/bash

#plot original
#python3 plot_graph.py data/chengdu/chengdu.csv

#split network
python3 split_network.py data/chengdu/chengdu.csv data/chengdu/chengdu_split.csv 10

#plot splited
#python3 plot_graph.py data/chengdu/chengdu_split.csv

#add nodes
python3 add_nodes.py data/chengdu/chengdu.csv 20 results/chengdu/chengdu.bin

#write cycles
python3 print_cycles.py results/chengdu/chengdu.bin results/chengdu/chengdu.txt

#plot histograms
python3 degree_histogram.py results/chengdu/chengdu.bin figures/chengdu/chengdu_length.svg figures/chengdu/chengdu_degrees.svg Chengdu

#plot initial cycles
python3 initial_degree.py data/chengdu/chengdu.csv figures/chengdu/chengdu_initial_degrees.svg Chengdu

#plot lambda
python3 plot_lambda_decay.py results/chengdu/chengdu.bin figures/chengdu/chengdu_lambda.svg Chengdu

#save optimised network
python3 adj_matrix.py results/chengdu/chengdu.bin data/chengdu/chengdu_optimised.txt

#add nodes for splitted network
python3 add_nodes.py data/chengdu/chengdu_split.csv 20 results/chengdu/chengdu_split.bin

#write cycles for splitted network
python3 print_cycles.py results/chengdu/chengdu_split.bin results/chengdu/chengdu_split.txt

#plot histograms for splitted network
python3 degree_histogram.py results/chengdu/chengdu_split.bin figures/chengdu/chengdu_split_length.svg figures/chengdu/chengdu_split_degrees.svg Chengdu\ with\ Splitting

#plot initial cycles for splitted network
python3 initial_degree.py data/chengdu/chengdu_split.csv figures/chengdu/chengdu_split_initial_degrees.svg Chengdu\ with\ Splitting

#plot lambda for splitted network
python3 plot_lambda_decay.py results/chengdu/chengdu_split.bin figures/chengdu/chengdu_split_lambda.svg Chengdu\ with\ Splitting

#save optimised splitted network
python3 adj_matrix.py results/chengdu/chengdu_split.bin data/chengdu/chengdu_split_optimised.txt
