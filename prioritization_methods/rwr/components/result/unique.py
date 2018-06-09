import pandas as pd

unique_list = []

iter = 0 
while iter<32:
    data = pd.read_csv("connected_components_"+str(iter)+".txt",delim_whitespace="",header=None)
    data = data[0]
    print "File = "+str(iter+1)
    for node in data:
        if node not in unique_list:
            unique_list.append(node)
    iter+=1

print len(unique_list)
fp = open("unique_degree_list.txt","wb")
for i in range(len(unique_list)):
    fp.write(unique_list[i]+"\n")
