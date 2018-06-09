import pandas as pd
import random 
import networkx as nx
from network_propagation import calculate_maximum_flow


def set1(candidate_list1,candidate_list2,NP_Graph,iterations):
	print "running for set 1...."
	path_to_save="result/set1/scores/with_seed"
	final_candidate_list=candidate_list1+candidate_list2
	calculate_maximum_flow(final_candidate_list,NP_Graph,iterations,path_to_save)
	path_to_save1="result/set1/genes/with_seed"
	fp=open(path_to_save1+str(iterations),'w')
	for gene in candidate_list2:
		fp.write(str(gene)+"\n")
	
	fp.close()


def set2(candidate_list1,candidate_list2,NP_graph,G,all_nodes,iterations):
	print "running  for set 2....."	
	path_to_save="result/set2/scores/same_degree"
	path_to_save1="result/set2/genes/same_degree"
	same_degree_nodes=[]	
	for i in candidate_list2:
		for j in all_nodes:
			if G.degree(i)==G.degree(j):
				same_degree_nodes.append(j)
				break

	final_candidate_list=candidate_list1+same_degree_nodes
	calculate_maximum_flow(final_candidate_list,NP_Graph,iterations,path_to_save)
	fp=open(path_to_save1+str(iterations),'w')
	for gene in same_degree_nodes:
		fp.write(str(gene)+"\n")
		
	fp.close()



def set3(candidate_list1,all_nodes,NP_Graph,iterations):
	print "running for set 3...."
	path_to_save="result/set3/scores/random_nodes"
	path_to_save1="result/set3/scores/random_nodes"
	random_node_list=random.sample(all_nodes,5)
	final_candidate_list=candidate_list1+random_node_list
	calculate_maximum_flow(final_candidate_list,NP_Graph,iterations,path_to_save)
	fp=open(path_to_save1,'w')
	for gene in random_node_list:
		fp.write(str(gene)+"\n")
	fp.close()


	

all_nodes_data=pd.read_csv("noschizo.txt",delim_whitespace="",header=None)
seed_genes_data=pd.read_csv("noschizoseed.txt",delim_whitespace="",header=None)


G=nx.read_gpickle("HPRD-Biogrid.pkl")
NP_Graph=nx.read_gpickle("SCHIZO_network.pkl")
all_nodes=all_nodes_data[0]
seed_set=seed_genes_data[0]
iterations=0

while iterations<100:

	candidate_list1=random.sample(all_nodes,95)
	candidate_list2=random.sample(seed_set,5)
	print "Running Network propagation..."
	set1(candidate_list1,candidate_list2,NP_Graph,iterations)
	set2(candidate_list1,candidate_list2,NP_Graph,G,all_nodes,iterations)
	set3(candidate_list1,all_nodes,NP_Graph,iterations)
	iterations=iterations+1
