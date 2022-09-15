# import necessary mobules 
import networkx as nx
import matplotlib.pyplot as plt

# draw graph 
g = nx.Graph()
g.add_edges_from([(1,2),(1,3),(2,4),(4,5)])
nx.draw_spring(g, with_labels = True)

# print output 
print("The BFS is:" ,list(nx.bfs_tree(g,1)))
plt.show()



