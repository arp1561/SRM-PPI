import pandas as pd
import networkx as nx
import random

G = nx.read_gpickle("HPRD-Biogrid.pkl")

all_nodes = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
all_nodes =  all_nodes[0]

seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list = seed_list[0]

deg_matched=[]
degree = []


for node1 in seed_list:
    for node2 in all_nodes:
        if G.degree(node1) == G.degree(node2):
            #print node1+" "+str(G.degree(node1))+" "+node2+" "+str(G.degree(node2))
            deg_matched.append(node2)
            degree.append(G.degree(node2))
            break



fp = open("degree_matched_genes.txt","w")
for i in range(len(seed_list)):
    fp.write(seed_list[i]+","+deg_matched[i]+","+str(degree[i])+"\n")
