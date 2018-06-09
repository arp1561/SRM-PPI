import networkx as nx
import pandas as pd

G = nx.Graph()
G = nx.read_gpickle("data/big_human_network_Graph.pkl") #input graph

data = pd.read_csv("data/candidate_list.txt",delim_whitespace="",header=None) #input file
data=data[0]
output_file = open("candidate_list_degrees.txt","w")
degrees=[]
tuple=()

for index in data:
    degrees.append(nx.degree(G,index))
    degree = nx.degree(G,index)
    output_file.write(str(index)+","+str(degree)+"\n")

