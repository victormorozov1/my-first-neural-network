from random import randrange as rd


all_neurons = []


class Neuron:
    def __init__(self):
        self.val = 0
        self.next_level_len = 0
        all_neurons.append(self)

    def set_next_level(self, next_level):
        self.next_level = next_level
        self.next_level_len = next_level.len
        self.widths = [rd(0, 101) / 100 for i in range(self.next_level_len)]

    def change_val_on(self, d):
        self.val += d
        if self.val > 1:
            self.val = 1
        elif self.val < 0:
            self.val = 0

    def count_next_level(self):
        for i in range(self.next_level_len):
            if self.val >= 0.5:
                self.next_level.neurons[i].change_val_on(self.widths[i])


class Neuronet:
    def __init__(self, len):
        self.len = len
        self.neurons = []
        for i in range(len):
            self.neurons.append(Neuron())

    def set_next_level(self, next_level):
        self.next_level = next_level
        self.next_level_len = next_level.len
        for i in range(self.len):
            self[i].set_next_level(self.next_level)

    def count_next_level(self):
        for neuron in self.neurons:
            neuron.count_next_level()

    def __getitem__(self, key):
        return self.neurons[key]
