# Код для генерации тестовых логов
import random
from datetime import datetime, timedelta

methods = ['GET', 'POST', 'PUT', 'DELETE']
paths = ['/index.html', '/api/users', '/api/products', '/admin', '/login', '/static/style.css']
status_codes = [200, 201, 304, 400, 401, 403, 404, 500]
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0)',
    'Chrome/120.0.0.0 Safari/537.36',
    'Python-requests/2.31.0',
    'curl/7.88.1'
]

with open('server.log', 'w', encoding='utf-8') as f:
    base_time = datetime(2024, 3, 15, 10, 0, 0)
    for i in range(25):
        time = base_time + timedelta(minutes=i*2)
        ip = f"192.168.1.{random.randint(1, 50)}"
        method = random.choice(methods)
        path = random.choice(paths)
        status = random.choice(status_codes)
        size = random.randint(100, 5000)
        agent = random.choice(user_agents)
        
        f.write(f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] {ip} - {method} "{path}" {status} {size} "{agent}"\n')


def analyze_server_logs(log_file):
    """
    Читает файл логов и возвращает файл со статистикой
    
    Параметры:
        log_file - файл с логами(str)
    
    Возвращает:
        dict()
    """
    stats = {
        'total_requests': 0,           # Общее количество запросов
        'requests_by_method': {},      # Запросы по HTTP-методам
        'requests_by_status': {},      # Запросы по кодам ответа
        'top_ips': [],                 # Топ-5 IP-адресов по запросам
        'errors_4xx_5xx': 0,           # Количество ошибочных запросов (4xx, 5xx)
        'busiest_hour': '',            # Самый загруженный час
        'largest_response': 0          # Максимальный размер ответа
    }
    
    global status_codes
    # ШАГ 1. Посчитаем запросы по HTTP-методам и кол-во запросов
    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            stats['total_requests'] = len(lines)
    except FileNotFoundError:
        print(f'Файла "{log_file}" не существует')
        return False
    stats['requests_by_method']['GET'] = 0
    stats['requests_by_method']['POST'] = 0
    stats['requests_by_method']['PUT'] = 0
    stats['requests_by_method']['DELETE'] = 0
    for line in lines:
        if 'GET' in line:
            stats['requests_by_method']['GET'] += 1
        elif 'POST':
            stats['requests_by_method']['POST'] += 1
        elif 'PUT':
            stats['requests_by_method']['PUT'] += 1
        elif 'DELETE':
                    stats['requests_by_method']['DELETE'] += 1

    
    # ШАГ 2. Посчитаем запросы по кодам ответа
    for status in status_codes:
        stats['requests_by_status'][status] = 0
            
    for line in lines:
        for status in status_codes:
            if str(status) in line:
                stats['requests_by_status'][status] += 1
    
    # ШАГ 3. Высчитаем топ-5 ip-адресов по запросам
    id_dict = {} # Словарь с id и количеством запросов 
    for line in lines: # Строка в файле
        for word in line.split(): # Слово в файле
            if '192' in word: # Если слово - ip
                if id_dict.get(word):
                    id_dict[word] += 1
                else:
                    id_dict[word] = 1
            
    top_id_dict = sorted(id_dict.items(), key=lambda x: x[1], reverse=True) # Сортируем
    top_id_dict = dict(top_id_dict[:5]) # Преобразуем обратно в словарь
    stats['top_ips'] = top_id_dict
        
    # ШАГ 4. Найдем количество ошибочных запросов
    errors = {}
    for line in lines:
        for word in line.split():
            if word in status_codes:
                if word[0] == '4' or word[0] == '5':
                    if errors.get(word):
                        errors[word] += 1
                    else:
                        errors[word] = 1
            
    stats['errors_4xx_5xx'] = errors

    # ШАГ 5. Найдем максимальный размер ответа
    sizes = []
    for line in lines:
        sizes.append(line[7])
    
    stats['largest_response'] = max(sizes)
        
    return stats
def generate_log_report(stats):
    """
    Выводит красивый отчет
    
    Параметры:
        stats - словарь с данными(словарь)
    """
    
    print('=== ОТЧЕТ ПО ЛОГАМ СЕРВЕРА ===\n')
    print('📊 Общая статистика:')
    print(f'Всего запросов: {stats['total_requests']}')
    print(f'Максимальный размер ответа: {stats['largest_response']} байт\n')
    print('🔍 Распределение по методам:')
    get = stats['requests_by_method']['GET'] / stats['total_requests'] * 100
    post = stats['requests_by_method']['POST'] / stats['total_requests'] * 100
    put = stats['requests_by_method']['PUT'] / stats['total_requests'] * 100
    delete = stats['requests_by_method']['DELETE'] / stats['total_requests'] * 100
    print(f'GET: {stats['requests_by_method']['GET']} запросов ({get:.1f}%)')
    print(f'POST: {stats['requests_by_method']['POST']} запросов ({post:.1f})')
    print(f'DELETE: {stats['requests_by_method']['DELETE']} запросов ({delete:.1f}%)')
    print(f'PUT: {stats['requests_by_method']['PUT']} запросов ({put:.1f}%)\n')
    print('📈 Коды ответов:')
    for code, value in stats['requests_by_status'].items():
        code_persont = value / stats['total_requests'] * 100
        print(f'{code}: {value} ({code_persont:.1f}%)')
    print()
    print('🌐 Топ-5 IP-адресов:')
    for ip, value in stats['top_ips'].items():
        print(f'{ip}: {value} запросов')


stats = analyze_server_logs('server.log')
generate_log_report(stats)