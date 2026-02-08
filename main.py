# ELO-рейтинг

# ФУНКЦИЯ РАСЧЁТА ИЗМЕНЕНИЯ
def get_rating_delta(rating_a, rating_b, result):
    """
    Считает, насколько изменится рейтинг при игре для игрока a
    
    Параметры:
        rating_a(int) - рейтинг для игрока 'a'
        ratinb_b(int) - рейтинг соперника игрока 'a'(игрока 'b')
        result(int) - результат матча для игрока 'a'. (1 - победил, 0 - проиграл, 0.5 - ничья)
    Возвращает:
        int() - на сколько изменился рейтинг
    """
    
    # Вычислим вероятность победы 'a' по формуле
    chance_to_win = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    
    # Вычислим изменение рейтинга для игрока 'a' по формуле
    change = 32 * (result - chance_to_win)
    
    # Возвращаем округленное изменение рейтинга
    return round(change)
# РЕГИСТРАЦИЯ МАТЧА
def register_match(p1_id, p2_id, winner):
    """
    1. Регестрирует матч
    2. Обновляет рейтинг для каждого игрока
    3. Увеличивает количество матчей
    
    Параметры:
        p1_id(int) = id первого игрока
        p2_id(int) = id второго игрока
        winner(int) - победитель (1 - победил первый, 2 - победил второй, 0 - ничья)
    
    Возвращает:
        True - матч успешно заригестрирован
        False - возникли проблемы в процессе регистрации
    """
    
    # Проверим, есть ли такие игроки
    global players
    if p1_id not in players.keys():
        print(f'Игрока с id {p1_id} не существует')
        return False
    if p2_id not in players.keys():
        print(f'Игрока с id {p2_id} не существует')
        return False

    # Если передан один и тот же игрок
    if p1_id == p2_id:
        print('Невозможный матч (игрок против самого себя)')
        return False
    # Получим результат игры для каждого игрока (1 - победил, 0 - проиграл, 0.5 - ничья)
    if winner == 1: # Победа первого
        p1_result = 1
        p2_result = 0
    elif winner == 2: # Победа второго
        p2_result = 1
        p1_result = 0
    elif winner == 0: # Ничья
        p1_result = 0.5
        p2_result = 0.5
        
    # Получим изменения рейтинга каждого игрока
    change_p1 = get_rating_delta(players[p1_id]['rating'], players[p2_id]['rating'], p1_result) # На сколько изменился рейтинг 1-ого
    change_p2 = get_rating_delta(players[p2_id]['rating'], players[p1_id]['rating'], p2_result) # На сколько изменился рейтинг 2-ого

    # Обновим рейтинг игроков
    players[p1_id]['rating'] += change_p1
    players[p2_id]['rating'] += change_p2
    
    # Увеличим количество матчей для каждого игрока 
    players[p1_id]['matches'] += 1
    players[p2_id]['matches'] += 1

    print(f'{'👍' if change_p1 > 0 else '👎'} Рейтинг игрока {players[p1_id]['name']} изменился на {change_p1}')
    print(f'{'👍' if change_p2 > 0 else '👎'} Рейтинг игрока {players[p2_id]['name']} изменился на {change_p2}')
    return True

players = {
    1: {"name": "Алексей", "rating": 1000, "matches": 0},
    2: {"name": "Мария", "rating": 1000, "matches": 0},
    3: {"name": "Дмитрий", "rating": 1000, "matches": 0}
}

# ТАБЛИЦА ЛИДЕРОВ
def show_leaderboard():
    """
    Выводит таблицу лидеров. 
    
    Возвращает:
        dict() - отсортированный словарь игроков
    """
    print('\n<<< ТАБЛИЦА ЛИДЕРОВ >>>\n')
    
    # Создадим отсортированный список по ELO
    global players
    
    # Получим элементы словаря с игроками (id: {'name' : ...})
    sorted_players_list = list(players.items())
    
    # Преобразуем сортированный список в словарь
    sorted_players = dict(sorted(sorted_players_list, key=lambda x: x[1]['rating'], reverse=True))
    
    # Выведем таблицу лидеров
    i = 0 
    for id, player in sorted_players.items():
        print(f'{i + 1}. {player['name']}[id: {id}] - {player['rating']} очков ({player['matches']} матчей)')
        i += 1
    
    # Вернем таблицу лидеров
    return sorted_players
    
# Матчи Дмитрия
register_match(3, 1, 1)
register_match(3, 1, 0)
register_match(3, 1, 2)
register_match(3, 2, 0)
register_match(3, 2, 1)
register_match(3, 1, 1)
register_match(3, 1, 1)
register_match(1, 3, 1)
register_match(2, 3, 1)
register_match(3, 3, 1)

show_leaderboard()