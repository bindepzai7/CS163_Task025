import json
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)  # Adjacency list for nodes
        self.stop_to_nodes = defaultdict(list)   # Map from stop_id to a list of nodes
        self.stop_frequency = defaultdict(int)   # Frequency of stop_ids in shortest paths

    def add_edge(self, start_node, end_node, edge):
        self.adjacency_list[start_node].append((end_node, edge))
        self.stop_to_nodes[start_node.stop_id].append(start_node)
        self.stop_to_nodes[end_node.stop_id].append(end_node)

    def dijkstra(self, start_stop_id, end_stop_id):
        pq = []
        # Start with the nodes corresponding to the start_stop_id, prioritizing by earliest departure
        for start_node in self.stop_to_nodes[start_stop_id]:
            heapq.heappush(pq, ((0, 0), start_node.stop_id, start_node.timestamp, 0))  # (weight, stop_id, departure_time, arrival_time)

        distances = defaultdict(lambda: (float('inf'), float('inf')))
        distances[start_stop_id] = (0, 0)
        previous = {}

        while pq:
            current_weight, current_stop_id, current_time, current_arrival_time = heapq.heappop(pq)
            current_node = next(node for node in self.stop_to_nodes[current_stop_id] if node.timestamp == current_time)

            if current_stop_id == end_stop_id:
                break

            for neighbor, edge in self.adjacency_list.get(current_node, []):
                new_weight = (current_weight[0] + edge.transfers, current_weight[1] + edge.time_diff)
                new_arrival_time = current_time + edge.time_diff

                # Determine if the new path is better, considering weight and time
                is_better_path = (
                    new_weight < distances[neighbor.stop_id] or
                    (new_weight == distances[neighbor.stop_id] and current_time < distances[neighbor.stop_id][1]) or
                    (new_weight == distances[neighbor.stop_id] and current_time == distances[neighbor.stop_id][1] and new_arrival_time < current_arrival_time)
                )

                if is_better_path:
                    distances[neighbor.stop_id] = (new_weight, current_time)
                    heapq.heappush(pq, (new_weight, neighbor.stop_id, neighbor.timestamp, new_arrival_time))
                    previous[neighbor.stop_id] = current_stop_id

        path = self.reconstruct_path(previous, start_stop_id, end_stop_id)
    
        for stop_id in path:
            self.stop_frequency[stop_id] += 1

        return path, distances[end_stop_id]

    def reconstruct_path(self, previous, start_stop_id, end_stop_id):
        path = []
        current_stop_id = end_stop_id
        while current_stop_id:
            path.append(current_stop_id)
            current_stop_id = previous.get(current_stop_id)
        path.reverse()
        return path
    
    def find_all_shortest_paths(self):
        all_stop_ids = list(self.stop_to_nodes.keys())
        total_pairs = len(all_stop_ids) * (len(all_stop_ids) - 1) // 2

        print(f"Calculating shortest paths for {total_pairs} pairs of stops...")
        for i, start_stop_id in enumerate(all_stop_ids):
            for j, end_stop_id in enumerate(all_stop_ids):
                if start_stop_id != end_stop_id:
                    self.dijkstra(start_stop_id, end_stop_id)
        print("Finished calculating all shortest paths.")
    
    def save_stop_frequencies(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.stop_frequency, f, indent=4)
        print(f"Stop frequencies saved to {file_path}.")