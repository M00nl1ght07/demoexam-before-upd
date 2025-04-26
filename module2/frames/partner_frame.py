from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap


class PartnerFrame(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db

        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        '''
        Функция создание интерфейса фрейма
        :return: None
        '''
        title = QLabel('Партнеры')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # добавление картинки
        self.add_pictures()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(self.create_partner_card())

        self.layout.addWidget(scroll_area)

    def add_pictures(self):
        '''
        Функция добаавления картинки
        :return: None
        '''
        icon = QLabel()
        icon_pix = QPixmap('C:/Users/igris/IdeaProjects/demolearnibg/icon/icon.png')
        icon.setScaledContents(True)
        icon.setFixedSize(100, 100)
        icon.setPixmap(icon_pix)

        layout_hv = QHBoxLayout()
        layout_hv.addWidget(QLabel())
        layout_hv.addWidget(icon)
        layout_hv.addWidget(QLabel())

        self.layout.addLayout(layout_hv)

    def calculate_discount(self, partner_name):
        '''
        Функция для расчета скидки партнера
        :param partner_name: имя партнера
        :return: discount
        '''
        count = self.db.sum_cost_partners(partner_name)
        if count > 300000:
            return 15
        elif count > 50000:
            return 10
        elif count > 10000:
            return 5
        else:
            return 0

    def create_partner_card(self):
        '''
        Функция создания карточки партнера
        :return: None
        '''
        # контейнер
        card_container = QWidget()
        # разметка для контейнера карточек
        cards_container_layout = QVBoxLayout(card_container)

        for partner_info in self.db.take_all_partners():
            card = QWidget()
            card.setObjectName("partner_card")

            card_layout = QVBoxLayout()
            card.setLayout(card_layout)

            card_horizontal = QHBoxLayout()
            type_partner = QLabel(f'{partner_info["type_partner"]} | {partner_info["partner_name"]}')
            type_partner.setObjectName("qlabel-card-main")

            discount_partner = QLabel(f'{self.calculate_discount(partner_info["partner_name"])}%')
            discount_partner.setObjectName("qlabel-card-right")

            card_horizontal.addWidget(type_partner)
            card_horizontal.addWidget(discount_partner)

            card_layout.addLayout(card_horizontal)

            director = QLabel(f'Директор: {partner_info["director"]}')
            director.setObjectName("qlabel-card")

            partner_phone = QLabel(f'Телефон: +7 {partner_info["partner_phone"]}')
            partner_phone.setObjectName("qlabel-card")

            rate_partner = QLabel(f'Рейтинг: {partner_info["rate_partner"]}')
            rate_partner.setObjectName("qlabel-card")

            card_layout.addWidget(director)
            card_layout.addWidget(partner_phone)
            card_layout.addWidget(rate_partner)

            cards_container_layout.addWidget(card)

        return card_container