from random import randrange as rd


all_neurons = []


class Neuron:
    def __init__(self, when_val_is_one=0.5):
        self.val = 0
        self.next_level_len = 0
        self.when_val_is_one = when_val_is_one
        self.widths = []
        self.next_level = None

        all_neurons.append(self)

    def set_next_level(self, next_level, rd_range=20):
        self.next_level = next_level
        self.next_level_len = next_level.len
        self.widths = [rd(0, rd_range) / 100 for i in range(self.next_level_len)]
        #print('---------------------')
        #print(self.widths)
        #print('---------------------')

    def set_val(self, val):
        self.val = val
        if self.val > 1:
            self.val = 1
        elif self.val < 0:
            self.val = 0

    def change_val_on(self, d):
        self.set_val(self.val + d)

    def count_next_level(self):
        for i in range(self.next_level_len):
            if self:
                self.next_level.neurons[i].change_val_on(self.widths[i])

    def set_width(self, ind, c):
        self[ind] = c
        if self[ind] > 1:
            self[ind] = 1
        elif self[ind] < 0:
            self[ind] = 0

    def change_width_on(self, ind, c):
        self.set_width(ind, self[ind] + c)

    def print(self, *args, one_string=False, print_name=True):
        if print_name:
            print('Neuron')
        if args == []:
            args = ['val', 'when_val_is_one', 'widths']
        for i in args:
            if one_string:
                exec(f'print("self.{i} ==", self.{i}, end="  ")')
            else:
                exec(f'print("self.{i} ==", self.{i})')
        if one_string:
            print()

    def __getitem__(self, key):
        return self.widths[key]

    def __setitem__(self, key, val):
        self.widths[key] = val

    def __bool__(self):
        return bool(self.val >= self.when_val_is_one)

    def __len__(self):
        return len(self.widths)

    def __str__(self):
        return f'Neuron val={self.val}'