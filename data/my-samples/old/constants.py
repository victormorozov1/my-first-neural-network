IM_SIZE = 15
SECONDARY_LAYER = 8
O = 4 * 10 ** 6
T = 50
S = 0.1

edges = IM_SIZE ** 2 * SECONDARY_LAYER + SECONDARY_LAYER ** 2 + SECONDARY_LAYER
time_on_test = edges / S * 2 * edges

all_time = time_on_test * T / O

print('Предположительное время работы программы:', all_time / 60 / 3, 'minutes')