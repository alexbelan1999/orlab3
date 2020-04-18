import networkx as nx
import matplotlib.pyplot as plt
import func

# nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nodes = [1, 2, 3, 4, 5]
edges_with_weight = [[1, 2, 17], [1, 3, 19], [2, 3, 4], [2, 4, 12], [3, 2, 4], [3, 5, 9], [3, 4, 8], [4, 2, 12],
                     [4, 3, 6], [4, 5, 24]]
edges_with_weight1 = [(1, 2, 17), (1, 3, 19), (2, 3, 4), (2, 4, 12), (3, 2, 4), (3, 5, 9), (3, 4, 8), (4, 2, 12),
                      (4, 3, 6), (4, 5, 24)]
# edges_with_weight = [[1,2,10], [1,4,5], [2,3,3], [2,5,9] , [3,6,11], [4,2,5], [4,5,10], [4,7,6], [4,8,15], [5, 6,13], [5,8,10], [5,9,5], [6,9,7], [7,8,8], [8,9,4]]
# edges_with_weight1 = [(1,2,10), (1,4,5), (2,3,3), (2,5,9) , (3,6,11), (4,2,5), (4,5,10), (4,7,6), (4,8,15), (5, 6,13), (5,8,10), (5,9,5), (6,9,7), (7,8,8), (8,9,4)]
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges_with_weight)

layout = nx.spring_layout(G)
nx.draw(G, layout, with_labels=True, node_color='b')
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
plt.show()

func.FordFalk(nodes, edges_with_weight, edges_with_weight1)
