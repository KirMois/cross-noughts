


sq1 = "1"
sq2 = "2"
sq3 = "3"
sq4 = "4"
sq5 = "5"
sq6 = "6"
sq7 = "7"
sq8 = "8"
sq9 = "9"


cross = []
nought = []

win_solution = [['1x','2x','3x'], ['4x', '5x', '6x'], ['7x', '8x', '9x'],
                ['1x', '4x', '7x'],['1x','4x','6x','7x'], ['2x', '5x', '8x'], ['3x', '6x', '9x'],
                ['1x', '5x', '9x'], ['3x', '5x', '7x']]

lost_solution = [['1o', '2o', '3o'], ['4o','5o', '6o'], ['7o', '8o', '9o'],
                 ['1o', '4o', '7o'], ['2o', '5o', '8o'], ['3o', '6o', '9o'],
                 ['1o', '5o', '9o'], ['3o', '5o', '7o']]




while True:
    cross.sort()
    nought.sort()
    print(' _____________') #squares
    print(f'| {sq1:}  | {sq2:}  | {sq3:} |  ')
    print(f'|-------------|')
    print(f'| {sq4:}  | {sq5:}  | {sq6:} |  ')
    print(f'|-------------|')
    print(f'| {sq7:}  | {sq8:}  | {sq9:} |  ')
    print(f' ------------- ')

    act = input('Введите номер клетки для Х: ')# users_X_moves

    if act == '1':
        sq1 = "X"
        cross.append('1x')
        cross.sort()
    if act == '2':
        sq2 = "X"
        cross.append('2x')
        cross.sort()
    if act == '3':
        sq3 = "X"
        cross.append('3x')
        cross.sort()
    if act == '4':
        sq4 = "X"
        cross.append('4x')
        cross.sort()
    if act == '5':
        sq5 = "X"
        cross.append('5x')
        cross.sort()
    if act == '6':
        sq6 = "X"
        cross.append('6x')
        cross.sort()
    if act == '7':
        sq7 = "X"
        cross.append('7x')
        cross.sort()
    if act == '8':
        sq8 = "X"
        cross.append('8x')
        cross.sort()
    if act == '9':
        sq9 = "X"
        cross.append('9x')
        cross.sort()
    else:
        print("введите номер от 1 до 9")






    cross.sort()
    nought.sort()
    print(' _____________')  # squares
    print(f'| {sq1}  | {sq2}  | {sq3} |  ')
    print(f'|-------------|')
    print(f'| {sq4}  | {sq5}  | {sq6} |  ')
    print(f'|-------------|')
    print(f'| {sq7}  | {sq8}  | {sq9} |  ')
    print(f' ------------- ')

    act2 = input('Введите номер клетки для O: ')


    if act2 == '1':
        sq1 = "O"
        nought.append('1o')
        nought.sort()
    if act2 == '2':
        sq2 = "O"
        nought.append('2o')
        nought.sort()
    if act2 == '3':
        sq3 = "O"
        nought.append('3o')
        nought.sort()
    if act2 == '4':
        sq4 = "O"
        nought.append('4o')
        nought.sort()
    if act2 == '5':
        sq5 = "O"
        nought.append('5o')
        nought.sort()
    if act2 == '6':
        sq6 = "O"
        nought.append('6o')
        nought.sort()
    if act2 == '7':
        sq7 = "O"
        nought.append('7o')
        nought.sort()
    if act2 == '8':
        sq8 = "O"
        nought.append('8o')
        nought.sort()
    if act2 == '9':
        sq9 = "O"
        nought.append('9o')
        nought.sort()
    else:
        print("введите номер от 1 до 9")





    if cross in win_solution:
        print('Кресты победили!')
        print('с ходами :', cross)
        break
    elif nought in lost_solution:
        print('Нули на высоте')
        print('ходы ноликов:', nought)
        break



    print(cross)
    print(nought)










"""if cross in win_solution:
        print('Кресты победили!')
        print('с ходами :', cross)
        break
    elif nought in lost_solution:
        print('Нули на высоте')
        print('ходы ноликов:',nought)
        break"""

""" print(cross)
    print(nought)"""



