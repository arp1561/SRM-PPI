import time
import pandas as pd
import networkx as nx
import sys
import os
import random
import threading
from threading import Thread
from rwr import Walker



#95 random + 5 disease associated
def set1(main_seed_list,candidate_list_one,candidate_list_two,G,iterations):
    print "Set 1..."

    #path where to save the scores
    path_to_save = "result/set1/scores/rwr_result_set1_" 
    
    #creating the candidate list
    candidate_list = candidate_list_one + candidate_list_two
    #creating seed list after filtering out the 5 genes from the main seed list
    seed_list = [x for x in candidate_list_two if x not in main_seed_list]

    print "Will now run RWR"
    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iterations)
    print "Successfully run RWR and saved scores\n Will now save the 5 genes"
    
    #for saving the 5 disease associated genes
    fp = open("result/set1/genes/gene_"+str(iterations)+".txt","w")
    for i in candidate_list_two:
        fp.write(i+"\n")
    
    
    print "Done saving now returning"
    return

def set2(main_seed_list,all_nodes,candidate_list_one,candidate_list_two,G,iterations):
    print "Set 2..."
    path_to_save = "result/set2/scores/rwr_result_set2_"
    
    
    print "Selecting same degree nodes"
    
    same_degree_nodes=[]
    while len(same_degree_nodes)<5:
        node = random.choice(all_nodes)
        for i in main_seed_list:
            if G.degree(node)==G.degree(i):
                same_degree_nodes.append(node)
                break
    print "Got the same degree nodes"
    candidate_list=candidate_list_one+same_degree_nodes
    seed_list = [x for x in same_degree_nodes if x not in main_seed_list]
    print "Got candidate list and seed list\n Will now run RWR"

    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iterations)

    print "Successfully run RWR and saved scores\n Will now save the 5 genes"

    fp = open("result/set2/genes/gene_"+str(iterations)+".txt","w")
    for i in same_degree_nodes:
        fp.write(i+"\n")
    print "Done saving now returning"



def set3(main_seed_list,all_nodes,candidate_list_one,G,iterations):
    print "Set 3..."
    path_to_save = "result/set3/scores/rwr_result_set3_"

    print "selecting random genes"

    candidate_list_two = random.sample(all_nodes,5)
    candidate_list = candidate_list_one+candidate_list_two
    seed_list = [x for x in candidate_list_two if x not in main_seed_list]

    print "Will now run RWR"

    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iterations)

    print "Successfully run RWR and saved scores\n Will now save the 5 genes"

    fp = open("result/set3/genes/gene_"+str(iterations)+".txt","w")

    for i in candidate_list_two:
        fp.write(i+"\n")

    print "Done saving now returning"






if __name__=="__main__":
    G = nx.read_gpickle("HPRD-Biogrid.pkl")
    all_nodes_temp = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
    all_nodes_temp = all_nodes_temp[0]
    main_seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    main_seed_list = main_seed_list[0]
    all_nodes = [node for node in all_nodes_temp if node not in main_seed_list]
    


    iterations=0
    while iterations<100:
        candidate_list=[]
        candidate_list_one = random.sample(all_nodes,95)
        candidate_list_two = random.sample(main_seed_list,5)

       # set1(main_seed_list,candidate_list_one,candidate_list_two,G,iterations)
        set2(main_seed_list,all_nodes,candidate_list_one,candidate_list_two,G,iterations)
        #set3(main_seed_list,all_nodes,candidate_list_one,G,iterations)
        
        
        print "iteration = "+str(iterations+1) 
    
    
        iterations +=1
