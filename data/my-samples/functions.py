from classes import all_neurons
from PIL import Image
from constants import IM_SIZE


def set_widths_to_layers():
    f = open('widths.txt', 'r')
    arr = [float(i) for i in f.read().split()]
    print(len(arr), len(all_neurons))
    arr_ind = 0

    for neuron in all_neurons:
        for i in range(len(neuron)):
            neuron[i] = arr[arr_ind]
            arr_ind += 1

    f.close()


def set_arr_to_layer(layer, arr):
    layer_ind = 0
    for i in range(len(arr)):
        if isinstance(i, float) or isinstance(i, int):
            layer.neurons[layer_ind].val = arr[i]
            layer_ind += 1
        else:
            for j in range(len(arr[i])):
                layer.neurons[layer_ind].val = arr[i][j]
                layer_ind += 1


def set_img_to_layer(layer, img_filename):
    im = Image.open(img_filename)
    pixels = im.load()
    szx, szy = im.size
    arr = []
    for i in range(szx):
        for j in range(szy):
            arr.append(1 - sum(pixels[i, j]) / 255 / 3)
    set_arr_to_layer(layer, arr)


def cut_img(img_filename):
    im = Image.open(img_filename)
    pixels = im.load()
    sz_x, sz_y = im.size
    x1, y1, x2, y2 = 0, 0, sz_x - 1, sz_y - 1
    while all([pixels[x1, y3] == (255, 255, 255) for y3 in range(0, sz_y)]) and x1 < sz_x - 1:
        x1 += 1
    while all([pixels[x2, y3] == (255, 255, 255) for y3 in range(0, sz_y)]) and x2 > 0:
        x2 -= 1
    while all([pixels[x3, y1] == (255, 255, 255) for x3 in range(0, sz_x)]) and y1 < sz_y - 1:
        y1 += 1
    while all([pixels[x3, y2] == (255, 255, 255) for x3 in range(0, sz_x)]) and y2 > 0:
        y2 -= 1

    cutted_im = Image.new("RGB", (x2 - x1 + 1, y2 - y1 + 1), (255, 255, 255))

    pixels2 = cutted_im.load()
    cutted_im_sz_x, cutted_im_sz_y = cutted_im.size
    for x in range(cutted_im_sz_x):
        for y in range(cutted_im_sz_y):
            pixels2[x, y] = pixels[x + x1, y + y1]

    cutted_im.save(img_filename.split('.') + '_cutted.' + img_filename.split('.')[1])


def resize_img(img_filename):
    im = Image.open(img_filename)
    im = im.resize((IM_SIZE, IM_SIZE))
    im.save(img_filename.split('.')[0] + '_resized.' + img_filename.split('.')[1])

