while True:
    try:
        change = int(input('Выберите направление конвертации:\n- Цельсий → Фаренгейт\n- Фаренгейт → Цельсий\nВаш выбор(1/2): '))
    except ValueError:
        print('Ваш ввод должен быть числовым!')
    if change not in [1, 2]:
        print('Введите верный вариант(1/2)!')
        continue
    else:
        while True:
            try:
                temperature = int(input('Введите температуру(число): '))
            except ValueError:
                print('Ваш ввод должен быть числовым!')
            else:
                if change == 1:
                    print(f'{temperature}°C → {(temperature * 1.8) + 32}°F') # Перевод Цельсий в Фаренгейты
                    break
                elif change == 2:
                    print(f'{temperature}°F → {(temperature / 32) / 1.8}') # Перевод Фаренгейтов в Цельсии
                    break 
        break