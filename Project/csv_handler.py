import csv
from graph import Graph
from node import Node
from edge import Edge

class CSVHandler:
    def __init__(self):
        self.graph = Graph()

    def read_csv(self, file_path):
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Skip header row if it exists
            for row in csv_reader:
                Node1 = Node(
                    route_id=int(row[1]), var_id=int(row[2]), stop_id=row[0],
                    timestamp=int(float(row[3])), node_type=int(row[15]),
                    latx=float(row[9]), lngy=float(row[10])
                )
                Node2 = Node(
                    route_id=int(row[5]), var_id=int(row[6]), stop_id=row[4],
                    timestamp=int(float(row[7])), node_type=int(row[16]),
                    latx=float(row[11]), lngy=float(row[12])
                )

                transfer = 0 if Node1.route_id == Node2.route_id else 1

                if Node1.node_type == 0 and Node2.node_type == 1:
                    start_node, end_node = Node1, Node2
                elif Node1.node_type == 1 and Node2.node_type == 0:
                    start_node, end_node = Node2, Node1
                else:
                    continue
                    
                edge = Edge(transfers=transfer, time_diff=float(row[8]), edge_type=int(row[20]))

                # Add edge to the graph
                self.graph.add_edge(start_node, end_node, edge)
                
    def print_graph(self):
        for node, edges in self.graph.adjacency_list.items():
            print(node.to_dict())
            for edge in edges:
                print(edge[0].to_dict(), edge[1].to_dict())
            print()
