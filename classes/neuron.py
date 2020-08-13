from classes.connection import Connection


class Neuron:
    def __init__(self, all_connections, next_layer=None, start_k=1):
        self.all_connections = all_connections

        self.next_layer = next_layer
        self.sum = 0

        print('next layer = ', next_layer)
        if self.next_layer:
            print('creating connections')
            self.connections = []
            self.make_connections(start_k)

    def count_next_neurons(self):
        for connection in self.connections:
            connection.count()

    def make_connections(self, start_k):
        for neuron in self.next_layer.neurons:
            self.connections.append(Connection(self, neuron, start_k))
            self.all_connections.append(self.connections[-1])
