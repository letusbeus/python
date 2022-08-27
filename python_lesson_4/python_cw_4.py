# 27
print('27. Строка содержит набор чисел. Показать большее и меньшее число.'
      '\n    Символ-разделитель - пробел.')
# С заданной строкой
string_of_numbers = '123 84 75 96 156 24 80 55 19'
print(max(list(map(int, string_of_numbers.split()))))
# С запросом строки у пользователя
print(max(list(map(int, input("Enter the numbers separated by a space: ").split()))))

# 28
print('28. Найти корни квадратного уравнения Ax² + Bx + C = 0'
      '\n    a) Математикой'
      '\n    b) Используя дополнительные библиотеки*')
# a) Математикой
a, b, c = list(map(int, input("Enter the variable values separated by a space: ").split()))
discriminant = D = b ** 2 - 4 * a * c
if D == 0:
    print('The discriminant is 0.\nThe only root of the equation is x = %.2f' % (-b / (2 * a)))
elif D < 0:
    print(f'The discriminant is less than 0.\nThe equation has no material roots.')
else:
    print(f'The discriminant is greater than 0.\nThe equation has 2 roots:')
    print('x_1 = %.2f,' % ((-b + D ** 0.5) / (2 * a)), 'x_2 = %.2f' % ((-b - D ** 0.5) / (2 * a)))
# b) Используя дополнительные библиотеки*
import Mathf

x, y, z = list(map(int, input("Enter the variable values separated by a space: ").split()))
discriminant = D = pow(b, 2) - 4 * a * c
if D == 0:
    print('The discriminant is 0.\nThe only root of the equation is x = %.2f' % (-b / (2 * a)))
elif D < 0:
    print(f'The discriminant is less than 0.\nThe equation has no material roots.')
else:
    print(f'The discriminant is greater than 0.\nThe equation has 2 roots:')
    print('x_1 = %.2f,' % ((-b + Mathf.sqrt(D)) / (2 * a)), 'x_2 = %.2f' % ((-b - Mathf.sqrt(D)) / (2 * a)))

# 29
print('29. Найти НОК двух чисел')
import math
# Математикой
a, b = map(int, input("Enter the variable values separated by a space: ").split())
least_common_multiple = max(a, b)
while True:
    if least_common_multiple % a == 0 and least_common_multiple % b == 0:
        print(f'The least common multiple is {least_common_multiple}')
        break
    else:
        least_common_multiple += 1
# Библиотекой
x, y = map(int, input("Enter the variable values separated by a space: ").split())
print(f'The greatest common divisor is {(x * y) // math.lcm(y, x)}')
print(f'The least common multiple is {(x * y) // math.gcd(y, x)}')
# Функцией


def calculate_lcm(m, n):
    if m > n:
        greater = m
    else:
        greater = n
    while True:
        if (greater % m == 0) and (greater % n == 0):
            lcm = greater
            break
        greater += 1
    return lcm


j, k = map(int, input("Enter the variable values separated by a space: ").split())
print('The least common multiple of %s and %s is %s' % (j, k, calculate_lcm(j, k)))

# 30
print('30. Вычислить число Пи c заданной точностью d.'
      '\n    Пример: при d = 0.001, Пи = 3.141, 10 ** -1 <= d <= 10 ** -10'
      '\n    *** Подумать, что если точность вычисления до 1000 знаков после запятой')
import decimal
print('Кто и шутя и скоро пожелаетъ пи узнать число, ужъ знаетъ')
pi_number = 0
series_of_inverted_squares = 0
user_prec = int(input('Enter the required precision (digits after dot): '))
for i in range(1, 10 ** (user_prec + 1)):
    series_of_inverted_squares += 1 / (i ** 2)
pi_number = decimal.Decimal((series_of_inverted_squares * 6) ** 0.5)
print('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
print(str(pi_number)[:(user_prec + 2)])
print(b - a)
