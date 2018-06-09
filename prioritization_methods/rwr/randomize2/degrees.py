import pandas as pd
import networkx as nx

G = nx.Graph()
G = nx.read_gpickle("HPRD-Biogrid.pkl")

data = pd.read_csv("input_data/parkinsons/seed_list.txt",delim_whitespace="",header=None)
node = data[0]

'''
diabetes_data = pd.read_csv("data/diabetes.txt",delim_whitespace="",header=None)
diabetes_node = diabetes_data[0]
diabetes_score = diabetes_data[1]


lung_cancer_data = pd.read_csv("data/lung_cancer.txt",delim_whitespace="",header=None)
lung_cancer_node = lung_cancer_data[0]
lung_cancer_score = lung_cancer_data[1]

pancreatic_data = pd.read_csv("data/pancreatic_cancer.txt",delim_whitespace="",header=None)
pancreatic_node = pancreatic_data[0]
pancreatic_score = pancreatic_data[1]


parkinsons_data = pd.read_csv("data/parkinsons.txt",delim_whitespace="",header=None)
parkinsons_node = parkinsons_data[0]
parkinsons_score = parkinsons_data[1]

schizo_data = pd.read_csv("data/schizo.txt",delim_whitespace="",header=None)
schizo_node = schizo_data[0]
schizo_score = schizo_data[1]

'''
fp = open("input_data/parkinsons/seed_list_with_degrees.txt","wb")
#fp2 = open("output_degree/diabetes_degrees.txt","w")
#fp3 = open("output_degree/lung_cancer_degrees.txt","w")
#fp4 = open("output_degree/pancreatic_cancer_degrees.txt","w")
#fp5 = open("output_degree/parkinsons_degrees.txt","w")
#fp6 = open("output_degree/schizo_degrees.txt","w")

for i in range(len(data)):
    degree = G.degree(node[i])
    fp.write(str(node[i])+","+str(degree)+"\n")


'''
for i in range(len(diabetes_data)):
    degree = G.degree(diabetes_node[i])
    fp2.write(str(diabetes_node[i])+","+str(diabetes_score[i])+","+str(degree)+"\n")

for i in range(len(lung_cancer_data)):
    degree = G.degree(lung_cancer_node[i])
    fp3.write(str(lung_cancer_node[i])+","+str(lung_cancer_score[i])+","+str(degree)+"\n")

for i in range(len(pancreatic_data)):
    degree = G.degree(pancreatic_node[i])
    fp4.write(str(pancreatic_node[i])+","+str(pancreatic_score[i])+","+str(degree)+"\n")
    
for i in range(len(parkinsons_data)):
    degree = G.degree(parkinsons_node[i])
    fp5.write(str(parkinsons_node[i])+","+str(parkinsons_score[i])+","+str(degree)+"\n")
    
for i in range(len(schizo_data)):
    degree = G.degree(schizo_node[i])
    fp6.write(str(schizo_node[i])+","+str(schizo_score[i])+","+str(degree)+"\n")


for node in lung_cancer_data:
    degree = G.degree(node)
    fp3.write(str(node)+","+str(degree)+"\n")

for node in pancreatic_data:
    degree = G.degree(node)
    fp4.write(str(node)+","+str(degree)+"\n")

for node in parkinsons_data:
    degree = G.degree(node)
    fp5.write(str(node)+","+str(degree)+"\n")

for node in schizo_data:
    degree = G.degree(node)
    fp6.write(str(node)+","+str(degree)+"\n")

for node in alzhimer_data:
    degree = G.degree(node)
    fp1.write(str(node)+","+str(degree)+"\n")

'''
