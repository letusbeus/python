# refactoring, map
# Было:
# print('8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У')
# point = input("Enter 2 point separated by a space: ").split()
# x = (list(map(int, point)))[0]
# y = (list(map(int, point)))[1]
# if x == 0 and y != 0:
#     print('The point lies on the x-axis')
# elif y == 0 and x != 0:
#     print('The point lies on the y-axis')
# elif x > 0:
#     if y > 0:
#         print('1st quarter coordinate plane')
#     else:
#         print('4th quarter coordinate plane')
# elif x < 0:
#     if y > 0:
#         print('2nd quarter coordinate plane')
#     else:
#         print('3rd quarter coordinate plane')
# else:
#     print('The point is null')
# Стало:
print('8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У')
point = input("Enter 2 point separated by a space: ").split()
x, y = list(map(int, point))
if x == 0 and y != 0:
    print('The point lies on the x-axis')
elif y == 0 and x != 0:
    print('The point lies on the y-axis')
elif x > 0:
    print('1st quarter coordinate plane') if y > 0 else print('4th quarter coordinate plane')
elif x < 0:
    print('2nd quarter coordinate plane') if y > 0 else print('3rd quarter coordinate plane')
else:
    print('The point is null')

# map
# # Было:
# print('\n10. Найти расстояние между двумя точками пространства')
# import math
#
# point_1 = input("Enter 3 coordinates of X separated by a space: ").split()
# point_2 = input("Enter 3 coordinates of Y separated by a space: ").split()
# x = list(map(int, point_1))
# y = list(map(int, point_2))
# print('Distance between X and Y is %.2f' % math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2))
# Стало:
print('\n10. Найти расстояние между двумя точками пространства')
import math

a, b, c = list(map(int, input("Enter 3 coordinates of X separated by a space: ").split()))
x, y, z = list(map(int, input("Enter 3 coordinates of Y separated by a space: ").split()))
print('Distance between X and Y is %.2f' % math.sqrt((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2))

# enumerate
# Было:
# print('\n22. Найти сумму чисел списка стоящих на нечетной позиции')
# # F.E. 45 23 6 11 9 31
# input_list = list(map(int, input("Enter the list of numbers separated by a space: ").split()))
# sum_of_even = 0
# for i in range(len(input_list)):
#     if i % 2 != 0:
#         sum_of_even += input_list[i]
# print(sum_of_even)
# Стало:
print('\n22. Найти сумму чисел списка стоящих на нечетной позиции')
# F.E. 45 23 6 11 9 31
input_list = list(map(int, input("Enter the list of numbers separated by a space: ").split()))
sum_of_even = 0
for idx, i in enumerate(input_list):
    if idx % 2 != 0:
        sum_of_even += i
print(sum_of_even) # удобная штука, оказывается :)

# list comprehensions
# Было:
# print('32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.'
#       '\n    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]')
# # F.E. 1 2 3 5 1 5 3 10
# given_list = list(map(int, input('Enter the numbers separated by a space: ').split()))
# output_list = []
# for i in given_list:
#     if i not in output_list:
#         output_list.append(i)
#     else:
#         continue
# print(output_list)
# Стало:
print('32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.'
      '\n    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]')
# F.E. 1 2 3 5 1 5 3 10
given_list = list(map(int, input('Enter the numbers separated by a space: ').split()))
output_list = [i for i in set(given_list)]
print(output_list)

# filter, lambda
# Было:
# print('38. Напишите программу, удаляющую из текста все слова содержащие "абв".')
# text = 'аб дыабв абыгн зыабв абв'
# frag = 'абв'
# print("Original text: {:>32s}\n".format(text) + "Fragment to delete: {:>6s}".format(frag))
# output_string = ''
# for i in list(text.split()):
#     if frag not in i:
#         output_string += f'{i} '
# print("The edited text: {:>14s}".format(output_string.rstrip()))
# Стало:
print('38. Напишите программу, удаляющую из текста все слова содержащие "абв".')
text = 'аб дыабв абыгн зыабв абв'
frag = 'абв'
print("Original text: {:>32s}\n".format(text) + "Fragment to delete: {:>6s}".format(frag))
text = list(text.split())
print(*list(filter(lambda x: not x.__contains__(frag), text)))
