# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def input_list(count):
    if count < 1:
        return 'Error'
    return sample(range(1, count * 2), count)


count = (int(input('Введите длину списка  ')))
res = input_list(count)
print(res)

result = sum([res[x] for x in range(0, count, 2)])
print(result)

# from random import sample


# def creat__list(count):
#     if count < 1:
#         return 'Error'
#     new_list = sample(range(1, count * 2), count)
#     return new_list


# def sum_elem(worker_list):
#     result = 0
#     for i in range(0, len(worker_list), 2):
#         result += worker_list[i]
#     return result


# res = creat__list(int(input('Введите длину списка  ')))
# print(res)
# print(sum_elem(res))
