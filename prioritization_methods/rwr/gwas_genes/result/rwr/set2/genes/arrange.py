import os
import pandas as pd
import networkx as nx
import ret_status as rs

G = nx.read_gpickle("HPRD-Biogrid.pkl")
seed_list =pd.read_csv("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/gwas_genes/gwas_genes_filtered.txt",delim_whitespace="",header=None)
seed_list = seed_list[0]

similar_genes = []
for node in seed_list:
    iteration = 0
    temp_list = []
    while iteration<=99:
        path = "gene_"+str(iteration)+".txt"
        gene_file = pd.read_csv(path,delim_whitespace="",header=None)
        for i in range(len(gene_file)):
            if node == gene_file[0][i]:
                temp_list.append(gene_file[1][i])
        iteration+=1
    temp_list = set(temp_list)
    temp_list = list(temp_list)
    similar_genes.append(temp_list)

fp = open("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/gwas_genes/result/rwr/set2/set2_analysis.txt","wb")
for i in range(len(seed_list)):
    fp.write(seed_list[i]+";"+str(G.degree(seed_list[i]))+";")
    temp_list = similar_genes[i]
    num_occurences = 0
    num_top10=0
    for j in range(len(temp_list)):
        print seed_list[i]+" "+temp_list[j]
        a,b,c = rs.ret_chars(seed_list[i],temp_list[j])
        fp.write(temp_list[j]+"("+str(c)+")"+",")
        print str(a)+" "+str(b)+" "+str(c)
        num_occurences+=a
        num_top10+=b
    fp.seek(-1, os.SEEK_CUR)
    fp.write(";")
#    del_last()
    fp.write(str(num_occurences)+";"+str(num_top10)+"\n")
fp.close()
