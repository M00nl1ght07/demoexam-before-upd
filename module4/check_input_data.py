def start_check(partners_input_data: dict):
    """
    Функция вызова проверок для данных
    :param partners_input_data: Словарь с датами проверки
    :return: Результат проверки True / False
    """
    if (
            check_inn(partners_input_data['inn_partner']) and
            check_mail(partners_input_data['email_partner']) and
            check_rate(int(partners_input_data['rate_partner'])) and
            check_phone(partners_input_data['partner_phone']) and
            check_org_name(partners_input_data['partner_name']) and
            check_dir_name(partners_input_data['director']) and
            check_ur_addr(partners_input_data['ur_adres'])
    ):
        return True
    return False

def check_org_name(partner_name: str):
    if len(partner_name) != 0:
        return True
    print("Введите имя партнера!")
    return False


def check_dir_name(dir_name: str):
    if len(dir_name.split(" ")) == 3:
        return True
    print("Введите имя директора!")
    return False


def check_rate(rate: int):
    try:
        if rate in range(1, 11):
            return True
        print("Введите рейтинг от 1 до 10!")
        return False
    except Exception:
        print("Введите рейтинг от 1 до 10!")
        return False


def check_phone(phone_number: str):
    if (len(phone_number) == 13 and
            phone_number[0] in ['9', '8', '4']):
        return True
    print("Введите корректный номер телефона!")
    return False


def check_mail(mail_address: str):
    if (len(mail_address.split("@")) == 2 and
            len(mail_address.split("@")[-1].split(".")) == 2):
        return True
    print("Введите корректный адрес электронной почты!")
    return False


def check_inn(inn: str):
    if inn.isdigit() and len(inn) == 10:
        return True
    print("Введите корректный ИНН")
    return False


def check_ur_addr(ur_addr: str):
    if (len(ur_addr.split(",")) > 2 and
            len(ur_addr.split(",")[0]) == 6 and
            ur_addr.split(",")[0].isdigit()):
        return True
    print("Введите корректный юридический адрес")
    return False