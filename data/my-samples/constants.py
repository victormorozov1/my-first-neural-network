IM_SIZE = 15
SECONDARY_LAYER = 8
O = 4 * 10 ** 6
T = 50
S = 0.1

edges = IM_SIZE ** 2 * SECONDARY_LAYER + SECONDARY_LAYER ** 2 + SECONDARY_LAYER
k = 0.0000000022

print('Предположительное время работы программы:', int(T * edges ** 2 / S * k), 'minutes')