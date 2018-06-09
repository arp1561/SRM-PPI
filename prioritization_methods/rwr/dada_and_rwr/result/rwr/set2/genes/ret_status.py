import pandas as pd
import networkx as nx



def ret_chars(seed,same_deg):
    G = nx.read_gpickle("HPRD-Biogrid.pkl")
    iteration=0
    num_occurences=0
    num_top10=0
    while iteration<=99: 
        path = "gene_"+str(iteration)+".txt"
        data = pd.read_csv(path,delim_whitespace="",header=None)
        seed_gene_list = data[0]
        same_deg_list = data[1]
        rank_list = data[2]
        for i in range(len(seed_gene_list)):
            if seed == seed_gene_list[i]:
                if same_deg == same_deg_list[i]:
                    num_occurences+=1
                    if rank_list[i]<=9:
                        num_top10+=1
        iteration+=1
                    
    return num_occurences,num_top10,G.degree(same_deg)






