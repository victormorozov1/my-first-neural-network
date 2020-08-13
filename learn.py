from classes.data_set import DataSet
from classes.neural_network import NeuralNetwork

if __name__ == '__main__':
    neural_network = NeuralNetwork(15 ** 2, 15, 2, 2)
    neural_network.learn(data_sets_num=6, data_set_len=4)
    neural_network.save()
