class Connection:
    def __init__(self, neuron1, neuron2, weight):
        self.neurons = [neuron1, neuron2]
        self.weight = weight

    def count(self):
        self.neurons[1].sum += self.neurons[0].sum * self.weight

    def __add__(self, other):
        return Connection(*self.neurons, self.weight+other)

    def __sub__(self, other):
        return Connection(*self.neurons, self.weight + other)

    def __iadd__(self, other):
        self.weight += other
        return self

    def __isub__(self, other):
        self.weight -= other
        return self

    def __str__(self):
        return f'Connection, weight={self.weight}'


if __name__ == '__main__':
    from classes.neuron import Neuron

    c = Connection(Neuron(), Neuron(), 1)
    c = 4
    print(c)
    c -= 0.5
    print(c)
    c += 0.1
    print(c)
    print()