# 38
print('38. Напишите программу, удаляющую из текста все слова содержащие "абв".')
text = 'аб дыабв абыгн зыабв абв'
frag = 'абв'
print("Original text: {:>32s}\n".format(text) + "Fragment to delete: {:>6s}".format(frag))
output_string = ''
for i in list(text.split()):
    if frag not in i:
        output_string += f'{i} '
print("The edited text: {:>14s}".format(output_string.rstrip()))

# 39
print('\n39. Создайте программу для игры с конфетами человек против человека.'
      '\n   Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.'
      '\n   Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.'
      '\n   Все конфеты оппонента достаются сделавшему последний ход.'
      '\n   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?'
      '\n   a) Добавьте игру против бота'
      '\n   b) Подумайте как наделить бота "интеллектом"')

print('player VS player')
candies_on_the_table = 200
move_counter = 0


def player(sweets):
    seized_sweets = int(input("How many candies do you want to take? "))
    while seized_sweets <= 0 or seized_sweets > 28:
        seized_sweets = int(input('You can take from 1 to 28 sweets, please try again: '))
        if sweets < seized_sweets:
            print(f'There are {sweets} candies left, you cannot take more than {sweets} candies')
    if sweets < seized_sweets:
        while seized_sweets <= 0 or seized_sweets > sweets:
            seized_sweets = int(input(f'There are {sweets} candies left, you cannot take more than {sweets} candies'))
    sweets -= seized_sweets
    return sweets


while candies_on_the_table > 0:
    if candies_on_the_table > 0:
        print('Player 1 turn')
        candies_on_the_table = player(candies_on_the_table)
        move_counter += 1
    if candies_on_the_table > 0:
        print('Player 2 turn')
        candies_on_the_table = player(candies_on_the_table)
        move_counter += 1
if move_counter % 2 == 0:
    print('Player 2 won')
else:
    print('Player 1 won')

print('\nplayer VS PC')
import random

candies_on_the_table = 200
move_counter = 0


def player(sweets):
    seized_sweets = int(input("How many candies do you want to take? "))
    while seized_sweets <= 0 or seized_sweets > 28:
        seized_sweets = int(input('You can take from 1 to 28 sweets, please try again: '))
        if sweets < seized_sweets:
            print(f'There are {sweets} candies left, you cannot take more than {sweets} candies')
    if sweets < seized_sweets:
        while seized_sweets <= 0 or seized_sweets > sweets:
            seized_sweets = int(input(f'There are {sweets} candies left, you cannot take more than {sweets} candies'))
    sweets -= seized_sweets
    print(f'You take {seized_sweets} candies. Candies left: {sweets}')
    return sweets


def pc(sweets):
    seized_sweets = random.randint(1, 28)
    while seized_sweets > sweets:
        seized_sweets = random.randint(1, 28)
    if sweets <= 28:
        seized_sweets = sweets
    if 28 < sweets < 56:
        seized_sweets = sweets - 29
    sweets -= seized_sweets
    print(f'PC takes {seized_sweets} candies. Candies left: {sweets}')
    return sweets


while candies_on_the_table > 0:
    if candies_on_the_table > 0:
        print('Your turn')
        candies_on_the_table = player(candies_on_the_table)
        move_counter += 1
    if candies_on_the_table > 0:
        print('PC turn')
        candies_on_the_table = pc(candies_on_the_table)
        move_counter += 1
if move_counter % 2 != 0:
    print('You won')
else:
    print('PC won')

# 40
print('\n40. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.')

game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    def user_move():
        move_list = list(map(int, input("Enter list of 3 numbers separated by a space: "
                                        "\nrow №, column № and X (1) or Y (2), f.e. 1 2 1: ").split()))
        move_string = ''
        if move_list[2] == 1:
            move_string += f'[{move_list[0] - 1}][{move_list[1] - 1}] = "x"'
        if move_list[2] == 2:
            move_string += f'[{move_list[0] - 1}][{move_list[1] - 1}] = "o"'
        return move_string
    move = user_move()
    exec("game_matrix" + move)
    for row in game_matrix:
        print(row)

    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] is not None:
            print("Game over!")
            game_is_on = False
            break

# 42
print('42. Реализовать RLE алгоритм: реализовать модуль сжатия и восстановления данных.'
      '\n   Входные и выходные данные хранятся в отдельных текстовых файлах.')


def encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        with open(r'd:\PyProjects\python_lesson_5\task_42_output_data.txt', '+a') as f:
            f.write(f'Encoded data: {encoding}\n')
        return encoding


def decode(data):
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    with open(r'd:\PyProjects\python_lesson_5\task_42_output_data.txt', '+a') as f:
        f.write(f'Decoded data: {decoding}\n')
    return decoding


with open(r'd:\PyProjects\python_lesson_5\task_42_encoding_data.txt', 'r') as f:
    encoding_data = f.read()
print(f'Encoding data: {encoding_data}\n' + "Result: {:>20s}".format(encode(encoding_data)))

with open(r'd:\PyProjects\python_lesson_5\task_42_decoding_data.txt', 'r') as f:
    decoding_data = f.read()
print("Decoding data: {:>2s}\n".format(decoding_data) + "Result: {:>41s}".format(decode(decoding_data)))
