from classes import Layer, all_neurons
from constants import IM_SIZE, SECONDARY_LAYER, S
import os
import numpy as np
from get_ans import get_inaccuracy, get_test_inaccuracy
from functions import set_img_to_layer, set_widths_to_layers
import datetime
from time import sleep
import random


def get_all_pictures_names():
    all_pictures_names = []
    a1, a2 = [], []
    for folder in filter(lambda i: '.' not in i, os.listdir()):
        for file in filter(lambda x: 'resized' in x, os.listdir(path=f'{folder}')):
            full_file = f'{folder}/{file}'
            if folder != '2':
                a1.append((full_file, folder))
            else:
                a2.append((full_file, folder))
    while a1 and a2:
        all_pictures_names.append(a1[0])
        all_pictures_names.append(a2[0])
        del a1[0]
        del a2[0]
    return all_pictures_names


def get_tests():
    tests = []
    all_pictures_names = get_all_pictures_names()
    for i in range(0, len(all_pictures_names), 4):
        tests.append((all_pictures_names[0], all_pictures_names[1], all_pictures_names[2], all_pictures_names[3]))
    return tests


def try_to_change_width(neuron, s, w_ind, l1, l2, l3, l4, n):
    #print('old w =', neuron[w_ind])
    old_w = neuron[w_ind]
    old_result = get_inaccuracy(n, l1, l2, l3, l4)
    neuron.change_width_on(w_ind, s)
    new_result = get_inaccuracy(n, l1, l2, l3, l4)
    #sleep(1)
    if new_result < old_result:
        print('change w to', neuron[w_ind])
        return True

    #print('neuron w not changed')
    neuron.set_width(w_ind, old_w)
    return False


start_time = datetime.datetime.now()
import_old_widths = not input('Do you want to import old widths?').lower() == 'n'


layer1, layer2, layer3, layer4 = Layer(IM_SIZE ** 2), Layer(SECONDARY_LAYER), Layer(SECONDARY_LAYER), Layer(
    1)

layer1.set_next_level(layer2)
layer2.set_next_level(layer3)
layer3.set_next_level(layer4)

if import_old_widths:
    set_widths_to_layers()

for test in get_tests():
    global best_w, best_result

    for neuron in all_neurons:
        for w_ind in range(len(neuron)):
            best_result = 8
            for new_w in np.arange(max(0, neuron[w_ind] - S), min(1, neuron[w_ind] + S + 0.00001), S):
                neuron[w_ind] = new_w
                current_result = get_test_inaccuracy(test, layer1, layer2, layer3, layer4)
                if current_result < best_result:
                    best_result = current_result
                    best_w = new_w

            neuron[w_ind] = best_w

    print(get_test_inaccuracy(test, layer1, layer2, layer3, layer4) / 4)


f = open('widths.txt', 'w')
for neuron in all_neurons:
    for w in neuron.widths:
        f.write(str(w) + ' ')
f.close()

print('Работа программы завершена за', datetime.datetime.now() - start_time, 'seconds')
