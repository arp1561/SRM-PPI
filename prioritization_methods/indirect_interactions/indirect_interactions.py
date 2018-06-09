import pandas as pd
import networkx as nx
import sys
import os


def generate_seed_list(path):
    seed_list=[]
    try:
        fp = open(path)
    except IOError:
        sys.exit("Error opening seed file")

    for line in fp.readlines():
        info = line.rstrip().split()
        seed_list.append(info[0])
    fp.close()
    return seed_list

def generate_candidate_list(path):
    candidate_list=[]
    try:
        fp = open(path)
    except IOError:
        sys.exit("Error opening candidate list")
    for line in fp.readlines():
        info = line.rstrip().split()
        candidate_list.append(info)
    candidate_list=[x[0] for x in candidate_list]
    return candidate_list


fp = open("indirect_interactions_results/indirect_interactions_schizo.txt","w")
G = nx.Graph()
print "Opening Graph"
G = nx.read_gpickle("big_human_network_Graph.pkl")


seed_list=[]
candidate_list=[]

seed_list_path = "schizophrenia/seed_list.txt"
seed_list=generate_seed_list(seed_list_path)

candidate_list_path = "schizophrenia/seed_list.txt"
candidate_list=generate_candidate_list(candidate_list_path)

exception=0
correct =0
for seeds in seed_list:
    for candidates in candidate_list:
        try:
            shortest_path_list = nx.shortest_path(G,source=seeds,target=candidates)
            for i in range(0,(len(shortest_path_list)-1)):
                print shortest_path_list[i]+" "+shortest_path_list[i+1]
                fp.write(shortest_path_list[i]+","+shortest_path_list[i+1]+"\n")
                
                
        except nx.exception.NetworkXError:
            print "Seed ="+str(seeds)+" Candidate :"+str(candidates)
            exception+=1

print "Correct = "+str(correct)+" Exceptions ="+str(exception)
