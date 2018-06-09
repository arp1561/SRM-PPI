import pandas as pd

seed = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed = seed[0]

gwas = pd.read_csv("gwas_genes.txt",delim_whitespace="",header=None)
gwas = gwas[0]

temp_gwas_genes = []
for i in gwas:
    flag =False
    for j in seed:
        if i==j:
            print i
            flag = True
            break
    if flag==False:
        temp_gwas_genes.append(i)
print len(temp_gwas_genes)

fp = open("gwas_genes_filtered.txt","wb")
for i in temp_gwas_genes:
    fp.write(i+"\n")

fp.close()
