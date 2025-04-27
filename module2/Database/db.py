"""
Модуль для работы с базой данных

Содержит класс Database для выполнения операций с базой данных системы "Мастер пол"
"""
import psycopg

class Database:
    """
    Класс для работы с базой данных системы "Мастер пол"
    
    Обеспечивает подключение к БД и выполнение основных операций
    """
    def __init__(self):
        """Инициализация класса базы данных"""
        self.connection = self.connection_db()
  
    def connection_db(self):
        """
        Подключение к базе данных
        
        :return: Объект соединения с БД или None при ошибке
        """
        try:
            conn = psycopg.connect(
                host = 'winserver001.asuscomm.com',
                user = 'admin',
                password = 'admin',
                dbname = 'demoupd',
                port = 5432
            )
            print("Подключение к БД установлено")
            return conn
        except Exception as err:
            print(f'Ошибка подключения: {err}')
            return None

    def take_all_partners(self):
        """
        Получение информации о всех партнерах
        
        :return: Список словарей с информацией о партнерах или пустой список при ошибке
        """
        try:
            query = "SELECT * FROM partners_import;"
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
            cursor.close()
            return partner_info
        except Exception as err:
            print(f'Ошибка при получении партнеров: {err}')
            return []

    def sum_cost_partners(self, partner_name):
        """
        Получение общей стоимости продаж партнера
        
        :param partner_name: Имя партнера
        :return: Сумма продаж или 0 при ошибке
        """
        try:
            query = f"""
                SELECT SUM(count_products)
                FROM partner_products_import
                WHERE partner_name_fk = '{partner_name}';
            """
            cursor = self.connection.cursor()
            cursor.execute(query)
            cost = cursor.fetchone()[0]
            cursor.close()
            
            return cost if cost else 0
        except Exception as error:
            print(f'Ошибка при получении стоимости продаж: {error}')
            return 0
