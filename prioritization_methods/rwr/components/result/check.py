import pandas as pd

gwas = pd.read_csv("diab_seed_list_15.txt",delim_whitespace="",header=None)
gwas = gwas[0]

iter = 0
while iter<15:
    temp_list = []
    data =  pd.read_csv("connected_components_"+str(iter)+".txt",delim_whitespace="",header=None)
    data = data[0]
    for i in data:
        flag = False
        for j in gwas:
            if i==j:
                flag = True
                break
        if flag==False:
            temp_list.append(i)
    print "Original length = "+str(len(data))+" New = "+str(len(temp_list))

    fp = open("connected_components_"+str(iter)+".txt","wb")
    for i in temp_list:
        fp.write(i+"\n")
    fp.close()
    iter+=1
