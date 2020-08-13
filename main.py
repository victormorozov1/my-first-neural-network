from classes.neural_network import NeuralNetwork
from functions import get_arr_from_im
from PIL import Image


if __name__ == '__main__':
    neural_network = NeuralNetwork(15**2, 15, 2, 2)
    neural_network.load()
    neural_network.set_first_layer(get_arr_from_im(Image.open('data/my-samples/3/5_resized.bmp')))
    neural_network.count()
    print(neural_network.result)