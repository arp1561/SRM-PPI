import pandas as pd
seed_list = pd.read_csv("seed_list.txt",delim_whitespace="",header=None)
seed_list = seed_list[0]
iter = 1
while iter<=8:
    temp_list = []
    candidate_list = pd.read_csv("candidate_list/candidate_list_"+str(iter)+".txt",delim_whitespace="",header=None)
    candidate_list = candidate_list[0]
    
    for can in candidate_list:
        flag = False
        for seed in seed_list:
            if can==seed:
                flag = True
                break
        if flag==False:
            temp_list.append(can)

    print len(candidate_list)
    print len(temp_list)
    fp = open("candidate_list/candidate_list_"+str(iter)+".txt","wb")
    for i in temp_list:
        fp.write(i+"\n")
    fp.close()
    iter+=1
