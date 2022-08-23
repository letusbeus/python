# 19.
print('19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел')
from time import perf_counter
len_of_num = input('Enter the len of number: ')
if len_of_num.isdigit():
    current_time = int(str(perf_counter()).split('.', 1)[-1])
    print(str(current_time ** (int(len_of_num) // 6 + 1))[:int(len_of_num)])
else:
    print('Please check if the entered value is a number')

# 20
print('20. Определить, присутствует ли в заданном списке строк, некоторое число')
num = input('Enter the number: ')
str1 = ["sohbg143h", "pos2435", "vnyt861t", "pjhsadj21", "1943gs"]
if num.isdigit():
    for strings in str1:
        exist = str(num) in strings
        print(exist)
else:
    print('Please check if the entered value is a number')

# 21
print('21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.'
      '\n    Примеры:'
      '\n    список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3'
      '\n    список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5'
      '\n    список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1'
      '\n    список: ["123", "234", 123, "567"], ищем: "123", ответ: -1'
      '\n    список: [], ищем: "123", ответ: -1')

list_of_strings = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
wanted_substring = "йцу"
ingoing = 0
for i in range(len(list_of_strings)):
    if list_of_strings[i] == wanted_substring:
        ingoing += 1
        if ingoing == 2:
            print(f'Second occurrence index is {i}')
            break
if ingoing < 2:
    print('-1: no second occurrence')
