import pandas as pd
import networkx as nx
from rwr import Walker

candidate_list_temp = pd.read_csv("candidate_list.txt",delim_whitespace="",header=None)
candidate_list_temp = candidate_list[0]
candidate_list_one = random.sample(candidate_list_temp,98)
candidate_list_two = ['DRD4','DAO']

candidate_list = candidate_list_one+candidate_list_two

seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list = seed_list[0]

G = nx.read_gpickle("HPRD-Biogrid.pkl")
rprob = 0.1
wk = Walker(G)
while rprob<1.0:
    print rprob
    wk.run_walker(seed_list,rprob,candidate_list,"result/rprob_",rprob)
    rprob+=0.1
