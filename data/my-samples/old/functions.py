def set_file_to_layer(layer, filename):
    f = open(filename, 'r')

    ind = 0
    for line in f.readlines():
        for number in [float(i) for i in line.split()]:
            layer[ind].val = number
            ind += 1
    f.close()


def set_widths_to_layers(l1, l2, l3, l4):
    f = open('widths.txt', 'r')
    arr = [float(i) for i in f.read().split()]
    for i in range(l1.len):
        l1.neurons[i] = arr[i]
    for i in range(l2.len):
        l2.neurons[i] = arr[i + l1.len]
    for i in range(l3.len):
        l3.neurons[i] = arr[i + l1.len + l2.len]
    f.close()
