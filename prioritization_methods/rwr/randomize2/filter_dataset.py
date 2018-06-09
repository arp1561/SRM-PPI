import pandas as pd
import networkx as nx

G=nx.read_gpickle("HPRD-Biogrid.pkl")

#candidate_list_temp =pd.read_csv("input_data/temp_candidate_list_low_degree.txt",delim_whitespace="",header=None)
#candidate_list_temp = candidate_list_temp[0]

seed_list_temp = pd.read_csv("input_data/parkinsons/seed_set.txt",delim_whitespace="",header=None)
seed_list_temp=seed_list_temp[0]



#candidate_file = open("input_data/candidate_list_low_degree.txt","w")
seed_file = open("input_data/parkinsons/filtered_seed_list.txt","w")

'''
can_present=0
can_not_present=0
for candidate in candidate_list_temp:
	if G.has_node(candidate) == True:
		can_present+=1
		candidate_file.write(str(candidate)+"\n")
	else:
		can_not_present+=1


print str(can_present)+" "+str(can_not_present)
'''

seed_present=0
seed_not_present=0

for seed in seed_list_temp:
	if G.has_node(seed) == True:
		seed_present+=1
		seed_file.write(str(seed)+"\n")
	else:
		seed_not_present+=1
print str(seed_present)+" "+str(seed_not_present)

