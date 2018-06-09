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


    rprob = 0.1
    while rprob<=0.9:
        path_to_save = "result/"+str(iterations+1)+"/rprob_"
    
        candidate_list = candidate_list_one + candidate_list_two
        seed_list=[]
        for i in main_seed_list:
            flag=False
            for j in candidate_list:
                if i==j:
                    flag = True
                    break
            if flag==False:
                seed_list.append(i)
        print "Will now run RWR"
        wk = Walker(G)
        wk.run_walker(seed_list,rprob,candidate_list,path_to_save,rprob)
        print "Successfully run RWR and saved scores\n Will now save the 5 genes"
        
        rprob+=0.1
    fp = open("result/"+str(iterations+1)+"/gene.txt","w")
    for i in candidate_list_two:
        fp.write(i+"\n")
    print "Returning"

if __name__=="__main__":
    G = nx.read_gpickle("HPRD-Biogrid.pkl")
    all_nodes_temp = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
    all_nodes_temp = all_nodes_temp[0]
    main_seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    main_seed_list = main_seed_list[0]
    all_nodes = [node for node in all_nodes_temp if node not in main_seed_list]
    


    iterations=0
    while iterations<50:
        candidate_list=[]
        candidate_list_one = random.sample(all_nodes,95)
        candidate_list_two = random.sample(main_seed_list,5)

        set1(main_seed_list,candidate_list_one,candidate_list_two,G,iterations)
        
        
        print "iteration = "+str(iterations+1) 
    
    
        iterations +=1
