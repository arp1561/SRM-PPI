import thread
import math
import select_random_genes as sr
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

    #path where to save the scores
    path_to_save = "result/rwr/set1/scores/rwr_result_set1_" 
    
    #creating the candidate list
    candidate_list = candidate_list_one + candidate_list_two
    #creating seed list after filtering out the 5 genes from the main seed list
    
    seed_list=[]
    for i in main_seed_list:
        flag = False
        for j in candidate_list:
            if i == j:
                flag = True
                break
        if flag == False:
            seed_list.append(i)

    print "Will now run RWR for set1"
    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iterations)
    print "Successfully run RWR and saved scores\n Will now save the 5 genes for set1"
    
    #for saving the 5 disease associated genes
    fp = open("result/rwr/set1/genes/gene_"+str(iterations)+".txt","w")
    for i in candidate_list_two:
        fp.write(i+"\n")
    
    
    print "Done saving now returning for set1"
    return

def set2(main_seed_list,candidate_list_one,candidate_list_two,hist_seed_list,G,iterations):
    path_to_save = "result/rwr/set2/scores/rwr_result_set2_"
    
    candidate_list = candidate_list_one+candidate_list_two
    same_degree_nodes = candidate_list_two
    print "Got candidate list and seed list\n Will now run RWR for set2"

    wk = Walker(G)
    wk.run_walker(main_seed_list,0.7,candidate_list,path_to_save,iterations)

    ranks = []
    for z in same_degree_nodes:
        flag=False
        result_file = pd.read_csv("result/rwr/set2/scores/rwr_result_set2_"+str(iterations)+".txt",delim_whitespace="",header=None)
        result_file = list(result_file[0])
        for i in range(len(result_file)):
            if z == result_file[i]:
                flag=True
                break
        if flag == True:
            ranks.append(i)



    print "Successfully run RWR and saved scores\n Will now save the 5 genes for set2"

    fp = open("result/rwr/set2/genes/gene_"+str(iterations)+".txt","w")
    

    for i in range(len(same_degree_nodes)):
        fp.write(hist_seed_list[i]+","+same_degree_nodes[i]+","+str(ranks[i])+"\n")

    fp.close()
    print "Done saving now returning for set2"

    
if __name__=="__main__":
    G = nx.read_gpickle("edge_swapped_graph.pkl")
    all_nodes_temp = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
    all_nodes_temp = list(all_nodes_temp[0])
    main_seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    main_seed_list = list(main_seed_list[0])
    all_nodes = [node for node in all_nodes_temp if node not in main_seed_list]
    


    iterations=0
    while iterations<100:
        candidate_list=[]
        candidate_list_one = random.sample(all_nodes,95)
        candidate_list_two = random.sample(main_seed_list,5)
        candidate_list = list(candidate_list_one)

        hist_seed_list = []
        same_degree_nodes = []
        while len(candidate_list)<=99:
            hist = random.choice(main_seed_list)
            deg_match = sr.ret_same_deg(hist)
            flag1 = False
            flag2 = False
            for node in candidate_list:
                if node == deg_match:
                    flag1 = True
                    break
            for node in hist_seed_list:
                if node == hist:
                    flag2=True
                    break
            if flag1== False and flag2==False:
                hist_seed_list.append(hist)
                same_degree_nodes.append(deg_match)
                candidate_list.append(deg_match)

        
	print "iteration = "+str(iterations+1) 
	
        print "RWR Set1"
        thread.start_new_thread(set1,(main_seed_list,candidate_list_one,hist_seed_list,G,iterations))
        print "RWR Set2"
	thread.start_new_thread(set2,(main_seed_list,candidate_list_one,same_degree_nodes,hist_seed_list,G,iterations))
	
    
    
        iterations +=1
