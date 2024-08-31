from csv_handler import CSVHandler

def main():
    handler = CSVHandler()
    handler.read_csv('Data/type12.csv')
    handler.read_csv('Data/type34.csv')
                     
    start_stop_id = '732'  # Example start stop
    end_stop_id = '1387'   # Example end stop

    path, weight = handler.graph.dijkstra(start_stop_id, end_stop_id)
    print(f"Shortest path: {path}")
    print(f"Weight (transfers, time_diff): {weight}")

    print("\nDetailed Path Information:")
    for i in range(len(path) - 1):
        current_stop_id = path[i]
        next_stop_id = path[i + 1]
        edge = next(edge for neighbor, edge in handler.graph.adjacency_list[handler.graph.stop_to_nodes[current_stop_id][0]] if neighbor.stop_id == next_stop_id)
        print(f"From {current_stop_id} to {next_stop_id}: Transfers = {edge.transfers}, Time Diff = {edge.time_diff}")
    

if __name__ == '__main__':
    main()
