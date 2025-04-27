"""
Модуль для создания таблиц в базе данных

Создает структуру базы данных для системы "Мастер пол"
с необходимыми таблицами и связями между ними.
"""
import config
import psycopg

def connect_to_db():
    """Подключение к базе данных из конфигурационного файла"""
    try:
        connection = psycopg.connect(
            host=config.HOST,
            user=config.USER,
            dbname=config.DBNAME,
            password=config.PASSWORD,
            port=config.PORT
        )
        print("Подключение к БД установлено")
        return connection
    except Exception as error:
        print(f"Ошибка подключения к БД: {error}")
        return None

def create_table(query, connection):
    """
    Выполняет SQL-запрос для создания таблиц
    
    :param query: SQL запрос для создания таблиц
    :param connection: Соединение с базой данных
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print("Таблицы успешно созданы")
    except Exception as error:
        print(f"Ошибка при создании таблиц: {error}")

# SQL-запросы на создание таблиц
SQL_CREATE_TABLES = '''
    create table product_type_import (
        type_product nchar(100) PRIMARY KEY,
        coef_type_product real NOT NULL
    );
    
    create table products_import (
        type_product_fk nchar(100) NOT NULL,
        foreign key (type_product_fk) references product_type_import(type_product) ON UPDATE CASCADE,
        product_name nchar(350) PRIMARY KEY not null,
        article nchar(7) NOT NULL,
        min_cost_partner reaL NOT NULL
    );
    
    create table material_type_import (
        type_material nchar(50) PRIMARY KEY NOT NULL,
        percent_broke nchar(5) NOT NULL
    );
    
    create table partners_import(
        type_partner nchar(3) NOT NULL,
        partner_name nchar(100) NOT NULL PRIMARY KEY,
        director nchar(250) NOT NULL,
        email_partner nchar(100) NOT NULL,
        partner_phone nchar(13) NOT NULL,
        ur_adres nchar(350) NOT NULL,
        inn_partner nchar(10) NOT NULL,
        rate_partner nchar(2) NOT NULL
    );
    
    create table partner_products_import(
        production_name_fk nchar(350) NOT NULL,
        foreign key (production_name_fk) references products_import(product_name) ON UPDATE CASCADE,
        partner_name_fk nchar(100) NOT NULL,
        foreign key (partner_name_fk) references partners_import(partner_name) ON UPDATE CASCADE,
        count_products INT NOT NULL,
        date_prod DATE NOT NULL,
        primary key (production_name_fk, partner_name_fk)
    );
'''

# Основная функция создания таблиц
def main():
    """Основная функция для создания таблиц в базе данных"""
    connection = connect_to_db()
    if connection:
        create_table(SQL_CREATE_TABLES, connection)

main()