from classes import Layer
from constants import IM_SIZE, SECONDARY_LAYER
from functions import set_img_to_layer, set_widths_to_layers


def print_ans(folder_num, file_num):
    l1, l2, l3, l4 = Layer(IM_SIZE ** 2, 0), Layer(SECONDARY_LAYER), Layer(SECONDARY_LAYER), Layer(1)
    l1.set_next_level(l2)
    l2.set_next_level(l3)
    l3.set_next_level(l4)
    full_img_name = f'{folder_num}/{file_num}_resized.bmp'
    set_img_to_layer(l1, full_img_name)
    set_widths_to_layers()
    l1.count_next_level()
    l2.count_next_level()
    l3.count_next_level()
    ans = l4[0]
    print(ans)
    if ans:
        print(f'This number is 2 {round(ans.val, 4) * 100}%')
    else:
        print(f'This number is not 2 {round(1 - ans.val, 4) * 100}%')


def get_inaccuracy(number, layer1, layer2, layer3, layer4):
    layer1.count_next_level()
    layer2.count_next_level()
    layer3.count_next_level()
    ans = layer4[0].val
    print(number, end=' ')
    if str(number) == '2':
        print(1 - ans)
        return 1 - ans
    print(ans)
    return ans


def get_test_inaccuracy(test, l1, l2, l3, l4):
    summ = 0
    for file_name, folder in test:
        set_img_to_layer(l1, file_name)
        res = get_inaccuracy(folder, l1, l2, l3, l4)
        summ += res
    return summ


if __name__ == '__main__':
    number = input('number')
    file_n = input('file number')
    print_ans(number, file_n)