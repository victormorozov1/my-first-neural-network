import os

n = 19
for i in os.listdir():
    if 'копия' in i:
        os.rename(i, str(n) + '.bmp')
        n += 1