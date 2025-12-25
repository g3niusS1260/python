user1_hobbies = {"чтение", "программирование", "музыка", "спорт"}
user2_hobbies = {"спорт", "путешествия", "фотография", "программирование"}

# Найдем интересы которые есть только у первого пользователя 
user1_unique_hobbies = user1_hobbies - user2_hobbies # Аналогично с user1_hobbies.difference(user2_hobbies)
print(f'Хобби, которые есть только у первого пользователя: {user1_unique_hobbies}')

# Найдем интересы которые есть только у второго пользователя 
user2_unique_hobbies = user2_hobbies - user1_hobbies # Аналогично с user2_hobbies.difference(user1_hobbies)
print(f'Хобби, которые есть только у второго пользователя: {user2_unique_hobbies}')

# Найдём общие интересы 
common_hobbies = user1_hobbies.intersection(user2_hobbies) # Аналогично с user1_hobbies & user_hobbies
print(f'Общие интересы: {common_hobbies}')

# Найдем уникальные интересы для двух пользователей
unique_hobbies = user1_unique_hobbies | user2_unique_hobbies # Аналогично с user1_unique_hobbies.union(user2_unique_hobbies)
print(f'Уникальные интересы интересы: {unique_hobbies}')