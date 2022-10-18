# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


count = int(input('Введите число N: '))
if count <= 0:
    print('Неверный ввод, введите целое положительное число')
else:
    numberslist = [round(((1+1/i)**i), 2) for i in range(1, count + 1)]
    result = sum(numberslist)
    print(numberslist, result)
   


# numberslist = []
# result = 0
# count = int(input('Введите число N: '))
# if count <= 0:
#     print('Неверный ввод, введите целое положительное число')
# else:
#     for i in range(1, count + 1):
#         numbers = (round((1 + 1/i) ** i))
#         numberslist.append(numbers)
#         result += numbers
#     print(numberslist)
#     print(result)


