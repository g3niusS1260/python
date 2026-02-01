# АНАЛИЗАТОР ПРОДАЖ

import datetime
sales = [
    {
        'date': '2024-01-01',
        'product': 'Ноутбук',
        'category': 'Электроника',
        'price': 75000,
        'quantity': 2,
        'seller': 'Иванов'
    },
    {
        'date': '2024-02-01',
        'product': 'Компьютерная мышь',
        'category': 'Электроника',
        'price': 3000,
        'quantity': 2,
        'seller': 'Сидоров'
    },
    {
        'date': '2024-12-01',
        'product': 'Посудомоечная машина',
        'category': 'Бытовая техника',
        'price': 80000,
        'quantity': 1,
        'seller': 'Иванов'
    },
    {
        'date': '2024-19-01',
        'product': 'Клавиатура',
        'category': 'Электроника',
        'price': 7000,
        'quantity': 5,
        'seller': 'Матросов'
    },
    {
        'date': '2024-30-01',
        'product': 'Зарядка',
        'category': 'Бытовая техника',
        'price': 700,
        'quantity': 3,
        'seller': 'Иванов'
    },
    {
        'date': '2024-30-01',
        'product': 'Духовка',
        'category': 'Бытовая техника',
        'price': 70000,
        'quantity': 3,
        'seller': 'Матросов'
    }
]

def total_revenue(sales):
    """
    Расчитывает общую выручку

    Параметры:
        sales - продажи(список)
    
    Возвращает:
        int() - если не возникло ошибок
        False - если ошибки возникли
    """
    
    if not sales:
        print('В вашем списке еще нет продаж')
        return False
    
    total = 0
    for sale in sales:
        total += (sale['price'] * sale['quantity'])
    
    return total

def best_selling_product(sales):
    """
    Находит товар с максимальным количеством продаж
    
    Параметры:
        sales - продажи(список)
        False - если ошибки возникли
    """
    
    if not sales:
        print('В вашем списке еще нет продаж')
        return False
    
    best_product = { # Лучший продукт по продажам
        'product' : '',
        'category': '',
        'quantity': 0,
        'price': 0
    }
    
    for sale in sales:
        if sale['quantity'] > best_product['quantity']:
            best_product['product'] = sale['product']
            best_product['category'] = sale['category']
            best_product['price'] = sale['price']
            best_product['quantity'] = sale['quantity']
    
    return best_product

def best_seller(sales):
    """
    Находит продовца с максимальной выручкой
    
    Параметры:
        sales - продажи(список)
    
    Возвращает:
        dict() - словарь {'Имя продовца': 'Выручка продавца'}
        False - если ошибки возникли
    """
    if not sales:
        print('В вашем списке еще нет продаж')
        return False
    
    b_seller = { # Лучший продавец
        'name': '',
        'revenue': 0
    }
    
    sellers_names = [] # Список имен продавцов
    for sale in sales:
        if sale['seller'] not in sellers_names:
            sellers_names.append(sale['seller'])
    
    sellers_data = {} # Словарь продавец: выручка
    for seller_name in sellers_names: # Создаем список словарей продавцов 
        sellers_data[seller_name] = 0
    
    # Установим выручку для продавцов
    for seller_name in sellers_data.keys():
        for sale in sales:
            if seller_name == sale['seller']:
                sellers_data[seller_name] += sale['price'] * sale['quantity']
    
    # Получим лучшего продавца 
    for seller_name, revenue in sellers_data.items():
        if revenue > b_seller['revenue']:
            b_seller = {
                'name': seller_name,
                'revenue': revenue
            }
    
    return b_seller

def sales_by_category(sales):
    """
    Показывает выручку в каждой категории продаж (Бытовая техника, электроника)
    
    Параметры:
        sales - продажи(список)
    
    Возвращает:
        dict() - словарь {'Категория': 'Выручка'}
        False - если ошибки возникли
    """
    if not sales:
        print('В вашем списке еще нет продаж')
        return False
    
    # ШАГ 1. Создадим список категорий
    categories = []
    
    for sale in sales:
        if sale['category'] not in categories:
            categories.append(sale['category'])
    
    # ШАГ 2. Создадим словарь с категориями и нулями вместо выручки
    sale_category = {}
    for category in categories:
        sale_category[category] = 0
    
    # ШАГ 3. Обозначим выручку по категориям
    for category in sale_category.keys():
        for sale in sales:
            if sale['category'] == category:
                sale_category[category] += sale['price'] * sale['quantity']
    
    return sale_category

def daily_sales(sales):
    """
    Возвращает словарь выручка по дням
    
    Параметры:
        sales - продажи(список)
    
    Возвращает:
        dict() - словарь день: выручка
        False - если возникла ошибка
    """
    if not sales:
        print('В вашем списке еще нет продаж')
        return False
    
    # ШАГ 1. Создадим список дат
    dates = []
    for sale in sales:
        if sale['date'] not in dates:
            dates.append(sale['date'])
    
    # ШАГ 2. Создадим словарь дата: выручка
    d_sales = {}
    for date in dates:
        d_sales[date] = 0
    
    # ШАГ 3. Установим выручку по дням
    for day, revenue in d_sales.items():
        for sale in sales:
            if sale['date'] == day:
                revenue += sale['price'] * sale['quantity']
                d_sales[day] = revenue
    
    # ШАГ 4. Вернем словарь с выручкой по дням
    return d_sales
            
def add_sale(sales, new_sale):
    """
    Добавляет новую продажу
    
    Параметры:
        sales - продажи(список)
        new_sale - продажа(словарь)
    
    Возвращает:
        dict() - новая продажа
        False - если возникла ошибка
    """
    if not new_sale:
        print('Нет информации о продаже')
        return False
    
    # ШАГ 1. Проверим, есть ли нужные поля в словаре
    if not new_sale.get('date'):
        print('В продаже не указана дата')
        return False
    if not new_sale.get('product'):
        print('В продаже не указан продукт продажи')
        return False
    if not new_sale.get('category'):
        print('В продаже не указана категория продукта продажи')
        return False
    if not new_sale.get('price'):
        print('В продаже не указана цена продукта продажи')
        return False
    if not new_sale.get('quantity'):
        print('В продаже не указано количество проданного товара')
        return False
    if not new_sale.get('seller'):
        print('В продаже не указан продавец')
        return False
    
    # ШАГ 2. Проверим корректность латы
    try:
        datetime.datetime.strptime(new_sale['date'], '%Y-%d-%m')
    except ValueError:
        print('Дата указана неправильно (нужный формат: год-число-месяц)')
        return False
    
    # ШАГ 3. Добавим продажу в список и вернем ее
    sales.append(new_sale)
    return new_sale

def generate_report(sales, start_date, end_date):
    """
    Делает отчет за конкретный период времени
    
    Параметры:
        sales - список продаж(список)
        start_date - откуда начинать отчет
        end_date - до куда идет отчет
    
    Возвращает:
        list()
    """
    
    if not sales:
        print('Продажи отсутствуют')
        return False

    report = []
    
    try: 
        start = datetime.datetime.strptime(start_date, '%Y-%d-%m')
        end = datetime.datetime.strptime(end_date, '%Y-%d-%m')
    except ValueError:
        print('Дата(ы) указаны неверно')
        return False
    
    for sale in sales:
        if start <= datetime.datetime.strptime(sale['date'], '%Y-%d-%m') <= end:
            report.append(sale)
    
    return report
    
# Тестовые данные
sales = [
    {'date': '2024-01-01', 'product': 'Ноутбук', 'category': 'Электроника', 
     'price': 75000, 'quantity': 2, 'seller': 'Иванов'},
    {'date': '2024-01-01', 'product': 'Мышь', 'category': 'Электроника', 
     'price': 1500, 'quantity': 5, 'seller': 'Петров'},
    # ...
]

print(f"Общая выручка: {total_revenue(sales)} руб.")
print(f"Лучший товар: {best_selling_product(sales)}")
print(f"Лучший продавец: {best_seller(sales)}")
