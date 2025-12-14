print()
is_continue = True # Флаг, показывающий, продолжится ли программа

while(is_continue): # Цикл работает, пока наш флаг True
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введитое второе число: '))
    except ValueError: # Если пользователь ввел не число - обрабатываем ValueError
        print('Введите число!')
        continue # Если ввод не число, то цикл начинается заново
    
    while True: 
        operation = input('Введите операцию(+, -, *, /): ')
        
        # Находим нужную операцию. Если ввод пользователя правильный - бесконечный цикл прерывается и программа работает дальше
        if operation == '+':
            print(f'{a} + {b} = {a + b}')
            break
        elif operation == '-':
            print(f'{a} - {b} = {a - b}')
            break
        elif operation == '*':
            print(f'{a} * {b} = {a * b}')
            break
        elif operation == '/': 
            print(f'{a} / {b} = {a / b}')
            break
        else:
            print('Введите корректную операцию(+, -, *, /)!')

    while True:
        
        """
        Обрабатываем ввод пользователя. Если введено 1 - бесконечный цикл прерывается и программа завершается.
        Если введено 2 - бесконечный цикл прерывается и программа продолжает работать
        """
        try:
            change = int(input('Завершить программу?\n1 - ДА\n2 - НЕТ\n>>> '))
        except ValueError:
            print('Введите правильный выбор(1/2)!')
            continue
        if change == 1:
            is_continue = False
            break
        elif change == 2:
            is_continue = True
            break
        else:
            print('Введите правильный выбор(1/2)!')
    