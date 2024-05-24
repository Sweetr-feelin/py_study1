import os.path
from zipfile import ZipFile

def add_to_zip(name, format):
    root = 'test_zip'
    fi = open(name, 'wt')
    for i in os.listdir(root):
        n_part = i.split('.')
        path = os.path.join(root, n_part[0])
        if not os.path.exists(path) and n_part[1] == format:
            fi_name = n_part[0] + '.' + n_part[1]
            with ZipFile(name, 'a') as testzip:
                testzip.write(fi_name)

    fi.close()
