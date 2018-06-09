import pandas as pd
import random
import sys
import numpy as np
import networkx as nx
from sklearn.preprocessing import normalize

threshold = 0.000001
final_list=[]
class Walker:
    def __init__(self,original_graph):
        self.OG = original_graph
        og_not_normalized = nx.to_numpy_matrix(original_graph)
        self.og_matrix = normalize(og_not_normalized,norm="l1",axis=0)


    def run_walker(self,seed_list,restart_prob,candidate_list):
        self.restart_prob = restart_prob

        p_0 = self.set_up_p0(seed_list)
        diff_norm=1

        p_t = np.copy(p_0)
                
        while(diff_norm>threshold):
            p_t_1 = self.calculate_next(p_t,p_0)
            diff_norm = np.linalg.norm(np.subtract(p_t_1,p_t),1)
            p_t = p_t_1
        
        gene_probs = zip(self.OG.nodes(),p_t.tolist())
        self.output_prob_from_candidate_list(gene_probs,candidate_list)



    def output_prob_from_candidate_list(self,prob_list,candidate_list):
	fp = open("result.csv","wb")
	temp=[]
        for index in prob_list:
            if index[0] in candidate_list:
	        temp.append((index[0],index[1],self.OG.degree(index[0])))
	        #fp.write(str(index[0])+","+str(index[1])+","+str(self.OG.degree(index[0]))+"\n")
	sort = sorted(temp,key=lambda x:x[1],reverse=True)
	for i in range(len(sort)):
	    fp.write(str(sort[i][0])+","+str(sort[i][1])+","+str(sort[i][2])+"\n")
	fp.close()

            

    def calculate_next(self,p_t,p_0):
        epsilon = np.squeeze(np.asarray(np.dot(self.og_matrix,p_t)))
        no_restart = epsilon * (1-self.restart_prob)
        restart = p_0 * self.restart_prob
        return np.add(no_restart,restart)

    def set_up_p0(self,source):
        p_0 = [0]*self.OG.number_of_nodes()
        
        for source_id in source:
            temp = source_id
            source_index = self.OG.nodes().index(temp)
            p_0[source_index] = 1/float(len(source))
        p_0 = np.array(p_0)
        return np.array(p_0)



def main(argv):

   # print "Will now transfer seed list data to seed_list"
    main_seed_list=pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    main_seed_list=main_seed_list[0]
    
   # print "Opening Graph"
    OG = nx.read_gpickle("HPRD-Biogrid.pkl")
    
   # print "Opening Candidate List"
    all_nodes = pd.read_csv("all_nodes.txt",delim_whitespace="",header=None)
    all_nodes = all_nodes[0]
    candidate_list_one = random.sample(all_nodes,95)
    candidate_list_two = random.sample(main_seed_list,5)
    candidate_list = candidate_list_one+candidate_list_two
    
    seed_list=[]
    for i in main_seed_list:
        flag = False
        for j in candidate_list:
    	    if i==j:
	            flag = True
    	            break
	if flag==False:
		seed_list.append(i)




    wk = Walker(OG)
    wk.run_walker(seed_list,0.7,candidate_list)

   # print final_list
if __name__=='__main__':
    main(sys.argv)
