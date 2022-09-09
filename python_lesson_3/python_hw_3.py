# 22
print('Найти сумму чисел списка стоящих на нечетной позиции')
# F.E. 45 23 6 11 9 31
input_list = list(map(int, input("Enter the list of numbers separated by a space: ").split()))
sum_of_even = 0
for i in range(len(input_list)):
    if i % 2 != 0:
        sum_of_even += input_list[i]
print(sum_of_even)

# 23
print('23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и'
      '\n    предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]')
list_of_nums = list(map(int, input("Enter the list of numbers separated by a space: ").split()))
list_of_pairs_multiply = []
for i in range(int(len(list_of_nums) / 2 + len(list_of_nums) % 2)):
    list_of_pairs_multiply.append(list_of_nums[i] * list_of_nums[-(i + 1)])
print(list_of_pairs_multiply)

# 24
print('24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным'
      '\n    значением дробной части элементов.'
      '\n    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19')

# F.E. 1.1 1.2 3.1 5 10.01 or 2.7 14.2 5.5 5.9 1.95
list_of_material_numbers = list(map(float, input("Enter the list of material numbers separated by a space: ").split()))
list_of_fractional_parts = []
for num in list_of_material_numbers:
    if num % 1 != 0:
        list_of_fractional_parts.append(float('0.%s' % str(num).split('.')[1]))
result = max(list_of_fractional_parts) - min(list_of_fractional_parts)
print(result)

# 25
print('25. Написать программу преобразования десятичного числа в двоичное.'
      '\n    Пример:'
      '\n    - 45 -> 101101'
      '\n    - 3 -> 11'
      '\n    - 2 -> 10')
given_number = int(input('Enter the number: '))


def adduction_to_binary(decimal_number):
    binary_number = ''
    while decimal_number != 0:
        binary_number = binary_number + str(int(decimal_number % 2))
        decimal_number = int(decimal_number / 2)
    return binary_number


print(adduction_to_binary(given_number))

# 26
print('26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.'
      '\n    Т. е. для k = 8 список будет выглядеть так:'
      '\n[-21 ,13, -8, 5, −3,  2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]')
len_of_negafibonacchi = int(input('Enter the number: '))


def negafibonacchi(user_num):
    negafibonacchi_list = []
    first_num = 0
    second_num = 1
    counter = 0
    while counter < user_num:
        if counter == 0:
            negafibonacchi_list.append(0)
        if counter == 1:
            negafibonacchi_list.insert(0, -1)
            negafibonacchi_list.append(1)
        else:
            subtotal = first_num + second_num
            first_num = second_num
            second_num = subtotal
            negafibonacchi_list.append(subtotal)
            if negafibonacchi_list[0] > 0:
                negafibonacchi_list.insert(0, -subtotal)
            else:
                negafibonacchi_list.insert(0, subtotal)
        counter += 1
    return negafibonacchi_list


print(negafibonacchi(len_of_negafibonacchi))
