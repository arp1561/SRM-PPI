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


    def run_walker(self,seed_list,restart_prob,candidate_list,path_to_save,iterations):
        self.restart_prob = restart_prob

        p_0 = self.set_up_p0(seed_list)
        diff_norm=1

        p_t = np.copy(p_0)
                
        while(diff_norm>threshold):
            p_t_1 = self.calculate_next(p_t,p_0)
            diff_norm = np.linalg.norm(np.subtract(p_t_1,p_t),1)
            p_t = p_t_1
        
        gene_probs = zip(self.OG.nodes(),p_t.tolist())
        self.output_prob_from_candidate_list(gene_probs,candidate_list,path_to_save,iterations)



    def output_prob_from_candidate_list(self,prob_list,candidate_list,path_to_save,iterations):
	fp = open(path_to_save+str(iterations)+".txt","w")
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
    input_graph_location = "edge_swapped_graph.pkl"
    input_seed_list_location = "input_data/schizo/seed_list_low_deg.txt"
    candidate_list_location="input_data/schizo/candidate_list_low_degree.txt"

   # print "Will now transfer seed list data to seed_list"
    seed_list=generate_seed_list_from_file(input_seed_list_location)
    
   # print "Opening Graph"
    OG = open_graph_from_path(input_graph_location)
    
   # print "Opening Candidate List"
    candidate_list=open_candidate_list_from_path(candidate_list_location)
    
    wk = Walker(OG)
    wk.run_walker(seed_list,0.7,candidate_list)

   # print final_list
if __name__=='__main__':
    main(sys.argv)
