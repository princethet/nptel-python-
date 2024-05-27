#page ranking algorithm
# step 1 take the random walk on the network 
# step 2 increament the points of each node 
# step 3 find the node with the highest points  
# crawlers takes random walk on www network and rank the websites.

import networkx as nx 
import matplotlib.pyplot as plt 
plt.figure(0)
G = nx.barbell_graph(40,2) 
nx.draw_networkx(G)
plt.figure(1)

G = nx.complete_graph(40) 
nx.draw_networkx(G)
plt.figure(2)

G = nx.ladder_graph(40) 
nx.draw_networkx(G)
plt.figure(3)

G = nx.path_graph(4) 
nx.draw_networkx(G)
#plt.figure(5)

plt.show()
# print(nx.draw(G))
