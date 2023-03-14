# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
my_list = list(random.randint(- 30, 30) for _ in range(20))
print(my_list)
num_min = 5
num_max = 15
def sort_list(in_list):
    if (in_list in range(num_min, num_max + 1)):
        return True
    else:
        return False
new_range_list = filter(sort_list, my_list)
new_range_list = list(map(int, new_range_list))
print(new_range_list)

for i in range(len(my_list)):
    for j in range(len(new_range_list)):
        if my_list[i] == new_range_list[j]:
            print(i)