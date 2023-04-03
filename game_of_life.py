import random
percent = 40
height = 5
width = 5
iterations = 10
y = height*width
x = percent*y/100
one = 0
zero = 0
table = {a: [] for a in range(height*width)}
num = 0
while y > 0:
    z = random.randint(1, y)
    y -= 1
    if z > x:
        zero += 1
        table[num] = '.'
    else:
        x -= 1
        one += 1
        table[num] = '@'
    num += 1

t = 0
while t < height:
    for i in range(t*width, (t+1)*width):
        print(table[i], ' ', end='')
    print('')
    t += 1
print('ones:', one, 'zeros:', zero)

for it in range(iterations):
    t_int = {a: [] for a in range(height*width)}
    for i in range(width*height):
        alive = 0
        for j in range(0, 10):
            if i + (width * (j % 3 - 1)) + (j // 3 - 1) in range(0, width*height):
                if i % width-(i + (width * (j % 3 - 1)) + (j // 3 - 1)) % width in range(-1, 2):
                    if table[i + (width * (j % 3 - 1)) + (j // 3 - 1)][0] == '@':
                        alive += 1
                    else:
                        continue
                else:
                    continue
            else:
                continue
        if table[i] == '@':
            if alive in range(3, 5):
                t_int[i] = '@'
            else:
                t_int[i] = '.'
        else:
            if alive == 3:
                t_int[i] = '@'
            else:
                t_int[i] = '.'
    table = t_int
    t = 0
    while t < height:
        for i in range(t*width, (t+1)*width):
            print(table[i], ' ', end='')
        print('')
        t += 1
    print('')