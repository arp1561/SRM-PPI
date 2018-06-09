import pandas as pd
import networkx as nx

G = nx.read_gpickle("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/randomize2/HPRD-Biogrid.pkl")
iteration=0
temp_hist_gene=[]



#creates a list of all hist genes
while iteration<100:
    path = "gene_"+str(iteration)+".txt"
    data = pd.read_csv(path,delim_whitespace="",header=None)
    data = data[0]
    for i in data:
        temp_hist_gene.append(i)
    iteration+=1

print len(temp_hist_gene)
#finding unique ones and finding degree
final_hist_gene=[]
degree=[]
for gene in temp_hist_gene:
    if gene not in final_hist_gene:
        final_hist_gene.append(gene)
        degree.append(G.degree(gene))

no_top10=[]
for gene in final_hist_gene:
    iteration=0
    count=0
    while iteration<100:
        path = "/home/arpit/github/SRM-PPI/prioritization_methods/rwr/randomize2/result/set3/scores/rwr_result_set3_"+str(iteration)+".txt"
        data = pd.read_csv(path,delim_whitespace="",header=None)
        data = data[0]
        x =0
        while x<10:
            if data[x] == gene:
                count+=1
            x+=1
        iteration+=1
    no_top10.append(count)
        

fp = open("/home/arpit/github/SRM-PPI/prioritization_methods/rwr/randomize2/result/set3/set3_analysis.txt","w")
for i in range(len(degree)):
    fp.write(str(final_hist_gene[i])+","+str(degree[i])+","+str(no_top10[i])+"\n")
fp.close()







