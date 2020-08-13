from classes.data_set import DataSet
from classes.layer import Layer
from random import randrange as rd


class NeuralNetwork:
    def __init__(self, input_layer_n, hidden_layer_n, output_layer_n, hidden_layers_num):
        self.all_connections = []

        self.output_layer = Layer(output_layer_n, self.all_connections)

        self.hidden_layers = []
        self.hidden_layers_num = hidden_layers_num
        for i in range(self.hidden_layers_num):
            if i == 0:
                self.hidden_layers.append(
                    Layer(hidden_layer_n, self.all_connections, next_layer=self.output_layer))
            else:
                self.hidden_layers.append(
                    Layer(hidden_layer_n, self.all_connections, next_layer=self.hidden_layers[i - 1]))
        self.hidden_layers = self.hidden_layers[::-1]  # maybe it will be better to delete this string

        self.input_layer = Layer(input_layer_n, self.all_connections, next_layer=self.hidden_layers[0])

        self.test_percent = None  # результат финального тестирования
        self.last_percent = 0  # последний результат обучающего тестирования. Должен стать 100%

        self.result = None

    def set_first_layer(self, arr):  # arr - массив чисел
        n, m = len(arr), len(arr[0])
        for i in range(n):
            for j in range(m):
                layer_ind = i * n + j
                self.input_layer[layer_ind] = arr[i][j]

    def count(self):
        self.input_layer.count_next_layer()

        for hidden_layer in self.hidden_layers:
            hidden_layer.count_next_layer()

        self.count_result()

    def count_result(self):
        max_val, self.result = -999999999, None
        for i in range(self.output_layer.n):
            sum = self.output_layer[i].sum
            if sum > max_val:
                max_val = sum
                self.result = i + 3  # !!!!!!!!!! Это нужно будет убрать

    def result_percent_right(self, right_answer):
        if right_answer == 3:
            return self.output_layer[0].sum - self.output_layer[1].sum
        return self.output_layer[1].sum - self.output_layer[0].sum

    def clear(self, clear_input_layer=True):
        if clear_input_layer:
            self.input_layer.clear()

        for hidden_layer in self.hidden_layers:
            hidden_layer.clear()

        self.output_layer.clear()

    def learn(self, data_set_len=10, data_sets_num=100):
        print('learn started')

        for i in range(data_sets_num):
            print(f'{round(i / data_sets_num * 100, 2)}% of learning completed')
            self.learn_iteration(data_set_len)
            self.save()

    def learn_iteration(self, data_set_len):
        data_set = DataSet(data_set_len)  # !!! возможно новый дата-сет нужно
        #                                       обновлять перед проверкой каждого
        #                                       нейрона
        debug_i = 0
        for connection in self.all_connections:
            print(debug_i / len(self.all_connections) * 100)
            self.find_best_weight(connection, data_set)
            debug_i += 1

    def try_to_change(self, connection, data_set):
        old_val, connection.weight = connection.weight, rd(-100, 101) / 100
        if data_set.test(self) < self.last_percent:
            connection.weight = old_val

    def find_best_weight(self, connection, data_set):
        best_res, best_val = (0, 0), None

        for val in [i / 10 for i in range(-10, 11)]:
            connection.weight = val
            curr_res = data_set.test(self)
            if curr_res[0] * curr_res[1] > best_res[0] * best_res[1]:
                best_res = curr_res
                best_val = val

        if best_val:
            connection.weight = best_val

        print('current res =', best_res)

    def save(self, filename='neural_network.txt'):
        f = open(filename, 'w')
        for connection in self.all_connections:
            f.write(str(connection.weight) + ' ')
        f.close()

    def load(self, filename='neural_network.txt'):
        f = open(filename, 'r')
        string_weights = f.read().split(' ')
        for i in range(len(self.all_connections)):
            self.all_connections[i].weight = float(string_weights[i])
