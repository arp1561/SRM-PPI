import pandas as pd
import pickle
import networkx as nx

#all_nodes =pd.read_csv("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/dada_and_rwr/deg_match_bin/seed_gene_all.txt",delim_whitespace="",header=None)
#all_nodes = all_nodes[0]
def bin_list(folder):
    G = nx.read_gpickle("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/dada_and_rwr/HPRD-Biogrid.pkl")
    all_nodes = pd.read_csv("all_nodes_with_seed.txt",delim_whitespace="",header=None)
    all_nodes = all_nodes[0]

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

    fp = open("bin_size.txt","wb")
    fp.write("bin1,1,"+str(len(bin1))+"\n")
    fp.write("bin2,2-5,"+str(len(bin2))+"\n")
    fp.write("bin3,6-10,"+str(len(bin3))+"\n")
    fp.write("bin4,11-25,"+str(len(bin4))+"\n")
    fp.write("bin5,26-50,"+str(len(bin5))+"\n")
    fp.write("bin6,51-75,"+str(len(bin6))+"\n")
    fp.write("bin7,76-100,"+str(len(bin7))+"\n")
    fp.write("bin8,Greater than 100,"+str(len(bin8))+"\n")
    fp.close()

