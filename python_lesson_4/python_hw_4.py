# 31
print('31. Составить список простых множителей натурального числа N')
natural_number = int(input('Enter the natural number: '))
list_of_prime_factors = []
i = 2
while natural_number > 1:
    while natural_number % i == 0:
        list_of_prime_factors.append(i)
        natural_number //= i
    i += 1
print(f'List of prime factors of a natural number:\n{list_of_prime_factors}')

# 32
print('32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.'
      '\n    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]')
# F.E. 1 2 3 5 1 5 3 10
given_list = list(map(int, input('Enter the numbers separated by a space: ').split()))
output_list = []
for i in given_list:
    if i not in output_list:
        output_list.append(i)
    else:
        continue
print(output_list)

# 33
print('33. Задана  k.'
      '\n    Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена'
      '\n    и записать в файл многочлен степени max_degree.'
      '\n    *Пример:k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0')
from random import randint

k = max_degree = int(input('Enter the value of the natural degree for a polynomial: '))
polynomial = ''
if max_degree == 0:
    nonzero_real_number = randint(-100, 100)
    while nonzero_real_number == 0:
        nonzero_real_number = randint(-100, 100)
        print(nonzero_real_number)
    print(nonzero_real_number)
    exit()
elif max_degree > 0:
    while max_degree > 0:
        if max_degree == 1:
            polynomial += f'{randint(0, 100)}*x + '
        else:
            polynomial += f'{randint(0, 100)}*x^{max_degree} + '
        max_degree -= 1
else:
    while max_degree < 0:
        if max_degree == -1:
            polynomial += f'{randint(0, 100)}*x + '
        else:
            polynomial += f'{randint(0, 100)}*x^{max_degree} + '
        max_degree += 1
polynomial += f'{randint(0, 100)} = 0'
with open(r'D:\PyProjects\python_lesson_4\task_33.txt', '+a') as f:
    f.write(polynomial + '\n')
print(polynomial)

# 34
print('34. Даны два файла, в каждом из которых находится запись многочлена.'
      '\n    Задача - сформировать файл, содержащий сумму многочленов.')

with open(r'd:\PyProjects\python_lesson_4\task_34_1.txt', 'r') as f_1:
    x = f_1.read()
with open(r'd:\PyProjects\python_lesson_4\task_34_2.txt', 'r') as f_2:
    y = f_2.read()


def polynomial_to_list(text_polynomial):
    # разбираем строку уравнения по членам, откинув все лишнее, и преобразуем в список чисел
    set_of_terms = list(map(str,
                            text_polynomial.replace(' = 0', '')
                            .replace(' ', '')
                            .replace('-', '+-')
                            .lstrip('+')
                            .split('+')))

    def filtered_list(input_list, index, var_str):
        # расставляем коэффициенты многочлена по убыванию степени
        for j in range(index, len(input_list)):
            if input_list[j].endswith(var_str):
                input_list.insert(index, input_list[j].rstrip(var_str))
                return

    filtered_list(set_of_terms, 0, '*x^3')
    filtered_list(set_of_terms, 1, '*x^2')
    filtered_list(set_of_terms, 2, '*x')

    for elem in range(3, len(set_of_terms)):
        if 'x' not in set_of_terms[elem]:
            set_of_terms.insert(3, set_of_terms[elem])
            break
    set_of_terms = [int(elem) for elem in set_of_terms[:4]]
    return set_of_terms


def sum_of_coefficients(a, b):
    total_list = list(map(sum, zip(a, b)))
    return total_list


def total_polynomial(arg):
    sum_of_polynomial = ''
    if len(arg) > 1:
        counter = 0
        while counter < len(arg) - 1:
            sum_of_polynomial += str(arg[counter]) + '*x^' + str(len(arg) - 1 - counter) + ' + '
            counter += 1
        sum_of_polynomial = ''.join([sum_of_polynomial.rstrip(' +'), ' + ', str(arg[-1]), ' = 0'])
        return sum_of_polynomial.replace('+ -', '- ').replace('^1', '').replace('^0', '')
    else:
        print('Zero polynomial')


loc_a = polynomial_to_list(x)
loc_b = polynomial_to_list(y)
soc = sum_of_coefficients(loc_a, loc_b)
sop = (total_polynomial(soc))
print(soc)
# Вывод для наглядности
print(f'First polynomial:   {x}\nSecond polynomial: {y}\nSum of polynomials is {sop}')
with open(r'D:\PyProjects\python_lesson_4\task_34_total.txt', 'w') as output_f:
    output_f.write(sop + '\n')
