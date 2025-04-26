from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from frames import history_partner
from partner_static_name import PartnerStaticName

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

        create_partner_btn = QPushButton("Добавить партнера")
        from frames.add_partner_info import AddPartnerInfo
        create_partner_btn.clicked.connect(lambda: self.controller.switch_frame(AddPartnerInfo))

        self.layout.addWidget(scroll_area)
        self.layout.addWidget(create_partner_btn)

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
        if count is None or count == 0:  # Добавляем проверку на None и 0
            return 0
        
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

            open_update_frame = QPushButton('Редактировать')
            open_update_frame.setObjectName(f'{partner_info["partner_name"]}')
            open_update_frame.clicked.connect(self.open_frame_update)

            open_history_frame = QPushButton('История партнера')
            open_history_frame.setObjectName(f'{partner_info["partner_name"]}')
            open_history_frame.clicked.connect(lambda checked, name=partner_info["partner_name"]: self.open_history_frame(name))
            open_history_frame.setObjectName("button-card")

            card_layout.addWidget(director)
            card_layout.addWidget(partner_phone)
            card_layout.addWidget(rate_partner)
            card_layout.addWidget(open_update_frame)
            card_layout.addWidget(open_history_frame)

            cards_container_layout.addWidget(card)

        return card_container

    def open_frame_update(self):
        '''
        Функция открытия фрейма по обработчику на кнопку
        :return: None
        '''
        sender = self.sender()
        print(sender.objectName())
        sender_name = sender.objectName()
        from frames.update_partner_info import UpdatePartnerInfo
        self.controller.switch_frame(UpdatePartnerInfo, sender_name)

    def open_history_frame(self, partner_name):
        '''
        Функция открытия фрейма истории партнера
        :param partner_name: имя партнера
        :return: None
        '''
        from frames import history_partner
        PartnerStaticName.set_partner_name(partner_name)
        self.controller.switch_frame(history_partner.HistoryPartner)
