import pandas as pd
import networkx as nx
import argparse


def connect_to_target(list_of_candidate_genes): 
	'''
	In the network propagation algorithm the candidate genes are connected
	to the target node 't' with an infinite capacity of flow
	'''
	target=[]
	for i in range(len(list_of_candidate_genes)):
		target.append('t')
	target_gene_edges=zip(target,list_of_candidate_genes)
	dictionary={}
	
	for j in range(len(target_gene_edges)):
		key=target_gene_edges[j]
		dictionary[key]=1000000
		
		
	return target_gene_edges,dictionary


def add_candidates_to_network(list_of_candidate_genes,phenome_interactome):
	'''
	the candidate nodes can only be added to the network 
	after they have been connected to 't'
	'''
	target_gene_edges,dictionary=connect_to_target(list_of_candidate_genes)
	phenome_interactome.add_edges_from(target_gene_edges)
	nx.set_edge_attributes(phenome_interactome,'capacity',dictionary)
	
	return phenome_interactome


def calculate_maximum_flow(list_of_candidate_genes,phenome_interactome,iterations,path_to_save):
	'''
	the maximum flow value is equal to the min no of edges that have to be removed 
	to ensure that no flow is present in the network
	networkx uses the preflow_push algorithm to calculate the maximum flow
	'''

	final_network=add_candidates_to_network(list_of_candidate_genes,phenome_interactome)
	flow_value,flow_dict=nx.maximum_flow(final_network,155600,'t')
	cut_value,partition=nx.minimum_cut(final_network,155600,'t')
	write_flows(list_of_candidate_genes,flow_dict,phenome_interactome,iterations,path_to_save)

'''
phenome_interactome=nx.Graph()
phenome_interactome=nx.read_gpickle("maxif_network.pkl")
#used argparse to parse the arguments in the command line
parser=argparse.ArgumentParser(description="finding the maximum flow of candidate genes related to alzheimers")
parser.add_argument('filename',help="enter a .txt file containing the candidate genes in gene symbol format")
parser.add_argument('-v','--verbose',help="maximise verbosity",action="store_true")

args=parser.parse_args()

if args.filename:


	with open(args.filename) as file:
		candidate=args.filename

'''
'''
data=pd.read_csv(candidate,delim_whitespace="",header=None)
list_of_candidate_genes=data[0]
flow_dict=calculate_maximum_flow(list_of_candidate_genes,phenome_interactome)
'''
'''
candidate_genes=[]
list_of_flows=[]
'''
'''
displaying the maximum flow value corresponding to every candidate gene in descending order
the candidate gene with higher maximum flow value is ranked higher during prioritization
'''
def write_flows(list_of_candidate_genes,flow_dict,phenome_interactome,iterations,path_to_save):
	fp=open(path_to_save+str(iterations),'w')
	candidate_genes=[]
	list_of_flows=[]	
	for gene in list_of_candidate_genes:
		sum_all_flows=0
	
		candidate_gene=gene
	
		flows=flow_dict[candidate_gene]
	
		for gene in flows:
			
			sum_all_flows+=flows[gene]
			candidate_genes.append(candidate_gene)
			list_of_flows.append(sum_all_flows)

	ranking_list=zip(list_of_flows,candidate_genes)
	ranking_list.sort(reverse=True)
	for flow,candidategene in ranking_list:
		fp.write(str(candidategene)+","+str(float(flow)/10000000)+","+str(phenome_interactome.degree(candidategene)-1)+"\n")
	fp.close()

		
