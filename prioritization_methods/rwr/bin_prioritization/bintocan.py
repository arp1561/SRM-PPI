import networkx as nx
import pickle
G = nx.read_gpickle("HPRD-Biogrid.pkl")
bin1=[]
bin2=[]
bin3=[]
bin4=[]
bin5=[]
bin6=[]
bin7=[]
bin8=[]    

with open("bin/bin1.pkl",'rb') as f:
    bin1 = pickle.load(f)
with open("bin/bin2.pkl",'rb') as f:
    bin2 = pickle.load(f)
with open("bin/bin3.pkl",'rb') as f:
    bin3 = pickle.load(f)
with open("bin/bin4.pkl",'rb') as f:
    bin4 = pickle.load(f)
with open("bin/bin5.pkl",'rb') as f:
    bin5 = pickle.load(f)
with open("bin/bin6.pkl",'rb') as f:
    bin6 = pickle.load(f)
with open("bin/bin7.pkl",'rb') as f:
    bin7 = pickle.load(f)
with open("bin/bin8.pkl",'rb') as f:
    bin8 = pickle.load(f)

fp = open("candidate_list_1.txt","wb")
for i in bin1:
    fp.write(i+"\n")
fp = open("candidate_list_2.txt","wb")
for i in bin2:
    fp.write(i+"\n")
fp = open("candidate_list_3.txt","wb")
for i in bin3:
    fp.write(i+"\n")
fp = open("candidate_list_4.txt","wb")
for i in bin4:
    fp.write(i+"\n")
fp = open("candidate_list_5.txt","wb")
for i in bin5:
    fp.write(i+"\n")
fp = open("candidate_list_6.txt","wb")
for i in bin6:
    fp.write(i+"\n")
fp = open("candidate_list_7.txt","wb")
for i in bin7:
    fp.write(i+"\n")
fp = open("candidate_list_8.txt","wb")
for i in bin8:
    fp.write(i+"\n")
    

