import networkx as nx
import time
import pandas as pd



G = nx.read_gpickle("HPRD-Biogrid.pkl")
seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list = seed_list[0]

analysis = pd.read_csv("set2_analysis.txt",delim_whitespace="",header=None)
seed_gene = analysis[0]
deg_match = analysis[2]
num_occurences = analysis[4]
num_top10 = analysis[5]

seed_gene_list = []
deg_match_list = []
num_occurences_list = []
top10_list = []

for seed in seed_list:
    temp_seed = []
    temp_deg_match = []
    temp_occur = []
    temp_top10 = []
    
    for i in range(len(analysis)):
        if seed_gene[i] == seed:
            temp_deg_match.append(deg_match[i])
            temp_occur.append(num_occurences[i])
            temp_top10.append(num_top10[i])


    deg_match_list.append(temp_deg_match)
    num_occurences_list.append(temp_occur)
    top10_list.append(temp_top10)

shortest_path = []
shortest_path_lengths = []


for i in range(len(deg_match_list)):
    seed = seed_list[i]
    temp_list = deg_match_list[i]
    temp_spath = []
    temp_spath_length = []
    print seed
    for j in range(len(temp_list)):
        print temp_list[j]
        
        x = nx.shortest_path(G,source=str(seed),target=str(temp_list[j]))
        temp_spath_length.append(len(x))
        temp_spath.append(x)
        
    shortest_path.append(temp_spath)
    shortest_path_lengths.append(temp_spath_length)
print shortest_path_lengths
