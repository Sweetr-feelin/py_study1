import os.path

def cat_n_files_task1(main_root, format, flag):
    list = []
    key_files = []
    result = []
    for i in os.listdir(main_root):
        lvl1 = i.split('.')
        path1 = os.path.join(main_root, lvl1[0])

        if os.path.exists(path1):
            list.append(path1)
            if (flag):
                for j in os.listdir(path1):
                    lvl2 = j.split('.')
                    path2 = os.path.join(path1, lvl2[0])
                    if os.path.exists(path2):
                        list.append(lvl2[0])
                    elif lvl2[1] == format:
                        key_files.append(j)
        elif lvl1[1] == format:
            key_files.append(i)
    result.append(list)
    result.append(key_files)
    return result
