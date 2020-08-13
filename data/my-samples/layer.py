class Layer:
    def __init__(self, len, when_val_is_one=0.5):
        self.len = len
        self.neurons = []
        for i in range(len):
            self.neurons.append(Neuron(when_val_is_one=when_val_is_one))
        self.next_level = None
        self.next_level_len = 0

    def set_next_level(self, next_level, rd_range=100):
        self.next_level = next_level
        self.next_level_len = next_level.len
        for neuron in self.neurons:
            neuron.set_next_level(self.next_level, rd_range=rd_range)

    def count_next_level(self):
        self.next_level.set_zero()
        for neuron in self.neurons:
            neuron.count_next_level()

    def set_zero(self):
        for neuron in self.neurons:
            neuron.set_val(0)

    def print(self, *layer_methods, neuron_methods=['val', 'when_val_is_one', 'widths']):
        print('Layer')
        if not layer_methods:
            layer_methods = ['len', 'neurons']
        for i in layer_methods:
            if i == 'neurons':
                print('self.neurons:')
                for neuron in self.neurons:
                    print('  ', end='')
                    neuron.print(*neuron_methods, one_string=True, print_name=False)
            else:
                exec(f'print("self.{i} ==", self.{i})')

    def __getitem__(self, key):
        return self.neurons[key]

    def __setitem__(self, key, val):
        if isinstance(val, int):
            self.neurons[key].val = val
        else:
            self.neurons[key] = val

    def __len__(self):
        return len(self.neurons)

    def __str__(self):
        return f'layer: {[i.val for i in self.neurons]}'
