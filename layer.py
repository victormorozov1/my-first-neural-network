from neuron import Neuron


class Layer:
    def __init__(self, n, next_layer=None, start_k=1):
        self.neurons = []
        self.n = n

        for i in range(self.n):
            self.neurons.append(Neuron(next_layer=next_layer, start_k=start_k))

    def count_next_layer(self):
        for neuron in self.neurons:
            neuron.count_next_neurons()

    def __getitem__(self, item):
        return self.neurons[item]

    def __setitem__(self, key, val):
        self.neurons[key].sum = val

    def __iter__(self):
        return iter(self.neurons)


if __name__ == '__main__':
    l3 = Layer(2)
    l2 = Layer(2, l3)
    l1 = Layer(3, l2)

    for neuron in l1:
        neuron.sum = 0.1

    l1.count_next_layer()
    l2.count_next_layer()
    print(l3[0].sum, l3[1].sum)
