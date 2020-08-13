from layer import Layer


class Neuronet:
    def __init__(self, *args):
        self.layers = []
        for layer_len in args:
            self.layers.append(Layer(int(layer_len)))

        for i in range(len(self.layers) - 1):
            self.layers[i].set_next_level(self.layers[i + 1], rd_range=(100 / self.layers[i + 1].len))

    def __str__(self):



