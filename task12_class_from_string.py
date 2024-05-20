def class_from_string(name):
    objs = []
    with open(name, 'rt') as fi:
        s = fi.readline()
        while s != '':
            s = s.rstrip()
            words = s.split(' ')

            try:
                words[1] = float(words[1])
                words[2] = int(words[2])
            except:
                print('Неверный формат')
                break

            objs.append('Cat(')
            objs.append(words)
            objs.append(')')
            s = fi.readline()
