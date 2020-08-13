from classes import Layer, all_neurons
from constants import IM_SIZE, SECONDARY_LAYER, S
import os
from numpy import arange
from get_ans import get_inaccuracy
from functions import set_img_to_layer


layer1, layer2, layer3, layer4 = layer(IM_SIZE ** 2), layer(SECONDARY_LAYER), layer(SECONDARY_LAYER), layer(
    1)

layer1.set_next_level(layer2)
layer2.set_next_level(layer3)
layer3.set_next_level(layer4)

for folder in filter(lambda i: '.' not in i, os.listdir(path='text')):
    print(folder)
    for file in os.listdir(path=f'text/{folder}'):
        full_file = f'{folder}/{file}'
        set_file_to_layer(layer1, full_file)

        best_result = get_ans(folder, layer1, layer2, layer3, layer4)
        learned_neurons = 0
        for neuron in all_neurons:
            old_val = neuron.val
            neuron.val = 0
            for new_val in arange(0, 1.0001, S):
                neuron.val = new_val
                result = get_ans(folder, layer1, layer2, layer3, layer4)
                if result > best_result:
                    old_val = new_val
                    best_result = result
            neuron.val = old_val

            learned_neurons += 1


f = open('widths.txt', 'w')
for neuron in all_neurons:
    f.write(str(neuron.val) + ' ')
f.close()