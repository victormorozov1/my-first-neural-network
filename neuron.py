from activation_function import activation_function
from connection import Connection


class Neuron:
    def __init__(self, next_layer=None, start_k=1):
        self.next_layer = next_layer
        self.sum = 0

        if self.next_layer:
            self.connections = []
            self.make_connections(start_k)

    def count_next_neurons(self):
        for connection in self.connections:
            connection.count()

    def make_connections(self, start_k):
        for neuron in self.next_layer.neurons:
            self.connections.append(Connection(self, neuron, start_k))
