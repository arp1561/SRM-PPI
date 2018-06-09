DEPENDENCIES: pandas,networkx
DOWNLOAD:
sudo pip install pandas
sudo pip install networkx 

FILES:
phenome_interactome(pickle file),candidate.txt

HOW TO RUN THE CODE:
1. when running the code from your terminal, the name of the file is to be given as command line argument
for example, python network_propagation.py candidate.txt
2. to access the --help optional argument 
run python network_propagation.py candidate.txt -h
3. make sure both the files are in the same directory as the code

OUTPUT:
your output will look something like this,
53.0 PRKCB
the maximum flow followed by the gene symbol of the candidate gene.

