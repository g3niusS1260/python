# ДНЕВНИК НАСТРОЕНИЯ
import datetime

print('=== ДНЕВНИК НАСТРОЕНИЯ ===\n')
moods = [] # Оценки настроения

while True: # Основной цикл 
    # 1. Запросим дату
    date = input('Введите дату (день-месяц-год) или нажмите Enter (сегодняшняя дата): ')
    
    if not date: # Если был нажат Enter
        date = datetime.date.today().strftime('%d-%m-%Y')
        
    try: # Проверим коррекстность даты
        datetime.datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        print('Дата указана неверно\n')
        continue
    
    # 2. Запросим настроение
    try:
        mood = int(input('Настроение (1-5): '))
    except ValueError:
        print('Неверный ввод\n')
        continue
    
    if not mood: # Если пользователь нажал enter
        print('Неверный ввод\n')
        continue
        
    if not 1 <= mood <= 5: # Если оценка не соответствует диапозону настроения
        print('Неверный ввод\n')
        continue
    
    # 3. Запросим описание дня
    description = input('Кратко опишите день: ')
    
    # 4. Сделаем строку для записи в файл
    to_file = f'[{date}] Настроение: {mood}/5\n{description}\n\n'
    
    # 5. Сделаем запись в файл
    with open('mood_diary.txt', 'a', encoding='utf-8') as f:
        f.write(to_file)
    print('\nЗапись сохранена!\n')

    # 6. Спросим у пользователя, хочет ли он сделать еще запись
    change = input('Хотите сделать еще запись? (да/нет): ')
    if change.lower() != 'да':
        # Получим оценки настроения
        with open('mood_diary.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                for word in line.split():
                    if '/' in word: # Если это слово вида x/5, т.е настроение
                        moods.append(int(word[0]))
        print('\nСтатистика за неделю:')
        print(f'Среднее настроение: {(sum(moods) / len(moods)):.1f}')
        
        # Найдем самый счастливый день
        with open('mood_diary.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            happiset_mood = max(moods)
            happiest_day = ''
            for line in lines:
                if f'{happiset_mood}/5' in line:
                    happiest_day = line
                    break
        
        print(f'Самый счастливый день: {happiest_day}')
        break
    print()