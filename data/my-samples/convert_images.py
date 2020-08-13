from PIL import Image
import os
from constants import IM_SIZE as IM_SZ


def get_im_sz(szx, szy):
    k = 1
    while IM_SZ ** 2 < int(szx * k) * int(szy * k):
        k -= 0.01
    return int(szx * k), int(szy * k)


if __name__ == '__main__':
    for folder in ([str(i) for i in range(10)] + ['caraculi']):
        print(folder)
        for file in os.listdir(path=folder):
            if len(file.split('.')[0]) in [1, 2]:
                print(file)

                im = Image.open(folder + '\\' + file)
                pixels = im.load()
                sz_x, sz_y = im.size
                x1, y1, x2, y2 = 0, 0, sz_x - 1, sz_y - 1
                while all([pixels[x1, y3] == (255, 255, 255) for y3 in range(0, sz_y)]) and x1 < sz_x - 1:
                    x1 += 1
                while all([pixels[x2, y3] == (255, 255, 255) for y3 in range(0, sz_y)]) and x2 > 0:
                    x2 -= 1
                while all([pixels[x3, y1] == (255, 255, 255) for x3 in range(0, sz_x)]) and y1 < sz_y - 1:
                    y1 += 1
                while all([pixels[x3, y2] == (255, 255, 255) for x3 in range(0, sz_x)]) and y2 > 0:
                    y2 -= 1

                cutted_im = Image.new("RGB", (x2 - x1 + 1, y2 - y1 + 1), (255, 255, 255))
                pixels2 = cutted_im.load()
                cutted_im_sz_x, cutted_im_sz_y = cutted_im.size
                for x in range(cutted_im_sz_x):
                    for y in range(cutted_im_sz_y):
                        pixels2[x, y] = pixels[x + x1, y + y1]
                cutted_im.save(folder + '\\' + file.split('.')[0] + '_cutted.' + file.split('.')[1])

                im = Image.open(folder + '\\' + file.strip('.')[0] + '_cutted.' + file.split('.')[1])
                pixels = im.load()
                im = im.resize((IM_SZ, IM_SZ))
                im.save(folder + '\\' + file.split('.')[0] + '_resized.' + file.split('.')[1])
            elif file.count('_') >= 2:
                os.remove(folder + '\\' + file)

