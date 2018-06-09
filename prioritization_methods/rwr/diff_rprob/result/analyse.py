import pandas as pd
import networkx as nx

class Analyse:
    
    def load_hist_gene(self,hist_gene_path):
        hist_genes = pd.read_csv(hist_gene_path,delim_whitespace="",header=None)
        hist_genes = hist_genes[0]
        return hist_genes

    def open_graph(slef,graph_location):
        G = nx.read_gpickle(graph_location)
        return G

    def write(self,G,folder,node1,node2,node3,node4,node5,hist_genes):
        fp = open(str(folder)+"/analyse.txt","w")
        fp.write("Gene,Degree,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9\n")
        
        fp.write(hist_genes[0]+","+str(G.degree(hist_genes[0]))+",")
        for i in range(len(node1)):
            fp.write(str(node1[i])+",")
        fp.write("\n")
        
        fp.write(hist_genes[1]+","+str(G.degree(hist_genes[1]))+",")
        for i in range(len(node2)):
            fp.write(str(node2[i])+",")
        fp.write("\n")
        
        fp.write(hist_genes[2]+","+str(G.degree(hist_genes[2]))+",")
        for i in range(len(node3)):
            fp.write(str(node3[i])+",")
        fp.write("\n")
        
        fp.write(hist_genes[3]+","+str(G.degree(hist_genes[3]))+",")
        for i in range(len(node4)):
            fp.write(str(node4[i])+",")
        fp.write("\n")
        
        fp.write(hist_genes[4]+","+str(G.degree(hist_genes[4]))+",")
        for i in range(len(node5)):
            fp.write(str(node5[i])+",")
        fp.write("\n")



    def run(self,folder,hist_gene_path,graph_location):
        hist_genes = self.load_hist_gene(hist_gene_path)
        G = self.open_graph(graph_location)
        node1=[]
        node2=[]
        node3=[]
        node4=[]
        node5=[]
        iteration=0.1
        while iteration<=0.9:
            result = pd.read_csv(str(folder)+"/rprob_"+str(iteration)+".txt",delim_whitespace="",header=None)
            result = result[0]
            for i in range(len(result)):
                if result[i] == hist_genes[0]:
                    node1.append(i+1)
                elif result[i] == hist_genes[1]:
                    node2.append(i+1)
                elif result[i] == hist_genes[2]:
                    node3.append(i+1)
                elif result[i] == hist_genes[3]:
                    node4.append(i+1)
                elif result[i] == hist_genes[4]:
                    node5.append(i+1)
            iteration+=0.1

        self.write(G,folder,node1,node2,node3,node4,node5,hist_genes)




