#TEST
import pandas as pd
import os

iter =0 
while iter<=99:
	data = pd.read_csv("result/dada/corrected_Ratio_"+str(iter)+".txt",delim_whitespace="",header=None)
	col1=data[0]
	col2=data[1]
	list=[]
	for i in range(len(data)):
		list.append((col1[i],col2[i]))
		print i
	sort = sorted(list,key=lambda x:x[1],reverse=True)
	fp = open("result/sorted/corrected_Ratio_"+str(iter)+".csv","w")
	for i in range(len(sort)):
		row = sort[i]
		fp.write(str(row[0])+","+str(row[1])+"\n")
	fp.close()	


	
	iter+=1
