from classes import Neuronet
from constants import IM_SIZE, SECONDARY_LAYER
from functions import set_file_to_layer, set_widths_to_layers


def get_ans(number, layer1, layer2, layer3, layer4):
    layer1.count_next_level()
    layer2.count_next_level()
    layer3.count_next_level()
    ans = layer4[0].val
    if str(number) == '2':
        return 1 - ans
    return ans


if __name__ == '__main__':
    number = input('number')
    file_n = input('file number')
    l1, l2, l3, l4 = Neuronet(IM_SIZE ** 2), Neuronet(SECONDARY_LAYER), Neuronet(SECONDARY_LAYER), Neuronet(1)
    set_widths_to_layers(l1, l2, l3, l4)
    set_file_to_layer(l1, f'text/{number}/{file_n}.txt')
    print(get_ans(number, l1, l2, l3, l4))