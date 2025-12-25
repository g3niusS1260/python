contacts = dict() # Телефонная книга

# Добавим контакты
contacts['Иван'] = '+7-123-456-78-90'
contacts['Мария'] = '+7-987-654-32-10'
contacts['Алексей'] = '+7-111-222-33-44'

# Найдем телефон по имени 'Алексей'
print('Алексей: ', contacts['Алексей'])

# Удалим контакт 'Мария'
delete_contact = contacts.pop('Мария')
print('Удаленный контакт: ', delete_contact)

# Выведем все контакты
print()
print('=' * 40)
print('ВСЕ КОНТАКТЫ')

for name, number in contacts.items():
    print(f'Контакт: {name}\nТелефон: {number}\n\n')
    
