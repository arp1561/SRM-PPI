import random
import pandas as pd
import pickle
import networkx as nx

def check_folder(node):
    path = "/home/prabal/Desktop/SRM-PPI/prioritization_methods/rwr/dada_and_rwr/deg_match_bin/component_bin/"
    seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
    seed_list=seed_list[0]
    i=0
    for i in range(len(seed_list)):
        if seed_list[i]==node:
            break
    
    i+=1
    folder = path+str(i)+"/"
    return folder
def ret_same_deg(node):
    folder = check_folder(node)
    G = nx.read_gpickle("HPRD-Biogrid.pkl")
    bin1=[]
    bin2=[]
    bin3=[]
    bin4=[]
    bin5=[]
    bin6=[]
    bin7=[]
    bin8=[]    
    with open(folder+"bin1.pkl",'rb') as f:
        bin1 = pickle.load(f)
    with open(folder+"bin2.pkl",'rb') as f:
        bin2 = pickle.load(f)
    with open(folder+"bin3.pkl",'rb') as f:
        bin3 = pickle.load(f)
    with open(folder+"bin4.pkl",'rb') as f:
        bin4 = pickle.load(f)
    with open(folder+"bin5.pkl",'rb') as f:
        bin5 = pickle.load(f)
    with open(folder+"bin6.pkl",'rb') as f:
        bin6 = pickle.load(f)
    with open(folder+"bin7.pkl",'rb') as f:
        bin7 = pickle.load(f)
    with open(folder+"bin8.pkl",'rb') as f:
        bin8 = pickle.load(f)

    if G.degree(node) == 1:
        same_deg = random.choice(bin1)
    elif G.degree(node)>=2 and G.degree(node)<=5:
        same_deg = random.choice(bin2)
    elif G.degree(node)>=6 and G.degree(node)<=10:
        same_deg = random.choice(bin3)
    elif G.degree(node)>=11 and G.degree(node)<=25:
        same_deg = random.choice(bin4)
    elif G.degree(node)>=26 and G.degree(node)<=50:
        same_deg = random.choice(bin5)
    elif G.degree(node)>=51 and G.degree(node)<=75:
        same_deg = random.choice(bin6)
    elif G.degree(node)>=76 and G.degree(node)<=100:
        same_deg = random.choice(bin7)
    else:
        same_deg = random.choice(bin8)
    return same_deg
