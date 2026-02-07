# Домашняя библиотека

# ГЛАВНОЕ МЕНЮ
def show_main_menu():
    print("\n" + "="*40)
    print("📚 МИНИ-БИБЛИОТЕКА")
    print("="*40)
    print("1. 📖 Показать все книги")
    print("2. ➕ Добавить книгу")
    print("3. 🔍 Найти книгу")
    print("4. 🔄 Выдать/вернуть книгу")
    print("5. 📊 Статистика")
    print("6. ❌ Выход")
    print("="*40)
    choice = input("Выберите действие (1-6): ")
    return choice

# ПОКАЗ ВСЕХ КНИГ
def show_all_books():
    """
    Показывает все книги
    
    Возвращает:
        False - если нет книг в библиотеке или возникла ошибка
    """
    print('\n<<< ВАША БИБЛИОТЕКА >>>\n')
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines() # Получим список книг в виде строк
            
            # Если библиотека пуста - сообщим об этом
            if not books:
                print('\nВаша библиотека пуста!\n')
                return False
            
            i = 0
            while i < len(books):
                info = books[i].split(';') # book[i] это строка из файла книг вида НАЗВАНИЕ;АВТОР;ГОД;ЖАНР;СТАТУС
                title, author, year, genre = info[0], info[1], info[2], info[3] # Распакуем список info
                status = '✅ доступна' if info[4] == 'доступна\n' else '🔄 выдана'
                print(f'{i + 1}. "{title}", {genre} ({year}) - {author} : {status}')
                i += 1
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False

# ДОБАВЛЕНИЕ КНИГИ
def add_book(title, author, year, genre):
    """
    Добавляет книгу в библиотеку
    
    Параметры:
        title(str) - название
        author(str) - автор
        year(int) - год от 1000 до 2026
        genre(str) - жанр
    
    Возвращает:
        str - строка с информацией о книге вида НАЗВАНИЕ;АВТОР;ГОД;ЖАНР;СТАТУС
        False - если в процессе добавления возникли ошибки
    """
    
    # ПРОВЕРКА КОРРЕСТНОСТИ НАЗВАНИЯ
    if not title:
        print('\nНе указано название!\n')
        return False
    
    # ПРОВЕРКА НАЛИЧИЯ КНИГИ
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines()
            
            # Сообщим пользователю, если такая книга уже есть
            for book in books:
                info = book.split(';') # Получим список с информацией о книге
                if title == info[0]: # info[0] - название книги book
                    print('\nВ библиотеке уже есть книга с таким названием!\n')
                    return False
    except FileNotFoundError: # Если файла с библиотекой нет - код ниже просто создаст файл и запишет первую книгу
        pass
    
    # ДОБАВЛЕНИЕ КНИГИ. Проверка данных
    if not author:
        print('\nНе указан автор!\n')
        return False
    if not 1000 <= year <= 2026:
        print('\nНе указан год!\n')
        return False
    if not genre:
        print('\nНе указан жанр!\n')
        return False

    # Если все данные корреткные - добавим книгу или создадим файл и добавим первую книгу
    try:
        with open('books.txt', 'a', encoding='utf-8') as books_file:
            book_to_write = f'{title};{author};{year};{genre};доступна' # При начальной инициализации книга доступна
            books_file.write(f'{book_to_write}\n')
            print('\n✅ Книга успешно добавлена\n')
            return book_to_write
    except Exception as e:
        print(f'\nВозникла неизвестная ошибка : {e}\n')
        return False

# ПОИСК КНИГИ
def search_book(key, value):
    """
    Ищет книгу(книги) по автору/названию/жанру
    
    Параметры:
        key(str) - ключ, по которому юудет идти поиск ('название', 'автор', 'жанр'). Передается в коде(не пользователем)
        value(str) - значение этого ключа ('Капитанская дочка', 'Александр Пушкин', 'Роман')
        
    Возвращает:
        str - книга в виде строки из файла
        list - если найдено несколько книг (по автору, по жанру)
        False - если книга не найдена или в процессе поиска возникли ошибки
    """
    
    # Проверим корректность value
    if not value:
        print('\nВы не передали значение для поиска!\n')
        return False
    
    # ПОИСК КНИГИ
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines()
            
            # Если библиотека пуста - сообщим польщователю
            if not books:
                print('\nВ вашей библиотеке нет книг!\n')
                return False
            
            print('\n<<< РЕЗУЛЬТАТЫ ПОИСКА >>>\n')
            
            # ПОИСК ПО НАЗВАНИЮ
            if key == 'название': 
                for book in books:
                    info = book.split(';') # Получим список с информацией о книге
                    title, author, year, genre = info[0], info[1], info[2], info[3] # Распакуем список info
                    status = '✅ доступна' if info[4] == 'доступна\n' else '🔄 выдана'
                    if value == title:
                        print(f'{title}, {genre} ({year}) - {author} : {status}')
                        return book
                print('\nВ вашей библиотеке нет книги с таким названием!\n')
                return False
            
            # ПОИСК ПО АВТОРУ
            elif key == 'автор':
                i = 0
                found_books = [] # Список найденных по данному автору книг
                while i < len(books):
                    info = books[i].split(';')
                    if value == info[1]:
                        found_books.append(books[i])
                    i += 1
                
                # Если нет таких книг - сообщим
                if not found_books:
                    print('\nВ вашей библиотеке нет такого автора!\n')
                    return False
                
                # Если такие книги есть - выведем их
                i = 0
                while i < len(found_books):
                    info = found_books[i].split(';')
                    title, author, year, genre = info[0], info[1], info[2], info[3] # Распакуем список info
                    status = '✅ доступна' if info[4] == 'доступна\n' else '🔄 выдана'
                    print(f'{i + 1}. {title}, {genre} ({year}) - {author} : {status}')
                    i += 1
                return found_books
            
            # ПОИСК ПО ЖАНРУ
            elif key == 'жанр':
                i = 0
                found_books = [] # Список найденных по данному жанру книг
                while i < len(books):
                    info = books[i].split(';')
                    if value == info[3]:
                        found_books.append(books[i])
                    i += 1
                
                # Если нет таких книг - сообщим
                if not found_books:
                    print('\nВ вашей библиотеке нет такого жанра!\n')
                    return False
                
                # Если такие книги есть - выведем их
                i = 0
                while i < len(found_books):
                    info = found_books[i].split(';')
                    title, author, year, genre = info[0], info[1], info[2], info[3] # Распакуем список info
                    status = '✅ доступна' if info[4] == 'доступна' else '🔄 выдана'
                    print(f'{i + 1}. {title}, {genre} ({year}) - {author} : {status}')
                    i += 1
                return found_books
                
                
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False


# ВЫДАЧА КНИГИ
def issue_book(title):
    """
    Выдает книгу(меняет ее статус в файле)
    
    Параметры:
        title(str) - название книги
        
    Возвращает:
        True - если книга выдана
        False - если возникли ошибки
    """
    
    if not title:
        print('\nВы не передали название!\n')
    
    # ПРОВЕРКА НАЛИЧИЯ КНИГИ
    is_in_library = False
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines()
            
            # Если библиотека пуста - сообщим об этом
            if not books:
                print('\nВ вашей библиотеке еще нет книг!\n')
            for book in books:
                info = book.split(';')
                if title == info[0]:
                    is_in_library = True
            if not is_in_library:
                print('\nВ вашей библиотеке нет книг с таким названием!\n')
                return False
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False
    
    # ПРОВЕРКА СТАТУСА КНИГИ
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            for book in books:
                info = book.split(';')
                if title == info[0]:
                    if info[4] == 'выдана\n':
                        print('\nКнига уже выдана!\n')
                        return False
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False
    
    # ВЫДАЧА КНИГИ
    try:
        with open('books.txt', 'w', encoding='utf-8') as books_file:
            # Сменим статус книге и перезапишем файл с обновленной книгой
            i = 0
            while i < len(books):
                info = books[i].split(';')
                if title == info[0]:
                    info[4] = 'выдана\n'
                    books[i] = ';'.join(info)
                i += 1
            books_file.writelines(books)
            print('\n✅ Книга успешно выдана!\n')
            return True
    except Exception as e:
        print(f'\nВозникла неизвестная ошибка : {e}\n')
        return False
    

# ВОЗВРАТ КНИГИ
def return_book(title):
    """
    Возвращает книгу(меняет ее статус в файле)
    
    Параметры:
        title(str) - название книги
        
    Возвращает:
        True - если книга возвращена
        False - если возникли ошибки
    """
    
    if not title:
        print('\nВы не передали название!\n')
    
    # ПРОВЕРКА НАЛИЧИЯ КНИГИ
    is_in_library = False
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines()
            
            # Если библиотека пуста - сообщим об этом
            if not books:
                print('\nВ вашей библиотеке еще нет книг!\n')
            for book in books:
                info = book.split(';')
                if title == info[0]:
                    is_in_library = True
            if not is_in_library:
                print('\nВ вашей библиотеке нет книг с таким названием!\n')
                return False
    except FileNotFoundError:
        print('\nВ вашей библиотеке еще нет книг!\n')
        return False
    
    # ПРОВЕРКА СТАТУСА КНИГИ
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            for book in books:
                info = book.split(';')
                if title == info[0]:
                    if info[4] == 'доступна\n':
                        print('\nКнига уже доступна!\n')
                        return False
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False
    
    # ВОЗВРАТ КНИГИ
    try:
        with open('books.txt', 'w', encoding='utf-8') as books_file:
            # Сменим статус книге и перезапишем файл с обновленной книгой
            i = 0
            while i < len(books):
                info = books[i].split(';')
                if title == info[0]:
                    info[4] = 'доступна\n'
                    books[i] = ';'.join(info)
                i += 1
            books_file.writelines(books)
            print('\n✅ Книга успешно возращена!\n')
            return True
    except Exception as e:
        print(f'\nВозникла неизвестная ошибка : {e}\n')
        return False
    

# СТАТИСТИКА БИБЛИОТЕКИ
def get_stats():
    """
    Выводит статистику библиотеки
    
    Возвращвает:
        False - если возникли ошибки
        dict - словарь со статистикой, если все прошло успешно
    """
    
    try:
        with open('books.txt', 'r', encoding='utf-8') as books_file:
            books = books_file.readlines()
            
            # Если библиотека пуста - сообщим
            if not books:
                print('\nВ вашей библиотеке еще нет книг!\n')
                return False

            print('\n<<< СТАТИСТИКА БИБЛИОТЕКИ >>>\n')
            stats = { # Общая статистика
                'quantity_books': len(books),
                'availables': 0,
                'issued': 0,
            }
            years = [] # Годы
            
            for book in books: 
                info = book.split(';')
                if info[4] == 'доступна\n':
                    stats['availables'] += 1
                else:
                    stats['issued'] += 1
                    
            for book in books: 
                info = book.split(';')
                if int(info[2]) not in years:
                    years.append(int(info[2]))
            
            print('📈 Общая статистика:')
            print(f'Всего книг: {stats['quantity_books']} ')
            print(f'Доступно сейчас: {stats['availables']} ({(stats['availables'] / stats['quantity_books'] * 100):.0f}%)')
            print(f'Выдано: {stats['issued']} ({(stats['issued'] / stats['quantity_books'] * 100):.0f}%)')
            genres = {} # Жанры и их количества
            for book in books:
                info = book.split(';')
                if info[3] not in genres.keys():
                    genres[info[3]] = 1
                else:
                    genres[info[3]] += 1
            sorted_genres_list = sorted(genres.items(), key=lambda x: x[1], reverse=True) # Получаем сортированный словарь жанров в виде списка
            if len(sorted_genres_list) > 3:
                sorted_genres = dict(sorted_genres_list[:3]) # Помещаем обратно в список, но теперь только 3 топовых значения
            else:
                sorted_genres = dict(sorted_genres_list)
            print('\n🏆 Топ-3 жанра:')
            i = 0
            for genre, value in sorted_genres.items():
                print(f'{i+1}. {genre}: {value} книг')
                i += 1
            print(f'\n📅 Самый старый год издания: {min(years)}')
            return stats
    except FileNotFoundError:
        print('\nВаша библиотека еще не создана!\n')
        return False
    
# ОСНОВНОЙ ЦИКЛ
while True:
    menu_choice = show_main_menu()
    
    if menu_choice == '1':
        show_all_books()
    elif menu_choice == '2':
        title = input('Введите название: ')
        author = input('Введите автора: ')
        try:    
            year = int(input('Введите год (1000-2026): '))
        except ValueError:
            print('\nГод должен быть числом!\n')
            continue
        genre = input('Введите жанр: ')
        
        add_book(title, author, year, genre)
    elif menu_choice == '3':
        print('Искать по')
        print('1. Названию')
        print('2. Автору')
        print('3. Жанру')
        print('4. Вернуться\n')
        search_choice = input('Выбор: ')
        
        if search_choice == '1':
            title = input('\nВведите название: ')
            search_book('название', title)
        elif search_choice == '2':
            author = input('\nВведите автора: ')
            search_book('автор', author)
        elif search_choice == '3':
            genre = input('\nВведите жанр: ')
            search_book('жанр', genre)
        elif search_choice == '4':
            continue
        else:
            print('\nНеверно выбран вариант!\n')
            continue
    elif menu_choice == '4':
        print('\nДествие:')
        print('1. Выдать книгу')
        print('2. Вернуть книгу')
        borrow_return_choice = input('\nВыбор: ')
        if borrow_return_choice == '1':
            title = input('Введите название: ')
            issue_book(title)
        elif borrow_return_choice == '2':
            title = input('Введите название: ')
            return_book(title)
    elif menu_choice == '5':
        get_stats()
    elif menu_choice == '6':
        break
    else:
        print('\nНекорректный ввод\n')