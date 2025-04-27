"""
Модуль для отображения информации о партнерах

Содержит класс PartnerFrame для создания интерфейса списка партнеров
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QScrollArea, 
    QHBoxLayout, QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PartnerFrame(QWidget):
    """
    Класс для отображения списка партнеров
    
    Представляет информацию о всех партнерах в виде карточек
    """
    def __init__(self, controller):
        """
        Инициализация фрейма партнеров
        
        :param controller: Основной контроллер приложения
        """
        super().__init__()
        self.controller = controller
        self.db = controller.db
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        """
        Создание интерфейса фрейма партнеров
        """
        # Заголовок
        title = QLabel('Партнеры')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # Добавление логотипа
        self.add_pictures()

        # Область прокрутки для карточек партнеров
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.create_partner_card())
        self.layout.addWidget(scroll_area)

    def add_pictures(self):
        """
        Добавление логотипа компании
        """
        # Создание метки для изображения
        icon = QLabel()
        icon_pix = QPixmap('res/icon.png')  # Исправлен путь к логотипу
        icon.setScaledContents(True)
        icon.setFixedSize(100, 100)
        icon.setPixmap(icon_pix)

        # Размещение логотипа по центру
        layout_hv = QHBoxLayout()
        layout_hv.addStretch()
        layout_hv.addWidget(icon)
        layout_hv.addStretch()

        self.layout.addLayout(layout_hv)

    def calculate_discount(self, partner_name):
        """
        Расчет скидки партнера на основе объема продаж
        
        :param partner_name: Имя партнера
        :return: Процент скидки (0, 5, 10 или 15)
        """
        count = self.db.sum_cost_partners(partner_name)
        
        # Простая и понятная логика расчета скидок
        if count > 300000:
            return 15
        elif count > 50000:
            return 10
        elif count > 10000:
            return 5
        else:
            return 0

    def create_partner_card(self):
        """
        Создание карточек для всех партнеров
        
        :return: Виджет, содержащий все карточки партнеров
        """
        # Контейнер для всех карточек
        card_container = QWidget()
        cards_container_layout = QVBoxLayout(card_container)
        cards_container_layout.setSpacing(10)  # Добавлен отступ между карточками

        # Получение списка партнеров из БД
        partners = self.db.take_all_partners()
        
        if not partners:
            # Если партнеров нет, показываем сообщение
            no_partners = QLabel("Нет данных о партнерах")
            no_partners.setAlignment(Qt.AlignCenter)
            cards_container_layout.addWidget(no_partners)
            return card_container
            
        # Создание карточки для каждого партнера
        for partner_info in partners:
            card = self.create_single_partner_card(partner_info)
            cards_container_layout.addWidget(card)

        return card_container
        
    def create_single_partner_card(self, partner_info):
        """
        Создание карточки для одного партнера
        
        :param partner_info: Словарь с информацией о партнере
        :return: Виджет карточки партнера
        """
        # Создание карточки
        card = QWidget()
        card.setObjectName("partner_card")
        card_layout = QVBoxLayout(card)
        
        # Верхняя часть с названием и скидкой
        header_layout = QHBoxLayout()
        
        # Название партнера
        type_and_name = QLabel(f'{partner_info["type_partner"]} | {partner_info["partner_name"]}')
        type_and_name.setObjectName("qlabel-card-main")
        
        # Скидка партнера
        discount = QLabel(f'{self.calculate_discount(partner_info["partner_name"])}%')
        discount.setObjectName("qlabel-card-right")
        
        header_layout.addWidget(type_and_name)
        header_layout.addWidget(discount)
        card_layout.addLayout(header_layout)
        
        # Информация о партнере
        director = QLabel(f'Директор: {partner_info["director"]}')
        director.setObjectName("qlabel-card")
        
        phone = QLabel(f'Телефон: +7 {partner_info["partner_phone"]}')
        phone.setObjectName("qlabel-card")
        
        rating = QLabel(f'Рейтинг: {partner_info["rate_partner"]}')
        rating.setObjectName("qlabel-card")
        
        # Добавление информации на карточку
        card_layout.addWidget(director)
        card_layout.addWidget(phone)
        card_layout.addWidget(rating)
        
        return card