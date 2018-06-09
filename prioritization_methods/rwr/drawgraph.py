import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()
edges = [('a','b'),('a','c'),('a','d'),('a','e'),('e','f'),('e','g'),('e','h')]
G.add_edges_from(edges)
print nx.shortest_path(G,source='x',target='g')


