from collections import defaultdict
import math

class Node(object):
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.cost = math.inf

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(list)
        self._node_map = {}

    def insert_node(self, new_node_val):
        if new_node_val not in self._node_map:
            new_node = Node(new_node_val)
            self.nodes.append(new_node)
            self._node_map[new_node_val] = new_node

    def find_node(self, node_val):
        return self._node_map.get(node_val)

    def insert_edge(self, distance, node_from_val, node_to_val):
        self.insert_node(node_from_val)
        self.insert_node(node_to_val)
        self.edges[node_from_val].append((node_to_val,distance))
        self.edges[node_to_val].append((node_from_val,distance))

    def insert_in_pq(self, pq, node):
        if node not in pq:
            insert_index = 0
            for (index,node_pq) in enumerate(pq):
                if node.cost < node_pq.cost:
                    insert_index = index + 1
            pq.insert(insert_index,node)

    def dijkstr(self, start_node_val):
        path = []
        start_node = self.find_node(start_node_val)
        pq = [start_node]
        start_node.cost = 0
        while pq:
            node = pq.pop()
            node.visited = True
            print('vert: {} {}'.format(node.value,node.cost))
            path.append(node.value)
            for edge in self.edges[node.value]:
                edge_node = self.find_node(edge[0])
                print('edge: {} {}'.format(edge_node.value,edge_node.cost))
                if(not edge_node.visited and node.cost + edge[1] < edge_node.cost):
                    edge_node.cost = node.cost + edge[1]
                    #TODO: set and store predcessor
                    self.insert_in_pq(pq, edge_node)
            print([(nn.value,nn.cost) for nn in pq])
        return path

graph = Graph()
graph.insert_edge(20, 'u', 'v')
graph.insert_edge(10, 'u', 'x')
graph.insert_edge(50, 'u', 'w')
graph.insert_edge(20, 'v', 'x')
graph.insert_edge(30, 'v', 'w')
graph.insert_edge(30, 'x', 'w')
graph.insert_edge(10, 'x', 'y')
graph.insert_edge(10, 'w', 'y')
graph.insert_edge(50, 'w', 'z')
graph.insert_edge(10, 'y', 'z')

print(graph.dijkstr('u'))
