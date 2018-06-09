import pandas as pd
import networkx as nx

candidate_file=pd.read_csv("candidate.txt",delim_whitespace="",header=None)
seed_file=pd.read_csv("seed.txt",delim_whitespace="",header=None)

candidate_list=candidate_file[0]
seed_list=seed_file[0]

G=nx.Graph()
G=nx.read_gpickle("human1_network")
list_sum=[]
for i in range(len(candidate_list)):
	sum_dist=0
	for j in range(len(seed_list)):
		try:
			avg_dist=nx.shortest_path_length(G,source=candidate_list[i],target=seed_list[j])
			sum_dist+=avg_dist
		except nx.exception.NetworkXError:
			sum_dist+=0
	average_shortest_distance=(sum_dist/len(seed_list))
	list_sum.append(sum_dist)
dictionary_deg={}
dictionary_deg=G.degree(candidate_list)
list_degree=[]

for key in dictionary_deg:
	list_degree.append(dictionary_deg[key])

candidate_list_deg=zip(list_degree,candidate_list)
candidate_list_deg.sort(reverse=True)
print "the degree"
for deg,gene in candidate_list_deg:
	print gene,deg
print "the distance"	
candidate_list_dist=zip(list_sum,candidate_list)
candidate_list_dist.sort()

for dist,gene in candidate_list_dist:
	
	print gene,float(dist)

print "in betweeness centrality"

dictionary_central={}

dictionary_central=nx.betweenness_centrality_subset(G,candidate_list,seed_list)
print dictionary_central
'''
except KeyError:
	dictionary_central['nan']="Not Found"
for key in dictionary_central:
	print key,dictionary_central[key]
'''
