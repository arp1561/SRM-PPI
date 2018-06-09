import pandas as pd
import networkx as nx

G = nx.Graph()
G = nx.read_gpickle("HPRD-Biogrid.pkl")
data = pd.read_csv("hpo_disease_gene.txt",delim_whitespace="",header=None)

schizo_genes=[]
temp_non_schizo_genes=[]
non_schizo_genes=[]


for i in range(len(data[0])):
    if data[1][i]=="Schizophrenia":
        print i
        schizo_genes.append(data[0][i])
print len(schizo_genes)
print schizo_genes

for i in range(len(data)):
    if data[0][i] not in schizo_genes:
        temp_non_schizo_genes.append(data[0][i])
        print i

print len(non_schizo_genes)

for i in range(len(temp_non_schizo_genes)):
    if temp_non_schizo_genes[i] not in non_schizo_genes:
        non_schizo_genes.append(temp_non_schizo_genes[i])

print len(non_schizo_genes)

fp=open("final_list.txt","w")

for i in range(len(non_schizo_genes)):
    if non_schizo_genes[i] in G.nodes():
        print "Iteration = "+str(i)
        degree = G.degree(non_schizo_genes[i])
        fp.write(str(non_schizo_genes[i])+","+str(degree)+"\n")

