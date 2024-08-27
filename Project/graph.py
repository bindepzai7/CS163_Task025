from node import Node
from edge import Edge
import heapq

class Graph:
    def __init__(self):
        self.node_frequency = {}  # Tracks the number of times a node appears in shortest paths
        self.adj = {}  # Adjacency list to store edges for shortest path calculations
    
    def add_edge(self, start_node, end_node, edge):
        if start_node.stop_id not in self.adj:
            self.adj[start_node.stop_id] = []
        self.adj[start_node.stop_id].append((end_node, edge))

        if start_node.stop_id not in self.node_frequency:
            self.node_frequency[start_node.stop_id] = 0
        if end_node.stop_id not in self.node_frequency:
            self.node_frequency[end_node.stop_id] = 0
    
    def print_graph(self):
        print("Nodes and their frequencies:")
        for node_id, freq in self.node_frequency.items():
            print(f"Node ID: {node_id}, Frequency: {freq}")
        
        print("\nEdges in the graph:")
        for node_id, edges in self.adj.items():
            print(f"Start Node ID: {node_id}")
            for end_node, edge in edges:
                print(f"  --> End Node ID: {end_node.stop_id}, Edge: {edge.time_diff}")
                

    #For each pair of stops, you are asked to find the shortest path with the least weight.
    #And if two paths for the pair (i, j) have the same weight, choose the path with the earliest departure time and, if needed, the earliest arrival time. 
    #Use these shortest paths to find the top k most important bus stops.
    def dijkstra(self, start_node_id):
        # Initialize distances to infinity
        dist = {node_id: float('inf') for node_id in self.adj}
        dist[start_node_id] = 0

        # Initialize priority queue with start node
        pq = [(0, start_node_id)]
        heapq.heapify(pq)

        while pq:
            cur_dist, cur_node_id = heapq.heappop(pq)
            if cur_dist > dist[cur_node_id]:
                continue

            for neighbor, edge in self.adj[cur_node_id]:
                new_dist = dist[cur_node_id] + edge.time_diff
                if new_dist < dist[neighbor.stop_id]:
                    dist[neighbor.stop_id] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor.stop_id))
        
        return dist            
    