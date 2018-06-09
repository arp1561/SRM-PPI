#to check wether each gene file has 5 genes
import pandas as pd
import time

iteration = 0
while iteration<100:
    data =  pd.read_csv("gene_"+str(iteration)+".txt",delim_whitespace="",header=None)
    data = data[0]
    if len(data)<5:
        print str(iteration)+" "+str(len(data))
    iteration+=1
