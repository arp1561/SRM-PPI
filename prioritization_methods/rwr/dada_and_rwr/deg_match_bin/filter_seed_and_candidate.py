import pandas as pd
import pickle
import networkx as nx

G = nx.read_gpickle("HPRD-Biogrid.pkl")
bin1=[]
bin2=[]
bin3=[]
bin4=[]
bin5=[]
bin6=[]
bin7=[]
bin8=[]    
with open("bin1.pkl",'rb') as f:
    bin1 = pickle.load(f)
with open("bin2.pkl",'rb') as f:
    bin2 = pickle.load(f)
with open("bin3.pkl",'rb') as f:
    bin3 = pickle.load(f)
with open("bin4.pkl",'rb') as f:
    bin4 = pickle.load(f)
with open("bin5.pkl",'rb') as f:
    bin5 = pickle.load(f)
with open("bin6.pkl",'rb') as f:
    bin6 = pickle.load(f)
with open("bin7.pkl",'rb') as f:
    bin7 = pickle.load(f)
with open("bin8.pkl",'rb') as f:
    bin8 = pickle.load(f)

seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list=seed_list[0]
bins=[]
for node in seed_list:
	if G.degree(node) == 1:
		if 'bin1' not in bins:
			bins.append('bin1')
	elif G.degree(node)>=2 and G.degree(node)<=5:
		if 'bin2' not in bins:
			bins.append('bin2')
	elif G.degree(node)>=6 and G.degree(node)<=10:
		if 'bin3' not in bins:
			bins.append('bin3')
	elif G.degree(node)>=11 and G.degree(node)<=25:
		if 'bin4' not in bins:
			bins.append('bin4')
	elif G.degree(node)>=26 and G.degree(node)<=50:
		if 'bin5' not in bins:
			bins.append('bin5')
	elif G.degree(node)>=51 and G.degree(node)<=75:
		if 'bin6' not in bins:
			bins.append('bin6')
	elif G.degree(node)>=76 and G.degree(node)<=100:
		if 'bin7' not in bins:
			bins.append('bin7')
	else:
		if 'bin8' not in bins:
			bins.append('bin8')	

print bins
