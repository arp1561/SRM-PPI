import pandas as pd
import time
iteration=0
while iteration<100:
    data =  pd.read_csv("rwr_result_set1_"+str(iteration)+".txt",delim_whitespace="",header=None)
    data= data[0]
    s = "DRD3"
    count=0
    for i in range(len(data)):
        if s==data[i]:
            count+=1
    print str(iteration)+" "+str(count)
    time.sleep(0.3)
    iteration+=1
