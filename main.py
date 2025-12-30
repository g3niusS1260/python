# Пароль-менеджер


password_storage = {}

def check_password_strength(password):
    """
    Проверяет надёжность пароля
    
    1. Длина не менее 8 символов
    2. Содержит хотя бы одну цифру
    3. Содержит хотя бы одну заглавную букву
    4. Содержит хотя бы один специальный символ (!@#$%^&*)
    
    Возвращает оценку: "слабый", "средний", "сильный"
    """
    
    score = 0
    
    # 1. Длина не менее 8 символов
    if len(password) >= 8 :
        print('✅ Длина пароля соответствует требованиям')
    else :
        print('❌ Пароль слишком короткий')
    
    
    # 2. Содержит хотя бы одну цифру
    if any(char.isdigit() for char in password):
        score += 1
        print('✅ Есть цифры')
    else:
        print('❌ Добавьте цифры')
    
    # 3. Содержит хотя бы одну заглавную букву
    if any(char.isupper() for char in password):
        score += 1
        print('✅ Есть заглавные буквы')
    else:
        print('❌ Добавьте заглавные буквы') 
        
    # 4. Содержит хотя бы один специальный символ
    special_chars = '!@#$%^&*'
    
    if any(char in special_chars for char in password):
        score += 1
        print('✅ Есть специальные символы')
    else:
        print('❌ Добавьте специальные символы')   
        
    
    # Определяем итоговую оценку 
    if score == 4:
        return 'сильный'
    elif score >= 2:
        return 'средний'
    else:
        return 'слабый'

def add_password(site, password): # Что делает слово global?
    """
    Добавляем пароль дял сайта
    
    Возвращает:
        True - если добавление успешно
        False - если такой сайт уже существует или пароль слабый
    """
    global password_storage # ОБъявляем, что будем арботать с глобальной переменной
    
    
    # Проверка 1: Сайт уже существует?
    if site in password_storage:
        print(f'Ошибка: сайт "{site} уже существует!"')
        print('Хотите перезаписать пароль? (да/нет)')
        choise = input().lower()
        if choise != 'да':
            return False
    
    # Проверка 2
    strenght = check_password_strength(password)
    
    # Проверка 3
    if strenght == 'Слабый':
        print(f'⚠ Внимание! Пароль для "{site}" оценивается как СЛАБЫЙ.')
        print('Вы уверены, что хотите использовать его? (да/нет)')
        choice = input().lower()
        if choice != 'да':
            print('Добавление отменено')
            return False
        
    # Сохраняем пароль
    password_storage[site] = {
        'password' : password,
        'strenght' : strenght
    }
    
    print(f'✅ Пароль для "{site}" успешно добавлен.')
    print(f'    Надёжность: {strenght}')
    return True

def show_all_passwords():
    """
    Показывает пароль для каждого сайта
    """
    global password_storage
    
    if not password_storage:
        print('Хранилище паролей пустое')
    else:
        for site, password_info in password_storage.items():
            print(f'Сайт: {site} ')
            print(f'   Пароль: {password_info['password']}')
            print(f'   Надежность: {password_info['strenght']}')

def find_password(site):
    """
    Ищет пароль по названию сайта
    Не выводит результат в консоль, функция возвращает значение(Пароль/None)
    """
    global password_storage
    
    if site not in password_storage:
        return None
    return password_storage[site]['password']