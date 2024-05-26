import random

k_list = []
for li in range(1, 101):
    k_list.append(li)

d_dict = {}
for j in k_list:
    x = random.randint(101, 999)
    d_dict[j] = x

for k in d_dict.keys():
    print('Ключ =', k,': Значение =', d_dict.get(k))

for i in k_list:
    d_dict.pop(i)

print(d_dict)
