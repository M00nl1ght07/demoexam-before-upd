"""
Модуль для заполнения таблиц базы данных данными

Импортирует данные из Excel-файлов в созданную базу данных
"""
import config
import psycopg
import pandas as pd

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

def fill_product_type_import(connection):
    """
    Заполнение таблицы типов продукции данными из Excel-файла
    
    :param connection: Соединение с базой данных
    """
    try:
        query = "INSERT INTO product_type_import VALUES (%s, %s);"
        df = pd.read_excel('excel/Product_type_import.xlsx', engine='openpyxl')
        cursor = connection.cursor()

        for row in df.itertuples():
            values = (row._1, row._2)
            cursor.execute(query, values)

        connection.commit()
        cursor.close()
        print("Таблица product_type_import заполнена")
    except Exception as error:
        print(f"Ошибка при заполнении таблицы product_type_import: {error}")

def fill_products_import(connection):
    """
    Заполнение таблицы продукции данными из Excel-файла
    
    :param connection: Соединение с базой данных
    """
    try:
        query = "INSERT INTO products_import VALUES (%s, %s, %s, %s);"
        df = pd.read_excel("excel/Products_import.xlsx", engine="openpyxl")
        cursor = connection.cursor()

        for row in df.itertuples():
            values = (row._1, row._2, row.Артикул, row._4)
            cursor.execute(query, values)
            
        connection.commit()
        cursor.close()
        print("Таблица products_import заполнена")
    except Exception as error:
        print(f"Ошибка при заполнении таблицы products_import: {error}")

def fill_material_type_import(connection):
    """
    Заполнение таблицы типов материалов данными из Excel-файла
    
    :param connection: Соединение с базой данных
    """
    try:
        query = "INSERT INTO material_type_import VALUES (%s, %s);"
        df = pd.read_excel("excel/Material_type_import.xlsx", engine="openpyxl")
        cursor = connection.cursor()
        
        for row in df.itertuples():
            percent_broke = str(round(row._2 * 100, 2)) + '%'
            values = (row._1, percent_broke)
            cursor.execute(query, values)
            
        connection.commit()
        cursor.close()
        print("Таблица material_type_import заполнена")
    except Exception as error:
        print(f"Ошибка при заполнении таблицы material_type_import: {error}")

def fill_partners_import(connection):
    """
    Заполнение таблицы партнеров данными из Excel-файла
    
    :param connection: Соединение с базой данных
    """
    try:
        query = "INSERT INTO partners_import VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        df = pd.read_excel("excel/Partners_import.xlsx", engine="openpyxl")
        cursor = connection.cursor()
        
        for row in df.itertuples():
            values = (
                row._1, 
                row._2, 
                row.Директор, 
                row._4, 
                row._5, 
                row._6, 
                row.ИНН, 
                row.Рейтинг
            )
            cursor.execute(query, values)
            
        connection.commit()
        cursor.close()
        print("Таблица partners_import заполнена")
    except Exception as error:
        print(f"Ошибка при заполнении таблицы partners_import: {error}")

def fill_partner_products_import(connection):
    """
    Заполнение таблицы продукции партнеров данными из Excel-файла
    
    :param connection: Соединение с базой данных
    """
    try:
        query = "INSERT INTO partner_products_import VALUES (%s, %s, %s, %s);"
        df = pd.read_excel("excel/Partner_products_import.xlsx", engine="openpyxl")
        cursor = connection.cursor()
        
        for row in df.itertuples():
            values = (row.Продукция, row._2, row._3, row._4)
            cursor.execute(query, values)
            
        connection.commit()
        cursor.close()
        print("Таблица partner_products_import заполнена")
    except Exception as error:
        print(f"Ошибка при заполнении таблицы partner_products_import: {error}")

def main():
    """Основная функция для заполнения таблиц базы данных"""
    connection = connect_to_db()
    if connection:
        fill_product_type_import(connection)
        fill_products_import(connection)
        fill_material_type_import(connection)
        fill_partners_import(connection)
        fill_partner_products_import(connection)
        print("Все таблицы успешно заполнены")

main()