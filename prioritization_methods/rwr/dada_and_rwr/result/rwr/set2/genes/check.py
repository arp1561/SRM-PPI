import pandas as pd

count =0 
iter =0 
while iter<=99:
    data = pd.read_csv("gene_"+str(iter)+".txt",delim_whitespace="",header=None)
    data=data[0]
    for i in data:
        if i == 'CLK1':
            count+=1
    iter+=1
print count
