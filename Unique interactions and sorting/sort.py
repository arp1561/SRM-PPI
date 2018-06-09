'''
Made by - Arpit Joshi
Purpose - Sort the Biogrid and HPRD database in a lexicographic manner between
col1 and col2 and then filter only the unique interactions
'''

import pandas as pd

data = pd.read_csv("BiogridDir2015.txt",delim_whitespace="",header=None)
col1 = data[0]
col2 = data[1]
col3 = data[2]

print "Data loaded"
for i in range(len(col1)):
    print "Iteration :"+str(i)
    if col1[i]>col2[i]:
        temp = col1[i]
        col1[i]=col2[i]
        col2[i]=temp
print "Sorted"
print "Will now find unique interactions"

tuple = zip(col1,col2)
temp_tuple = []
unique_tuple = []

for i in range(len(tuple)):
    print "Iteration "+str(i+1)
    if tuple[i] not in temp_tuple:
        temp_tuple.append(tuple[i])
        unique_tuple.append((tuple[i][0],tuple[i][1],col3[i]))

print "Length of unique interaction ="+str(len(unique_tuple))

fp = open("unique_interactions.txt","w")
for i in range(len(unique_tuple)):
    print "iteration "+str(i+1)
    fp.write(str(unique_tuple[i][0])+","+str(unique_tuple[i][1])+","+str(unique_tuple[i][2])+"\n")

