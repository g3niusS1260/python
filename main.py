emails = [ # Список с email
    "user1@example.com",
    "user2@example.com", 
    "user1@example.com",  # Дубликат
    "user3@example.com",
    "user2@example.com",  # Дубликат
    "admin@example.com",
    "user4@example.com"
]

# Создадим множество email без дубликатов
unique_emails = set(emails)

# Создадим список дубликатов
duplicate_list = []

for email in emails:
    if emails.count(email) > 1:
        duplicate_list.append(email)

# Сколько был оудалено дубликатов
quentity_duplicates = len(emails) - len(duplicate_list)

isEmailInSet = "admin@example.com" in unique_emails

print(f'Удалено дубликатов: {quentity_duplicates}')
print(f'Список уникальных email: {unique_emails}')
print(f'Наличие почты админа: {isEmailInSet}')

