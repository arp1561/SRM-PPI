import pandas as pd

seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list=list(seed_list[0])
iter = 0
while iter<31:
    path = "result/connected_components_"+str(iter)+".txt"
    data = pd.read_csv(path,delim_whitespace="",header=None)
    data = list(data[0])
    temp_list = []
    for node in data:
        flag = False
        for genes in seed_list:
            if node == genes:
                flag = True
                break
        if flag == False:
            temp_list.append(node)
    fp = open(path,"wb")
    for i in temp_list:
        fp.write(i+"\n")
    fp.close()
    print iter
    iter+=1
