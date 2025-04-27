"""
Модуль для проверки корректности данных партнера

Содержит функции для валидации различных полей формы партнера
"""

def start_check(partners_input_data: dict) -> bool:
    """
    Функция вызова всех проверок для данных партнера
    
    :param partners_input_data: Словарь с данными партнера
    :return: True если все проверки пройдены, False в противном случае
    """
    return all([
        check_inn(partners_input_data['inn_partner']),
        check_mail(partners_input_data['email_partner']),
        check_rate(int(partners_input_data['rate_partner'])),
        check_phone(partners_input_data['partner_phone']),
        check_org_name(partners_input_data['partner_name']),
        check_dir_name(partners_input_data['director']),
        check_ur_addr(partners_input_data['ur_adres'])
    ])

def check_org_name(partner_name: str) -> bool:
    """
    Проверка корректности названия организации
    
    :param partner_name: Название организации
    :return: True если название корректно, False в противном случае
    """
    if len(partner_name) > 0:
        return True
    print("Введите имя партнера!")
    return False

def check_dir_name(dir_name: str) -> bool:
    """
    Проверка корректности ФИО директора
    
    :param dir_name: ФИО директора
    :return: True если ФИО корректно, False в противном случае
    """
    # Проверка что ФИО состоит из трех частей (Фамилия Имя Отчество)
    if len(dir_name.split()) == 3:
        return True
    print("Введите ФИО директора (Фамилия Имя Отчество)!")
    return False

def check_rate(rate: int) -> bool:
    """
    Проверка корректности рейтинга
    
    :param rate: Рейтинг партнера
    :return: True если рейтинг корректен, False в противном случае
    """
    try:
        if 1 <= rate <= 10:
            return True
        print("Введите рейтинг от 1 до 10!")
        return False
    except Exception:
        print("Введите рейтинг от 1 до 10!")
        return False

def check_phone(phone_number: str) -> bool:
    """
    Проверка корректности номера телефона
    
    :param phone_number: Номер телефона
    :return: True если номер телефона корректен, False в противном случае
    """
    if (len(phone_number) == 13):
        return True
    print("Введите корректный номер телефона!")
    return False

def check_mail(mail_address: str) -> bool:
    """
    Проверка корректности адреса электронной почты
    
    :param mail_address: Адрес электронной почты
    :return: True если адрес электронной почты корректен, False в противном случае
    """
    # Проверка формата email (содержит @ и домен с точкой)
    if (len(mail_address.split("@")) == 2 and 
            len(mail_address.split("@")[-1].split(".")) == 2):
        return True
    print("Введите корректный адрес электронной почты!")
    return False

def check_inn(inn: str) -> bool:
    """
    Проверка корректности ИНН
    
    :param inn: ИНН партнера
    :return: True если ИНН корректен, False в противном случае
    """
    # ИНН должен содержать 10 цифр
    if inn.isdigit() and len(inn) == 10:
        return True
    print("Введите корректный ИНН (10 цифр)")
    return False

def check_ur_addr(ur_addr: str) -> bool:
    """
    Проверка корректности юридического адреса
    
    :param ur_addr: Юридический адрес
    :return: True если юридический адрес корректен, False в противном случае
    """
    # Адрес должен содержать индекс и минимум 3 компонента адреса
    parts = ur_addr.split(",")
    if (len(parts) > 2 and 
            len(parts[0]) == 6 and 
            parts[0].isdigit()):
        return True
    print("Введите корректный юридический адрес (начинается с индекса)")
    return False