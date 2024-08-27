class Edge:
    def __init__(self, transfers, time_diff, edge_type):
        self.transfers = transfers
        self.time_diff = time_diff
        self.edge_type = edge_type

    def to_dict(self):
        return {
            'transfers': self.transfers,
            'time_diff': self.time_diff,
            'edge_type': self.edge_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            transfers=data['transfers'],
            time_diff=data['time_diff'],
            edge_type=data['edge_type']
        )
