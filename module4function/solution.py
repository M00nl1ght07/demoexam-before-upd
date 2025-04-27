import psycopg
import math  # Для округления вверх

product_dict = dict()
material_dict = dict()

def calc_method(product_id, material_id, result_count: int, param_1: float, param_2: float) -> int:
    """
    Метод расчета количества материала для производства продукции
    :param product_id: Идентификатор продукции
    :param material_id: идентификатор материала
    :param result_count: Количество продукции
    :param param_1: Параметр 1
    :param param_2: Параметр 2
    :return: INT количество материала
    """
    # Проверка входных данных
    try:
        product_coef = product_dict[product_id]
        material_percent = material_dict[material_id]

        if result_count < 1 or param_1 <= 0 or param_2 <= 0:
            return -1
    except Exception as err:
        print(f"Ошибка проверки данных: {err}")
        return -1

    # Расчет количества материала на единицу продукции
    material_per_unit = param_1 * param_2 * product_coef

    # Расчет с учетом процента брака материала
    material_with_broke = material_per_unit * (1 + material_percent)

    # Общее количество материала
    final_count = material_with_broke * result_count

    # Округление вверх
    return math.ceil(final_count)


def take_products(connection):
    """
    Метод получения продукции
    :return: Словарь продукции
    """
    try:
        query = """
        SELECT * FROM product_type_import
        """

        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor.fetchall():
            product_dict[row[0].strip()] = float(row[1])

        return product_dict
    except Exception as error:
        print(f"Ошибка получения продукции: {error}")
        return dict()


def take_materials(connection):
    """
    Метод получения материалов
    :return: Словарь материалов
    """
    try:
        query = """
        SELECT * FROM material_type_import
        """

        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor.fetchall():
            # Исправление: убираем % и делим на 100 для получения коэффициента
            material_dict[row[0].strip()] = float(row[1].strip()[:-1]) / 100

        return material_dict
    except Exception as error:
        print(f"Ошибка получения материалов: {error}")
        return dict()


def main():
    try:
        connection = psycopg.connect(
            host='winserver001.asuscomm.com',
            user='admin',
            password='admin',
            dbname='demolearning',
            port=5432
        )

        # Получение данных
        products = take_products(connection)
        print("\nСписок продукции:")
        for id, coefficient in products.items():
            print(f"ID: {id}\tКоэффициент: {coefficient}")

        product_id_input = input("\nВведите идентификатор продукции: ").strip()

        materials = take_materials(connection)
        print("\nСписок материалов:")
        for id, broke in materials.items():
            print(f"ID: {id}\tПроцент брака: {broke * 100}%")

        material_id_input = input("\nВведите идентификатор материала: ").strip()

        try:
            res_count = int(input("\nВведите количество получаемой продукции: "))
        except Exception:
            res_count = -1

        try:
            param_1 = float(input("Введите параметр 1: "))
        except Exception:
            param_1 = -1

        try:
            param_2 = float(input("Введите параметр 2: "))
        except Exception:
            param_2 = -1

        result = calc_method(product_id_input, material_id_input, res_count, param_1, param_2)
        print(f"\nНеобходимое количество материала: {result}")

    except Exception as connection_error:
        print(f"Ошибка подключения к БД: {connection_error}")
    finally:
        try:
            connection.close()
        except:
            pass

main()