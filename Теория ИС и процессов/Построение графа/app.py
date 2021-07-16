import networkx as nx
import os
import pylab as plt
import pandas as pd

#g = nx.read_edgelist("face.txt")
g = nx.read_edgelist("facebook_combined.txt")
k = g.number_of_nodes()
nx.draw(g)
print(nx.info(g))
print('Плотность: ', nx.density(g))
print('Коэф кластризации: ', nx.average_clustering(g))
#print(nx.transitivity(g))
#print(nx.degree_histogram(g))
#plt.savefig('graph.png')
#plt.close()