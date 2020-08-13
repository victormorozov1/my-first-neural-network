from PIL import Image


def cut_image(im):
    width, height = im.size
    pixels = im.load()

    left_x, up_y = 0, 0
    right_x, down_y = width - 1, height - 1

    while all([pixels[left_x, y] == (255, 255, 255) for y in range(height)]):
        left_x += 1

    while all([pixels[right_x, y] == (255, 255, 255) for y in range(height)]):
        right_x -= 1

    while all([pixels[x, up_y] == (255, 255, 255) for x in range(width)]):
        up_y += 1

    while all([pixels[x, down_y] == (255, 255, 255) for x in range(width)]):
        down_y -= 1

    return im.crop((left_x, up_y, right_x, down_y))


if __name__ == '__main__':
    num = '3'
    for i in range(20, 40):
        im = Image.open(f'data/{num}/{i}.bmp')
        pixels = im.load()
        width, height = im.size

        im = cut_image(im)
        im = im.resize((15, 15))
        im.save(f'data/{num}/{i}_resized.bmp')


