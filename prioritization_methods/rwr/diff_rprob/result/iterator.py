from analyse import Analyse as ana
obj = ana()
graph ="/home/arpit/github/SRM-PPI/prioritization_methods/rwr/diff_rprob/HPRD-Biogrid.pkl"

iteration = 1
while iteration<=10:
    obj.run(iteration,str(iteration)+"/gene.txt",graph)
    iteration+=1
