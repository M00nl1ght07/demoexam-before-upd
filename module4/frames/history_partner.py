"""
Модуль для отображения истории продаж партнера

Содержит класс HistoryPartner для просмотра истории продаж выбранного партнера
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, 
    QTreeWidget, QTreeWidgetItem
)
from PySide6.QtCore import Qt
import partner_static_name
from Database import db

class HistoryPartner(QWidget):
    """
    Класс для отображения истории продаж партнера
    
    Отображает таблицу с историей продаж конкретного партнера
    """
    def __init__(self, controller):
        """
        Инициализация фрейма истории продаж
        
        :param controller: Основной контроллер приложения
        """
        super().__init__()
        self.controller = controller
        self.db = controller.db
        self.partner_name = partner_static_name.PartnerStaticName.get_partner_name()
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        """
        Создание интерфейса фрейма истории продаж
        """
        # Заголовок с именем партнера
        title = QLabel(f'История продаж партнера {self.partner_name}')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # Создание таблицы продаж
        sales_table = self.create_sales_table()
        self.layout.addWidget(sales_table)

        # Кнопка возврата
        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(self.return_to_partner_frame)
        self.layout.addWidget(back_btn)

    def create_sales_table(self):
        """
        Создание и заполнение таблицы с историей продаж
        
        :return: Виджет таблицы с историей продаж
        """
        # Создание таблицы с колонками
        table = QTreeWidget()
        table.setHeaderLabels(["Название продукта", "Имя партнера", "Количество", "Дата продажи"])
        
        # Получение данных о продажах из БД
        sales_data = self.db.take_sales_info(self.partner_name)
        
        # Проверка наличия данных
        if not sales_data:
            # Если данных нет, добавляем сообщение
            no_data_item = QTreeWidgetItem(table)
            no_data_item.setText(0, "Нет данных о продажах")
            return table
            
        # Заполнение таблицы данными
        for data in sales_data:
            item = QTreeWidgetItem(table)
            item.setText(0, data['production_name_fk'])
            item.setText(1, data['partner_name_fk'])
            item.setText(2, str(data['count_products']))
            item.setText(3, str(data['date_prod']))
            
        return table
        
    def return_to_partner_frame(self):
        """
        Возврат к фрейму партнеров
        """
        from frames import partner_frame
        self.controller.switch_frame(partner_frame.PartnerFrame)