# 14.
print('Подсчитать сумму цифр в вещественном числе.')
number = input("Enter the number: ")
result = 0
for i in number:
    if i.isdigit():
        result += int(i)
    else:
        continue
print(f'The sum of digits in the given number = {result}')

# 15.
print('15. Написать программу получающую набор произведений чисел от 1 до N.'
      '\n    Пример: пусть N = 4, тогда [ 1, 2, 6, 24]')
n = input('Enter the number: ')
arr = [1]
if n.isdigit():
    for i in range(1, int(n)):
        arr.append(arr[i - 1] * (i + 1))
else:
    print('Please check if the entered value is a number')
print(f'List of multiplies: {arr}')

# 18
print('18. Реализовать алгоритм перемешивания списка.')
# Дял псевдорандома взяла perf_counter
import random
from time import perf_counter

given_list = list(map(int, input("Enter list of numbers separated by a space: ").split()))
# F.e. 63 5 34 64 12 5 93 127 432 73 664
num_of_shift = int(str(perf_counter()).split('.', 1)[-1][:3])
while num_of_shift > 0:
    # Осталось прикрутить perf_counter к выбору элемента, логика та же
    a = random.randint(0, len(given_list) - 1)
    given_list.append(given_list[a])
    given_list.pop(a)
    num_of_shift -= 1
print(given_list)
