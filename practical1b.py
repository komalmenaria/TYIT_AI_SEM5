import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
g.add_edges_from([("A","B") ,("A","C"),("B","D"),("B","E"),("D","G"),("C","F"),("F","H")])
nx.draw_spring(g, with_labels = True)
print("The DFS as is:" ,list(nx.dfs_tree(g,"A")))
plt.show()
