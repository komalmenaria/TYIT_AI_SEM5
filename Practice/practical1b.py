# Step 1 import packages 2 
import networkx as nx
import matplotlib.pyplot as plt

# Step 2 draw diagram 
g = nx.Graph()
g.add_edges_from([(1,2),(1,3),(2,4),(2,5),(5,6)])
nx.draw_spring(g,with_labels = True)
# Step 3 print output

print("The DFS is:",list(nx.dfs_tree(g,1)))
plt.show() 
