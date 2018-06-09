import pandas as pd
import pickle
import networkx as nx

#all_nodes =pd.read_csv("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/dada_and_rwr/deg_match_bin/seed_gene_all.txt",delim_whitespace="",header=None)
#all_nodes = all_nodes[0]
def bin_list(folder,all_nodes):
    G = nx.read_gpickle("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/dada_and_rwr/HPRD-Biogrid.pkl")


    bin1=[]
    bin2=[]
    bin3=[]
    bin4=[]
    bin5=[]
    bin6=[]
    bin7=[]
    bin8=[]
    
    for node in all_nodes:
        if G.degree(node)==1:
            bin1.append(node)
        elif G.degree(node)>=2 and G.degree(node)<=5:
            bin2.append(node)
        elif G.degree(node)>=6 and G.degree(node)<=10:
            bin3.append(node)
        elif G.degree(node)>=11 and G.degree(node)<=25:
            bin4.append(node)
        elif G.degree(node)>=26 and G.degree(node)<=50:
            bin5.append(node)
        elif G.degree(node)>=51 and G.degree(node)<=75:
            bin6.append(node)
        elif G.degree(node)>=76 and G.degree(node)<=100:
            bin7.append(node)
        else:
            bin8.append(node)
    
    with open(folder+"/bin1.pkl","wb") as f:
        pickle.dump(bin1,f)
    with open(folder+"/bin2.pkl","wb") as f:
        pickle.dump(bin2,f)
    with open(folder+"/bin3.pkl","wb") as f:
        pickle.dump(bin3,f)
    with open(folder+"/bin4.pkl","wb") as f:
        pickle.dump(bin4,f)
    with open(folder+"/bin5.pkl","wb") as f:
        pickle.dump(bin5,f)
    with open(folder+"/bin6.pkl","wb") as f:
        pickle.dump(bin6,f)
    with open(folder+"/bin7.pkl","wb") as f:
        pickle.dump(bin7,f)
    with open(folder+"/bin8.pkl","wb") as f:
        pickle.dump(bin8,f)
