from datetime import datetime

j = 9

start_time = datetime.now()

for i in range(10**8):
    if i % 10 ** 6 == 0:
        print(i / 10**8)
    j += 2

print(datetime.now() - start_time)