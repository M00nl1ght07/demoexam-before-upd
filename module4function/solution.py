import psycopg


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

    # Проверить данные на соответствие
    try:
        product_coef = product_dict[product_id]
        material_percent = material_dict[material_id]

        if result_count < 1:
            return -1
        elif param_1 < 1:
            return -1
        elif param_2 < 1:
            return -1
    except Exception as err:
        print(err)
        return -1

    # Расчет количества материала на единицу продукции
    material_per_unit = param_1 * param_2 * product_coef
    
    # Расчет с учетом брака
    # Если брак 10% (0.1), нужно умножить на 1.1
    material_with_broke = material_per_unit * (1 + material_percent)
    
    # Общее количество материала
    final_count = material_with_broke * result_count

    print(final_count)
    return int(final_count)


def take_products(connection):
    """
    Метод получения продукции
    :return: Список со словарями
    """
    try:
        query = """
        select *
        from product_type_import"""

        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor.fetchall():
            product_dict[row[0].strip()] = row[1]

        return product_dict
    except Exception as error:
        print(error)
        return dict()


def take_materials(connection):
    """
    Метод получения продукции
    :return: Список со словарями
    """
    try:
        query = """
        select *
        from material_type_import"""

        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor.fetchall():
            material_dict[row[0].strip()] = float(row[1].strip()[:-1]) #0.1%

        return material_dict
    except Exception as error:
        print(error)
        return dict()


def main():
    connection = psycopg.connect(
        host='winserver001.asuscomm.com',
        user='admin',
        password='admin',
        dbname='demolearning',
        port=5432
    )

    # Получение идентификатора продукции
    # { ID:COEFFICIENT ,  ID2:COEFFICIENT2 }
    print(take_products(connection).items())
    for id, coefficient in take_products(connection).items():
        print(f"ID: {id}\tКоэффициент:\t {coefficient}")
    product_id_input = input("Название продукции: ")


    # Получение материалов
    for id, broke in take_materials(connection).items():
        print(f"ID: {id}\tБрак:\t {broke}")
    material_id_input = input("Название материала: ")

    try:
        res_count = int(input("Введите количество получаемой продукции: "))
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

    print(calc_method(product_id_input, material_id_input, res_count, param_1, param_2))
main()