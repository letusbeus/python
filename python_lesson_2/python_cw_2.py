# 11.
print('11. Сформировать список из  N членов последовательности.'
      '\n    Для N = 5: 1, -3, 9, -27, 81 и т.д.')
output_list = []
for i in range(int(input("Enter the number: "))):
    output_list.append((-3)**i)
print(*output_list, sep=', ')

# 12.
print('12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.'
      '\n    Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}')
output_dict = {}
for i in range(1, int(input("Enter the number: ")) + 1):
    output_dict.setdefault(i, i * 3 + 1)
print(output_dict)

# 13.1
print('Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.')
print('There\'re', input("Enter your string: ").count(input("Enter the substring: ")), 'substrings in your string')

# 13.2
print('Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.')
str_1 = 'Lorem ipsum dolor sit amet'
str_2 = 'or'
counter = str_1.count(str_2)
print(f'There\'re {counter} substrings in your string')

# 16
print('16. Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму')
len_of_list = input('Enter the number of elements: ')
list_of_numbers = []
if len_of_list.isdigit():
    len_of_list = int(len_of_list)
    for i in range(1, len_of_list + 1):
        list_of_numbers.append((1 + 1 / i) ** i)
else:
    print('Please check if the entered value is a number')
print(sum(list_of_numbers))

# 17.
print('17. Задать список из N элементов, заполненных числами из [-N, N].'
      '\n    Найти произведение элементов на указанных позициях.'
      '\n    Позиции хранятся в файле file.txt в одной строке одно число')

import math

len_of_multiply_list = int(input())
list_for_multiply = []
indexes = []
nums_for_multiply = []
result = 1

for i in range(-len_of_multiply_list, len_of_multiply_list + 1):
    list_for_multiply.append(i)
print(list_for_multiply)
with open(r"D:\PyProjects\python_lesson_2\task_17.txt") as f:
    nums_from_file = f.read().split('\n')
for n in nums_from_file:
    indexes.append(int(n))
print(indexes)


def multiply_of_current_numbers(factor, multiplicand):
    for elem in factor:
        nums_for_multiply.append(multiplicand[elem])

    return math.prod(nums_for_multiply)


print(multiply_of_current_numbers(indexes, list_for_multiply))
