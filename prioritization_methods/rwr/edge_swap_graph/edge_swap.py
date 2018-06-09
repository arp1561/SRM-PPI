import networkx as nx
G = nx.read_gpickle("HPRD-Biogrid.pkl")
nx.double_edge_swap(G,G.number_of_nodes(),G.number_of_nodes()*10)

print nx.number_of_edges(G)

nx.write_gpickle(G,"edge_swapped_graph.pkl")



