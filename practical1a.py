import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
g.add_edges_from([(1,2),(1,3),(2,4),(2,5),(3,6),(3,7)])
nx.draw_spring(g , with_labels = True)
print("The BFS is :",list(nx.bfs_tree(g,1)))
plt.show()