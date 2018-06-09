import pandas as pd

#data_seed=pd.read_csv("noschizoseed.txt",delim_whitespace="",header=None)
same_degree=['ASS1','XPC','CAMK1']

path="same_degree"
txt_file=open("no_of_same_degree_genes.txt",'w')
sum_count=0
for gene in same_degree:
	count=0
	for i in range(0,100):
		path_to_look=path+str(i)
		data_random=pd.read_csv(path_to_look,delim_whitespace="",header=None)
		random_seed_list=data_random[0]
		for j in range(len(random_seed_list)):
			if gene==random_seed_list[j]:
				count=count+1
	txt_file.write(str(gene)+","+str(count)+"\n")
	



txt_file.close()
