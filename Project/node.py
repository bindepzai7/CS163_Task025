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

    def from_dict(cls, data):
        return cls(
            route_id=data['route_id'],
            var_id=data['var_id'],
            stop_id=data['stop_id'],
            timestamp=data['timestamp'],
            node_type=data['node_type'],
            latx=data['latx'],
            lngy=data['lngy']
        )
