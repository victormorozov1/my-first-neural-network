from mnist import MNIST
from random import randrange as rd
from PIL import Image


class DataSet:
    def __init__(self, tests_num):
        self.tests_num = tests_num

        self.tests_arr = []
        self.create_tests_arr()

    def create_tests_arr(self, using_numbers=[3, 4]):
        for i in range(self.tests_num):
            print('i =', i)
            number = using_numbers[i % len(using_numbers)]
            print('number =', number)
            file_index = i // len(using_numbers) + 1
            arr = []

            image = Image.open(f'data/my-samples/{number}/{file_index}_resized.bmp')
            width, height = image.size
            pixels = image.load()

            for y in range(height):
                arr.append([])
                for x in range(width):
                    arr[-1].append(round((255 * 3 - sum(pixels[x, y])) / 255 * 3, 2))

            self.tests_arr.append([arr, number])
    
    def test(self, neural_network):
        right_answers = 0
        right_k = 0
        
        for test in self:
            neural_network.clear(clear_input_layer=False)  # Не чистим первый слой так как собираемся сразу его заполнить
            neural_network.set_first_layer(test[0])

            neural_network.count()
            right_k += neural_network.result_percent_right(test[1])
            if neural_network.result == test[1]:
                right_answers += 1
            
        return right_answers, right_k
    
    def __getitem__(self, item):
        return self.tests_arr[item]

    def __iter__(self):
        return iter(self.tests_arr)


if __name__ == '__main__':
    ds = DataSet(3)
    for test in ds:
        print('right answer', test[1])
        for line in test[0]:
            print(line)
        print('\n')
