import pandas as pd
import time

iter =0
count =0
while iter<=99:
    data = pd.read_csv("gene_"+str(iter)+".txt",delim_whitespace="",header=None)
    hist_gene = list(data[0])
    deg_match_gene = list(data[1])
    #rank = list(data[2])
    for i in range(len(data)):
        if hist_gene[i] == 'AKT1':
            print "File ="+str(iter)+" "+"Deg match gene = "+deg_match_gene[i]
            time.sleep(0.5)
    iter+=1
