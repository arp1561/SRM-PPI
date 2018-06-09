from operator import itemgetter
import pandas as pd

iter=0
while iter<100:
    data = pd.read_csv("set3/scores/rwr_result_set3_"+str(iter)+".txt",delim_whitespace="",header=None)
    list = []
    col1 = data[0]
    col2 = data[1]
    col3 = data[2]

    for i in range(len(data[0])):
        list.append((col1[i],col2[i],col3[i]))
        print i
    sort = sorted(list,key = lambda x:x[1],reverse=True)
    
    fp = open("set3/scores/rwr_result_set3_"+str(iter)+".txt","w")
    for i in range(len(sort)):
        row = sort[i]
        fp.write(str(row[0])+","+str(row[1])+","+str(row[2])+"\n")
    iter+=1
