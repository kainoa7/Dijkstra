import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in graph}
    # Distance from start vertex to itself is 0
    distances[start] = 0
    
    # Set of vertices whose shortest distance is known
    visited = set()
    
    while len(visited) < len(graph):
        # Find the vertex with the minimum distance from the start
        current_vertex = min((v for v in graph if v not in visited), key=lambda x: distances[x])
        
        # Mark the current vertex as visited
        visited.add(current_vertex)
        
        # Update distances to adjacent vertices through the current vertex
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print("Vertex:", vertex, "Distance:", distance)

# Create a graph from the adjacency list
G = nx.Graph()
for vertex, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(vertex, neighbor, weight=weight)

# Position nodes using spring layout
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold")

# Draw edge labels
edge_labels = {(node1, node2): weight['weight'] for node1, node2, weight in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Show plot
plt.title("Graph Visualization")
plt.show()