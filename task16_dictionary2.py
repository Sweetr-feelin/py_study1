import random

list = []
for li in range(1, 101):
    x = random.randint(1,10)
    list.append(x)

def dict2(list, n):
    d_dict = {}
    result = []
    for i in list:
        if i in d_dict:
            d_dict[i] = d_dict.get(i) + 1
        else:
            d_dict[i] = 1

    for k in d_dict.keys():
        if d_dict.get(k) >= n:
            result.append(k)
    return result
