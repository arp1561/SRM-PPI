import select_random_genes as sr
import thread
import pandas as pd
import networkx as nx
import random
from rwr import Walker

def set1_original(main_seed_list,candidate_list_one,candidate_list_two,G,iteration):
    
    path_to_save = "result/rwr/edge_swap_result/original/set1/scores/rwr_result_set1_"

    candidate_list = candidate_list_one + candidate_list_two

    seed_list = []
    for i in main_seed_list:
        flag = False
        for j in candidate_list:
            if i==j:
                flag = True
                break
        if flag==False:
            seed_list.append(i)

    print "Running RWR for Set1_original"
    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iteration)
    print "RWR Done and scores saved. Saving gene list.."

    fp = open("result/rwr/edge_swap_result/original/set1/genes/gene_"+str(iteration)+".txt","w")
    for i in candidate_list_two:
        fp.write(i+"\n")
    fp.close()
    
    print "Done saving genes for Set1_original"
    return 

def set2_original(main_seed_list,all_nodes,candidate_list_one,G,iteration):
    path_to_save = "result/rwr/edge_swap_result/original/set2/scores/rwr_result_set2_"

    print "Selecting same degree nodes"

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
                flag2 = True
                break
        if flag1==False and flag2==False:
            hist_seed_list.append(hist)
            same_degree_nodes.append(deg_match)
            candidate_list.append(deg_match)

    for i in range(len(same_degree_nodes)):
        print str(hist_seed_list[i])+" "+str(G.degree(hist_seed_list[i]))+" "+str(same_degree_nodes[i])+" "+str(G.degree(same_degree_nodes[i]))

    print "Running RWR for Set2_original"
    wk = Walker(G)
    wk.run_walker(main_seed_list,0.7,candidate_list,path_to_save,iteration)

    ranks = []
    for z in same_degree_nodes:
        flag = False
        result_file = pd.read_csv("result/rwr/edge_swap_result/original/set2/scores/rwr_result_set2_"+str(iteration)+".txt",delim_whitespace="",header=None)
        result_file = list(result_file[0])
        for i in range(len(result_file)):
            if z == result_file[i]:
                flag = True
                break
        if flag == True:
            ranks.append(i)

    print "Ran RWR and saved scores. Will now save gene list for Set2_original"

    fp = open("result/rwr/edge_swap_result/original/set2/genes/gene_"+str(iteration)+".txt","w")
    for i in range(len(same_degree_nodes)):
        fp.write(hist_seed_list[i]+","+same_degree_nodes[i]+","+str(ranks[i])+"\n")
    print "done writing.."
    return hist_seed_list,same_degree_nodes

def set1_swapped(main_seed_list,candidate_list_one,candidate_list_two,G,iteration):
    path_to_save = "result/rwr/edge_swap_result/edge_swap/set1/scores/rwr_result_set1_"

    candidate_list = candidate_list_one+candidate_list_two

    seed_list = []
    for i in main_seed_list:
        flag = False
        for j in candidate_list:
            if i==j:
                flag = True
                break
        if flag==False:
            seed_list.append(i)
    print "Running RWR for Set1_EdgeSwap"
    
    wk = Walker(G)
    wk.run_walker(seed_list,0.7,candidate_list,path_to_save,iteration)
    print "RWR done for set1-edge swapped"

    fp = open("result/rwr/edge_swap_result/original/set1/genes/gene_"+str(iteration)+".txt","w")
    for i in candidate_list_two:
        fp.write(i+"\n")
    fp.close()

    print "Done saving genes for Set1_edge_swapped"
    return

def set2_swapped(main_seed_list,candidate_list_one,same_degree_nodes,G,iteration):
    path_to_save = "result/rwr/edge_swap_result/edge_swap/set2/scores/rwr_result_set2_"

    candidate_list = candidate_list_one+same_degree_nodes

    print "Running rwr for set2_swapped"
    wk = Walker(G)
    wk.run_walker(main_seed_list,0.7,candidate_list,path_to_save,iteration)

    ranks = []
    for z in same_degree_nodes:
        flag = False
        result_file = pd.read_csv("result/rwr/edge_swap_result/edge_swap/set2/scores/rwr_result_set2_"+str(iteration)+".txt",delim_whitespace="",header=None)
        result_file = list(result_file[0])
        for i in range(len(result_file)):
            if z==result_file[i]:
                flag = True
                break
        if flag == True:
            ranks.append(i)
    print "RWR Done for set2-edgeswapped"
    fp = open("result/rwr/edge_swap_result/edge_swap/set2/genes/gene_"+str(iteration)+".txt","w")
    for i in range(len(same_degree_nodes)):
        fp.write(hist_seed_list[i]+","+same_degree_nodes[i]+","+str(ranks[i])+"\n")
    print "Done Writing..."
    return






if __name__ == "__main__":
    G1 = nx.read_gpickle("HPRD-Biogrid.pkl")
    G2 = nx.read_gpickle("edge_swapped_graph.pkl")
    all_nodes_temp = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
    all_nodes_temp = list(all_nodes_temp[0])

    main_seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    main_seed_list = list(main_seed_list[0])

    all_nodes = [node for node in all_nodes_temp if node not in main_seed_list]

    iteration = 0
    while iteration<100:
        candidate_list_one = random.sample(all_nodes,95)
        print "Iteration = "+str(iteration+1)

        print "Set2 - Original graph"
        hist_seed_list,same_degree_nodes = set2_original(main_seed_list,all_nodes,candidate_list_one,G1,iteration)        

        thread.start_new_thread(set1_original,(main_seed_list,candidate_list_one,hist_seed_list,G1,iteration))
        thread.start_new_thread(set1_swapped,(main_seed_list,candidate_list_one,hist_seed_list,G2,iteration))
        thread.start_new_thread(set2_swapped,(main_seed_list,candidate_list_one,same_degree_nodes,G2,iteration))


        iteration+=1    
    



