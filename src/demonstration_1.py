"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).
​
You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).
​
The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.
​
*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
colors = set(["Red", "Green", "Blue", "Purple", "Yellow"])
​
# Definition for a graph node.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None
​
# brute force approach 
# `graph` is a list of GraphNodes 
# V: number of nodes/vertices in the graph 
# E: number of edges/connections
# C: number of possible colors 
​
# O(V * E * C)
def color_graph(graph, colors):
    # Your code here
    # iterate through the nodes in our graph 
    for node in graph: # O(V)
        # figure out what colors are illegal based on the neighbors' colors 
        # illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])
        illegal_colors = {neighbor.color for neighbor in node.neighbors if neighbor.color}
​
        # for neighbor in node.neighbors: # O(E)
        #     if neighbor.color is not None:
        #         illegal_colors.add(neighbor.color)
​
        # pick a color that isn't taken by a neighbor 
        for color in colors: # O(C)
            if color not in illegal_colors: # O(1)
                node.color = color
                break
​
# Construct a undirected graph 
g1 = GraphNode(1)
g2 = GraphNode(2)
g3 = GraphNode(3)
g4 = GraphNode(4)
g5 = GraphNode(5)
​
nodes = [g1, g2, g3, g4, g5]
​
g1.neighbors.add(g2)
g1.neighbors.add(g3)
g1.neighbors.add(g4)
g2.neighbors.add(g1)
g2.neighbors.add(g4)
g2.neighbors.add(g5)
g2.neighbors.add(g3)
g3.neighbors.add(g1)
g3.neighbors.add(g2)
g4.neighbors.add(g1)
g4.neighbors.add(g2)
g5.neighbors.add(g2)
​
color_graph(nodes, colors)
​
for node in nodes:
    print(node.label, node.color)