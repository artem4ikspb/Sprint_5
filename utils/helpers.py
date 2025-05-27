import random
import string

def generate_random_email():
    # Генерация случайного локального имени (до @)
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    
    # Генерация случайного домена
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    
    # Выбор случайного домена верхнего уровня
    tld = random.choice(['com', 'net', 'org', 'ru', 'info', 'biz'])
    
    # Формирование полного email-адреса
    email = f"{local_part}@{domain}.{tld}"
    return email


def generate_random_password():
    return "password"


def get_random_unit(units):
    size = len(units)
    return random.choices(units)