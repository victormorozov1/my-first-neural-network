class Connection:
    def __init__(self, neuron1, neuron2, weight):
        self.neurons = [neuron1, neuron2]
        self.weight = weight

    def count(self):
        self.neurons[1].sum += self.neurons[0].sum * self.weight
