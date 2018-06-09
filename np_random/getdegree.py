import pandas as pd
import networkx as nx

data=pd.read_csv("noschizoseed.txt",delim_whitespace="",header=None)

seed=data[0]

g=nx.read_gpickle("SCHIZO_network.pkl")

dictionary=g.degree(seed)
txt_file=open("degrees.txt",'w')
for key in dictionary:
	txt_file.write(str(key)+","+str(dictionary[key])+"\n")

txt_file.close()

