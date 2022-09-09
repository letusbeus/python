# # 1
# print('1. По двум заданным числам проверить является ли одно квадратом второго')
# num_1 = int(input('First number: '))
# num_2 = int(input('Second number: '))
# if pow(num_2, 2) == num_1:
#     print(f'The first number = {num_1} is the square of the second = {num_2}')
# elif pow(num_1, 2) == num_2:
#     print(f'The second number = {num_2} is the square of the first = {num_1}')
# else:
#     print('Neither number is the square of the other')
# # 2
# print('\n2. Найти максимальное из пяти чисел')
# entered_list = input("Enter a list of numbers separated by a space: ").split()
# print("You entered the following numbers", end=': ')
# print(*entered_list, sep=', ')
# print('Max number is', max(list(map(int, entered_list))))
#
# # 3
# print('\n3. Вывести на экран числа от -N до N')
# range_num = input("Enter the number: ")
# if range_num.isdigit():
#     print(f'Range from -{range_num} to {range_num}:')
#     for i in range(-abs(int(range_num)), int(range_num) + 1):
#         print(i)
# else:
#     print("The entered value is not a number")
#
# # 4
# print('\n4. Показать первую цифру дробной части числа')
# num = input("Enter a fractional number separated by a comma: ").split(',')
# print('The first digit of the fractional part of the number is', num[1][0])
#
# # 5
# print('\n5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30')
# five_num = input("Enter the number: ")
# if five_num.isdigit():
#     five_num = int(five_num)
#     if five_num % 10 == 0 and five_num % 30 != 0:  # нет смысла проверять кратность 5, если число кратно 10
#         print('Multiple of 5 and 10 nor 30')
#     elif five_num % 15 == 0 and five_num % 30 != 0:
#         print('Multiple of 15 nor 30')
#     else:
#         print("Does not meet the conditions")
# else:
#     print("The entered value is not a number")
#
# # 6
# print('\n6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.')
# day_num = input("Enter the number of a day: ")
# week = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday',
#         7: 'sunday'}
# if day_num.isdigit():
#     day_num = int(day_num)
#     if day_num in week:
#         if day_num in (6, 7):
#             print(week[day_num].title() + ' - holiday')
#         else:
#             print(week[day_num].title() + ' - working day')
#     else:
#         print('There are only 7 days in a week')
# else:
#     print("The entered value is not a number")

# 7
print('\n7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')
x = [True, False]
y = [True, False]
z = [True, False]
count = 0
for a in x:
    for b in y:
        for c in z:
            count += 1
            print(f"{count} {not (x or y or z) == (not x and not y and not z)}")
# С этим пока вообще непонятно. Надо покурить мануалы.