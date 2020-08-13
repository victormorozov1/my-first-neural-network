from PIL import Image
import os


IM_SZ = 22


def get_im_sz(szx, szy):
    k = 1
    while IM_SZ ** 2 < int(szx * k) * int(szy * k):
        k -= 0.01
    return int(szx * k), int(szy * k)


def convert_img_to_txt(folder, file):
    im = Image.open(folder + '/' + file + '.bmp')
    f = open(f'text/{folder}/{file}.bmp')
    pixels = im.load()
    szx, szy = im.size
    for x in range(szx):
        for y in range(szy):
            k = round(1 - sum(pixels[x, y]) / 255 / 3, 6)
            f.write(str(k) + ' ')
        f.write('\n')
    f.close()


if __name__ == '__main__':
    for folder in ([str(i) for i in range(10)] + ['caraculi']):
        print(folder)
        for file in os.listdir(path=folder):
            if '_resized' in file:
                print(file)
                convert_img_to_txt(folder, file.split('.')[0])

