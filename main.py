from classes.neural_network import NeuralNetwork
from functions import get_arr_from_im
from PIL import Image
from random import randrange as rd

if __name__ == '__main__':
    neural_network = NeuralNetwork(15**2, 15, 2, 2)
    neural_network.load()

    number = rd(3, 5)
    ind = rd(20, 40)
    resized_im = Image.open(f'data/{number}/{ind}_resized.bmp')
    im = Image.open(f'data/{number}/{ind}.bmp')

    neural_network.set_first_layer(get_arr_from_im(resized_im))
    neural_network.count()

    print('This is number', neural_network.result)
    im.show()

    neural_network.clear()
