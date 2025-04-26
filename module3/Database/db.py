import psycopg
from check_input_data import start_check

class Database():
    def __init__(self):
        self.connection = self.connection_db()

    def connection_db(self):
        '''
        Функция для подключения к БД
        :return: connection object
        '''
        try:
            conn = psycopg.connect(
                host = 'winserver001.asuscomm.com',
                user =  'admin',
                password =  'admin',
                dbname =  'demolearning',
                port = 5432
            )
            print("Подключение установлено")
            return conn
        except Exception as error:
            print(f'Ошибка подключения: {error}')
            return None

    def take_all_partners(self):
        '''
        Функция получения информации о всех партнерах
        :return: partner_info - список с инфо о партнере
        '''
        try:
            query = '''
                select * from partners_import;
                '''

            cursor = self.connection.cursor()
            cursor.execute(query)
            partner_info = []

            for row in cursor.fetchall():
                partner_info.append({
                    'type_partner': row[0].strip(),
                    'partner_name': row[1].strip(),
                    'director': row[2].strip(),
                    'email_partner': row[3].strip(),
                    'partner_phone': row[4].strip(),
                    'ur_adres': row[5].strip(),
                    'inn_partner': row[6].strip(),
                    'rate_partner': row[7].strip(),
                })
            self.connection.commit()
            cursor.close()
            return partner_info
        except Exception as error:
            print(error)
            return []

    def sum_cost_partners(self, partner_name):
        '''
        Функция для получения стоимости продаж партнера
        :return: cost или 0 в случае ошибки/отсутствия данных
        '''
        try:
            query = f'''
                SELECT COALESCE(SUM(count_products), 0) 
                FROM partner_products_import
                WHERE partner_name_fk = '{partner_name}';
                '''

            cursor = self.connection.cursor()
            cursor.execute(query)
            cost = cursor.fetchone()[0]
            cursor.close()
            return cost

        except Exception as error:
            print(f'Ошибка: {error}')
            return 0  # Возвращаем 0 вместо None в случае ошибки

    def take_partner_info(self, partner_name: str):
        '''
        Функция получения информации о партнере
        :param partner_name: Имя партнера
        :return:
        '''
        try:
            query = f'''
            SELECT *
            FROM partners_import
            WHERE partner_name = '{partner_name}';
            '''
            cursor = self.connection.cursor()
            cursor.execute(query)
            partner_info = dict()
            for data in cursor.fetchall():
                partner_info = {
                    'type_partner': data[0].strip(),
                    'partner_name': data[1].strip(),
                    'director': data[2].strip(),
                    'email_partner': data[3].strip(),
                    'partner_phone': data[4].strip(),
                    'ur_adres': data[5].strip(),
                    'inn_partner': data[6].strip(),
                    'rate_partner': data[7].strip(),
                }
            cursor.close()
            return partner_info
        except Exception as error:
            print(f'Ошибка: {error}')
            # При ошибке возвращается пустой словарь
            return dict()

    def update_partner_info(self, partner_name: str, partner_info: dict):
        '''
        Функция обновления данных о партнере
        :param partner_name: имя партнера
        :param partner_info: словарь с данными о партнере
        :return:
        '''
        try:
            query = f'''
                UPDATE partners_import
                SET
                partner_name = '{partner_info["partner_name"]}',
                director = '{partner_info["director"]}',
                email_partner = '{partner_info["email_partner"]}',
                partner_phone = '{partner_info["partner_phone"]}',
                ur_adres = '{partner_info["ur_adres"]}',
                inn_partner = '{partner_info["inn_partner"]}',
                rate_partner = '{partner_info["rate_partner"]}'
                WHERE partner_name = '{partner_name}';
            '''
            if not start_check(partner_info):
                return False
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as error:
            print(f'Ошибка: {error}')

    def add_partner_info(self, partner_info: dict):
        '''
        Функция добавления нового партнера
        :param partner_info: словарь с данными о партнере
        :return: True если успешно, False если ошибка
        '''
        try:
            query = '''
                INSERT INTO partners_import (
                    type_partner,
                    partner_name,
                    director,
                    email_partner,
                    partner_phone,
                    ur_adres,
                    inn_partner,
                    rate_partner
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s
                )
            '''
            values = (
                partner_info["type_partner"],
                partner_info["partner_name"],
                partner_info["director"],
                partner_info["email_partner"],
                partner_info["partner_phone"],
                partner_info["ur_adres"],
                partner_info["inn_partner"],
                partner_info["rate_partner"]
            )
            
            if not start_check(partner_info):
                return False
            
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            return True
        
        except Exception as error:
            print(f'Ошибка: {error}')
            return False
