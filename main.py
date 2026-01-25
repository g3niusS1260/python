from collections import Counter

# ШАГ 1. Класс Movie
class Movie:
    """
    Объект фильма
    
    Атрибуты:
    title - название фильма (строка)
    director - режиссер (строка)
    year - год выпуска (целое число, от 1888 до 2024)
    genre - жанр (строка: "комедия", "драма", "боевик", "фантастика", "ужасы")
    rating - рейтинг фильма от пользователя (число от 1 до 10, по умолчанию None)
    """

    def __init__(self, title, director, year, genre):
        """
        Конструктор класс Movie. Проверяет корректность данных и инициализирует фильм. 
        При некорректности данных останавливает программу
        """
        
        is_correct_data = True # Корректны ли данные
        
        # Проверка корретности названия
        if not title:
            print('У фильма должно быть указано название!')
            is_correct_data = False
        
        # Проверка корретности режиссера
        if not director:
            print('У фильма должен быть указан режиссер!')
            is_correct_data = False
        
        # Проверка корретности года выпукса
        if not 1888 <= year <= 2024:
            print('У фильма должен быть правильно указан год выпуска (1888-2024)')
            is_correct_data = False

        # Проверка корректности жанра
        valid_genres = ['комедия', 'драма', 'боевик', 'фантастика', 'ужасы'] # Допустимые жанры
        if genre.lower() not in valid_genres:
            print('У фильма должен быть допустимый жанр!')
            is_correct_data = False
        
        if not is_correct_data:
            raise ValueError('Некорректные данные')
        
        self.__title = title
        self.__director = director
        self.__year = year
        self.__genre = genre
        self._rating = None
        
    def set_rating(self, rating):
        """
        Устанавливает рейтинг для фильма с проверкой (1-10)
        
        Аргументы:
            rating - рейтинг фильма 1-10 (число)
            
        Возвращает: 
            rating - если мы установили рейтинг без ошибок
            False - если рейтинг был передан некорректно
        """
        
        if 1 <= rating <= 10: 
            self._rating = rating
            return rating
        return False
    
    def is_high_rated(self):
        """
        Проверка на высокий рейтинг
        
        Возвращает:
            True - если рейтинг >= 8
            False - если рейтинг <= 8 или он отсутствует
        """
        
        if not self._rating:
            print(f'Фильм "{self.__title}" еще не оценён!')
            return False
        
        return True if self._rating >= 8 else False
    
    
    def info_in_tuple(self):
        """
        Возвращает информацию о фильме в виде кортежа (название фильма, информация о фильме в виде словаря)
        Нужен для записи фильма в домашнюю коллекцию
        
        Возвращает: 
            dict()
        """
        data = (
            self.__title,
            {
                'Режиссёр': self.__director,
                'Год выпуска': self.__year,
                'Жанр' : self.__genre,
                'Рейтинг': self._rating
            }
        )
        
        return data
    
    def __str__(self):
        """
        Строковое представление о фильме
        Возвращает: str (описание фильма)
        """
        
        return f'{self.__title} ({self.__year}) - {self.__director} [{self.__genre}] ★ {self._rating if self._rating else 'рейтинг не определён'}'


# ШАГ 2. Класс MovieCollection
class MovieCollection:
    """
    Библиотека фильмов. Проверяет корректность имени и создает movies
    Атрибуты:
        name - название коллекции (строка)
        movies - список объектов Movie (список)
    """
    
    quantity_movies = 0
    
    def __init__(self, name):
        """Конструктор класса MovieCollection"""
        
        # Проверка на корректность названия
        if not name:
            raise ValueError('У коллекции должно быть название!')
        
        self._name = name
        self.__movies = []
        
    def add_movie(self, movie):
        """
        Добавление фильма в домашнюю коллекцию.
        
        Параметры:
            movie - фильм (Movie)
        
        Возвращает:
            Movie() - если добавление прошло успешно
            False - если возникла ошибка
        """
        
        if movie in self.__movies:
            print(f'Фильм "{movie.info_in_tuple()[0]}" уже есть в библиотеке!')
            return False

        self.__movies.append(movie)
        self.quantity_movies += 1
        return movie
    
    def remove_movie(self, title):
        """
        Удаляет фильм по названию.
        
        Параметры:
            title - название фильма (строка)
        
        Возвращает:
            Movie() - если удаление прошло успешно
            False - если возникла ошибка
        """
        
        if not self.__movies:
            print(f'В коллекции "{self._name}" еще нет фильмов!')
            return False
        # Проверим, есть ли такой фильм в коллекции и удалим его
        movie = self.get_movie_by_title(title)
        if movie:
            self.__movies.remove(movie)
            return movie
        
        print(f'В коллекции "{self._name}" нет фильма "{title}"')
        return False
    
    def get_movie_by_title(self, title):
        """
        Находит фильм по названию.
        
        Аргументы:
            title - название фильма (строка)
        
        Возвращает:
            Movie() - если фильм найден
            False - если не найден
        
        """

        if not self.__movies:
            print(f'В коллекции "{self._name}" еще нет фильмов!')
            return False
        
        # Найдем фильм
        for movie in self.__movies:
            if title == movie.info_in_tuple()[0]: # Если название фильма есть в коллекции
                return movie
        
        print(f'В коллекции "{self._name}" нет фильма "{title}"')
        return False
    
    def rate_movie(self, title, rating):
        """
        Устанавливает рейтинг для фильма.
        
        Аргументы:
            rating - рейтинг (число 1-10)
            title - название фильма (строка)
            
        Возвращает:
            Movie() - если оценивание прошло успешно
            False - если возникла ошибка (неправильный рейтинг или несуществующий фильм)
        """
        
        if not 1 <= rating <= 10:
            print('Рейтинг должен быть от 1 до 10!')
            return False
        
        movie = self.get_movie_by_title(title)
        
        if movie:
            movie.set_rating(rating)
            return movie

        print(f'Фильма "{title}" нет в вашей коллекции!')
        return False
    def get_top_movies(self, limit=5):
        """
        Возвращает топ-N фильмов по рейтингу.
        
        Аргументы:
            limit - количество книг для вывода в топ
            
        Возвращает:
            list() - список топ-N фильмов.
            Fasle - если произошла ошибка
        """
        list_rated_movies = [movie.info_in_tuple() for movie in self.__movies if movie.info_in_tuple()[1]['Рейтинг']] # Список оцененных фильмов, представленных в виде списка кортежей (название, рейтинг)
        
        if limit > len(list_rated_movies):
            print(f'В коллекции {self._name} нет столько фильмов с рейтингом!')
            return False
        
        if not self.__movies:
            print(f'В коллекции {self._name} еще нет фильмов!')
            return False
        
        
        sorted_list_movies = sorted(list_rated_movies, key=lambda x: x[1]['Рейтинг'], reverse=True) # Отсортированный список фильмов, представленных в виде списка кортежей (название, рейтинг) 
        top_films = [self.get_movie_by_title(info[0]) for info in sorted_list_movies] # Топ-N фильмов
        return top_films
    
    def get_movies_by_genre(self, genre):
        """
        Возвращает все фильмы указанного жанра.
        
        Аргументы:
            genre - жанр (строка)
        
        Возвращает:
            list() - если найдены фильмы данного жанра
            False - если не найдены
        """

        if not self.__movies:
            print(f'В коллекции "{self._name}" еще нет фильмов!')
            return False
        
        movies_by_genre = [] # Фильмы данного жанра
        for movie in self.__movies:
            if genre == movie.info_in_tuple()[1]['Жанр']:
                movies_by_genre.append(movie)
            
        if movies_by_genre:
            return movies_by_genre
        
        print(f'В коллекции "{self._name}" нет фильмов жанра "{genre}"')
        return False
    
    def __str__(self):
        """
        Строковое представление коллекции фильмов
        
        Возвращает:
            str()
        """
        
        genres = [] # Жанры
        directors = [] # Режиссеры
        
        for movie in self.__movies:
            desc_movie = movie.info_in_tuple()[1]
            genres.append(desc_movie['Жанр'])
            directors.append(desc_movie['Режиссёр'])
        
        most_common_genre = Counter(genres).most_common(1) # Самый популярный жанр в коллекции
        most_common_director = Counter(directors).most_common(1) # Самый популярный режиссер в коллекции
        return f"""Коллекция "{self._name}"
            Фильмов в коллекции: {self.quantity_movies}
            Самый популярный режиссер: {f'{most_common_director[0][0]} ({most_common_director[0][1]} фильмов)' if most_common_director[0][1] > 1 else 'неопредёл'}
            Самый популярный жанр: {f'{most_common_genre[0][0]} ({most_common_genre[0][1]} фильмов)' if most_common_genre[0][1] > 1 else 'неопредёл'}
            """

    def get_stats(self):
        """
        Возвращает статистику коллекции.
        
        Возвращает:
            dict()
        """
        
        stats = { # Статистика коллекции
            'total_movies': 0,
            'rated_movies': 0,
            'average_rating': 0,
            'most_common_genre': 'не определен',
            'high_rated_count': 0        
        }
        
        # Если еще нет фильмов
        if not self.__movies:
            return stats
        
        
        rated_movies = 0 # Количество оцененных фильмов
        average_rating = 0 # Средний рейтинг (только для оцененных)
        most_common_genre = '' # Самый популярный жанр
        high_rated_count = 0 # Количество фильмов с рейтингом ≥ 8
        genres = [] # Жанры
        
        for movie in self.__movies:
            if movie.info_in_tuple()[1]['Рейтинг']:
                average_rating += movie.info_in_tuple()[1]['Рейтинг']
                rated_movies += 1
                if movie.is_high_rated():
                    high_rated_count += 1
        
        for movie in self.__movies:
            desc_movie = movie.info_in_tuple()[1]
            genres.append(desc_movie['Жанр'])
        
        most_common_genre = Counter(genres).most_common(1)[0][1]
        average_rating /= rated_movies
        stats['total_movies'] = len(self.__movies)
        stats['rated_movies'] = rated_movies
        stats['average_rating'] = average_rating    
        stats['most_common_genre'] = most_common_genre
        stats['high_rated_count'] = high_rated_count
        
        return stats
    

# ТЕСТ    

# Создаем коллекцию
my_collection = MovieCollection("Мои любимые фильмы")
my_collection1 = MovieCollection("Мои любимые фильмы 2")

# Создаем фильмы
film1 = Movie("Начало", "Кристофер Нолан", 2010, "фантастика")
film2 = Movie("Крестный отец", "Фрэнсис Форд Коппола", 1972, "драма")
film3 = Movie("Интерстеллар", "Кристофер Нолан", 2014, "фантастика")
film4 = Movie("1+1", "Оливье Накаш", 2011, "драма")
film5 = Movie("Темный рыцарь", "Кристофер Нолан", 2008, "фантастика")
film6 = Movie("Леон", "Люк Бессон", 1994, "боевик")
film6 = Movie("Леон", "Люк Бессон", 1994, "боевик")

# Добавляем в коллекцию
my_collection.add_movie(film1)
my_collection.add_movie(film2)
my_collection.add_movie(film3)
my_collection.add_movie(film4)
my_collection.add_movie(film5)
my_collection.add_movie(film6)

# Удалим фильм
removed_movie = my_collection.remove_movie('Untitled')
removed_movie1 = my_collection.remove_movie('Начало')
removed_movie2 = my_collection1.remove_movie('Начало')

print(removed_movie, removed_movie1, removed_movie2)

# Оценим фильмы
film1.set_rating(10000)
my_collection.rate_movie('Начало', -1)
my_collection.rate_movie('цуа', 1000)
my_collection.rate_movie('1+1', 10)
my_collection.rate_movie('Интерстеллар', 8.5)


print(film4)

# Получим фильм по названию
print(my_collection.get_movie_by_title('фантастика'))
print(my_collection.get_movie_by_title('начало'))
print(my_collection.get_movie_by_title('Интерстеллар'))

# Получим фильмы по жанру
movies_by_genre1 = my_collection.get_movies_by_genre('фантастика')
movies_by_genre2 = my_collection.get_movies_by_genre('Фантастика')
movies_by_genre3 = my_collection.get_movies_by_genre('боевик')

for movie in movies_by_genre1:
    print(movie)
for movie in movies_by_genre3:
    print(movie)

# Получим топ-3 фильма по рейтингу
top = my_collection.get_top_movies(3)
if top:
    for movie in top:
        print(movie)
print(top)

# Получим фильм по названию
film = my_collection.get_movie_by_title('Крестный отец')
print(film)
film = my_collection.get_movie_by_title('интерстеллар')
print(film)

# Получим статистику
print(my_collection.get_stats())
