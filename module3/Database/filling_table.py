import config
import psycopg
import pandas as pd

connection = psycopg.connect(
    host = config.HOST,
    user = config.USER,
    dbname = config.DBNAME,
    password = config.PASSWORD,
    port = config.PORT
)

def fill_product_type_import(connection):
    query = '''
        INSERT INTO product_type_import VALUES (%s, %s);
    '''
    df = pd.read_excel('C:/Users/igris/IdeaProjects/demolearnibg/Excel/Product_type_import.xlsx', engine = 'openpyxl')
    cursor = connection.cursor()

    for row in df.itertuples():
        type_product = row._1
        coef_type_product = row._2
        values = (type_product, coef_type_product)
        cursor.execute(query, values)

    connection.commit()
    cursor.close()

def fill_products_import(connection):
    query = '''
        INSERT INTO products_import VALUES (%s, %s, %s, %s);
    '''

    df = pd.read_excel("C:/Users/igris/IdeaProjects/demolearnibg/Excel/Products_import.xlsx", engine = "openpyxl")

    cursor = connection.cursor()

    for row in df.itertuples():
        type_product_fk = row._1
        product_name = row._2
        article = row.Артикул
        min_cost_partner = row._4
        values = (type_product_fk, product_name, article, min_cost_partner)
        cursor.execute(query, values)
    connection.commit()
    cursor.close()

def fill_material_type_import(connection):
    query = '''
        INSERT INTO material_type_import VALUES (%s, %s);
        '''
    df = pd.read_excel("C:/Users/igris/IdeaProjects/demolearnibg/Excel/Material_type_import.xlsx", engine="openpyxl")
    cursor = connection.cursor()
    for row in df.itertuples():
        type_material = row._1
        percent_broke = str(round(row._2 * 100, 2)) + '%'
        values = (type_material, percent_broke)
        cursor.execute(query, values)
    connection.commit()
    cursor.close()

def fill_partners_import(connection):
    query = '''
        INSERT INTO partners_import VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
    df = pd.read_excel("C:/Users/igris/IdeaProjects/demolearnibg/Excel/Partners_import.xlsx", engine="openpyxl")
    cursor = connection.cursor()
    for row in df.itertuples():
        type_partner = row._1
        partner_name = row._2
        director = row.Директор
        email_partner = row._4
        partner_phone = row._5
        ur_adres = row._6
        inn_partner = row.ИНН
        rate_partner= row.Рейтинг
        values = (type_partner, partner_name, director, email_partner, partner_phone, ur_adres, inn_partner, rate_partner)
        cursor.execute(query, values)
    connection.commit()
    cursor.close()

def fill_partner_products_import(connection):
    query = '''
		INSERT INTO partner_products_import VALUES (%s, %s, %s, %s);
	'''
    cursor = connection.cursor()
    df = pd.read_excel("C:/Users/igris/IdeaProjects/demolearnibg/Excel/Partner_products_import.xlsx", engine = "openpyxl")
    for row in df.itertuples():
        production_name_fk = row.Продукция
        partner_name_fk = row._2
        count_products = row._3
        date_prod = row._4

        values = (production_name_fk, partner_name_fk, count_products, date_prod)
        cursor.execute(query, values)
    connection.commit()
    cursor.close()


fill_products_import(connection)
fill_product_type_import(connection)
fill_material_type_import(connection)
fill_partners_import(connection)
fill_partner_products_import(connection)