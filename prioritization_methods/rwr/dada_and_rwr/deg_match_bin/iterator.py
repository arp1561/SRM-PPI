import pandas as pd
import pickle
import sort_all_nodes_folder as san

iter = 0
while iter<15:
    path = "/home/arpit/github/SRM-PPI/prioritization_methods/rwr/components/result/connected_components_"+str(iter)+".txt"
    folder = "component_bin/"+str(iter+1)
    components = pd.read_csv(path,delim_whitespace="",header=None)
    components=components[0]
    san.bin_list(folder,components)
    print iter
    iter+=1
