from PIL import Image
import os

if __name__ == '__main__':
    dir = 'data/'
    num = '3/'
    dir += num
    for i in range(200):
        filename = f'{i}.bmp'
        if filename not in os.listdir(dir):
            im = Image.new('RGB', (500, 500), color=(255, 255, 255))
            im.save(dir + filename)
