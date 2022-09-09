# 8
print('8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У')
point = input("Enter 2 point separated by a space: ").split()
x = (list(map(int, point)))[0]
y = (list(map(int, point)))[1]
if x == 0 and y != 0:
    print('The point lies on the x-axis')
elif y == 0 and x != 0:
    print('The point lies on the y-axis')
elif x > 0:
    if y > 0:
        print('1st quarter coordinate plane')
    else:
        print('4th quarter coordinate plane')
elif x < 0:
    if y > 0:
        print('2nd quarter coordinate plane')
    else:
        print('3rd quarter coordinate plane')
else:
    print('The point is null')

# 9
print('\n9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат '
      'для точек этой четверти')
plane = input("Enter the number of the plane: ")
if plane.isdigit() and int(plane) in (1, 2, 3, 4):
    plane = int(plane)
    if plane == 1:
        print('0 < x < +∞, 0 < y < +∞')
    if plane == 2:
        print('-∞ < x < 0, 0 < y < +∞')
    if plane == 3:
        print('-∞ < x < 0, -∞ < y < 0')
    if plane == 4:
        print('0 < x < +∞, -∞ < y < 0')
else:
    print("Please check if the entered value is a number and meets the conditions")

# 10
print('\n10. Найти расстояние между двумя точками пространства')
import math

point_1 = input("Enter 3 coordinates of X separated by a space: ").split()
point_2 = input("Enter 3 coordinates of Y separated by a space: ").split()
x = (list(map(int, point_1)))
y = (list(map(int, point_2)))
print('Distance between X and Y is %.2f' % math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2))
