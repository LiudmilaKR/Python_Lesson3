# 1. Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# print(list)
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(f'Сумма элементов списка, стоящих на позициях с нечетным индексом равна {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# list1= []
# print(list)
# mult = 1
# if len(list) % 2 == 0:
#     for i in range(int(len(list) / 2)):
#         mult = list[i] * list[len(list) - i - 1]
#         list1.append(mult)
# else:
#     for i in range(int(len(list) / 2) + 1):
#         mult = list[i] * list[len(list) - i - 1]
#         list1.append(mult)
# print(list1)

# 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной
# части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]
# list1 = []
# print(list)
# temp = 0
# for i in range(len(list)):
#     list1.append(round(list[i] - int(list[i]), 2))
# min = list1[0]
# max = list1[0]
# for i in range(1, len(list1)):
#     if list1[i] != 0:
#         if list1[i] < min:
#             min = list1[i]
#         elif list1[i] > max:
#             max = list1[i]
# print(f'Разница составляет {max - min}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number10 = int(input('Введите десятичное число: '))
# number2 = ''
# while number10 / 2 > 0:
#     number2 = str(number10 - (number10 // 2) * 2) + number2
#     number10 = number10 // 2
# print(f'Введенное число в двоичной системе {number2}')

# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи

# number = int(input('Введите число: '))
# list = []
# list1 = []

# def fib(N):
#     if N == 1 or N == 2:
#         return 1
#     else:
#         return fib(N - 1) + fib(N - 2)

# for i in range(1, number + 1):
#     list.append(fib(i))

# for i in range(number, 1, -1):
#     if i % 2 == 0:
#         list1.append(-1 * fib(i))
#     else:
#         list1.append(fib(i))

# print(list1 + [0] + list)