from random import randint

n = 10

while n != 0:
    count = n
    name = str(count) + '.txt'
    fi = open(name, 'wt')

    for i in range(3):
        x = randint(1, 9)
        s = str(x) + '\n'
        fi.write(s)

    fi.close()
    n -= 1
