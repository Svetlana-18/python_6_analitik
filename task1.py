# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите вещественное число: "))
numberLengt = len(str(number)) - 2
number = int(number * 10 ** numberLengt)
if number < 0:
    number = number * - 1
sum_digits = 0
while (number != 0):
    sum_digits += (number % 10)
    number = number // 10
print("сумма цифр равна:", sum_digits)