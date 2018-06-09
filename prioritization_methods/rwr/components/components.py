import networkx as nx
import pandas as pd 

G=nx.read_gpickle("HPRD-Biogrid.pkl")

seed_list=pd.read_csv("15_seed/diab_seed_list_15.txt",delim_whitespace="",header=None)

seed_genes=seed_list[0]

fp = open("result/seed_list_order.txt","wb")
for i in seed_genes:
	fp.write(i+"\n")

iteration = 0
while iteration<15:
	file=open("result/connected_components_"+str(iteration)+".txt","w")
	l= nx.node_connected_component(G,seed_genes[iteration])
	li = list(l)
	print str(len(li))+" "+seed_genes[iteration]
	for j in li:
		file.write(j+"\n")

	iteration+=1


