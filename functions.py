def get_arr_from_im(image):
    width, height = image.size
    pixels = image.load()
    arr = []

    for y in range(height):
        arr.append([])
        for x in range(width):
            arr[-1].append(round((255 * 3 - sum(pixels[x, y])) / 255 * 3, 2))

    return arr
