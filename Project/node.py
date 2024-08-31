class Node:
    def __init__(self, route_id, var_id, stop_id, timestamp, node_type, latx, lngy):
        self.route_id = route_id
        self.var_id = var_id
        self.stop_id = stop_id
        self.timestamp = timestamp
        self.node_type = node_type
        self.latx = latx
        self.lngy = lngy

    def to_dict(self):
        return {
            'route_id': self.route_id,
            'var_id': self.var_id,
            'stop_id': self.stop_id,
            'timestamp': self.timestamp,
            'node_type': self.node_type,
            'latx': self.latx,
            'lngy': self.lngy
        }

    def __eq__(self, other):
        return (self.stop_id, self.timestamp) == (other.stop_id, other.timestamp)

    def __hash__(self):
        return hash((self.stop_id, self.timestamp))
