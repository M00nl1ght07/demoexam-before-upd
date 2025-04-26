from PySide6.QtWidgets import *
import partner_static_name
from Database import db
from send_message_box import *

class HistoryPartner(QWidget):
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
        title = QLabel(f'История продаж партнера {partner_static_name.PartnerStaticName.get_partner_name()}')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        table = QTreeWidget()
        table.setHeaderLabels(["Название продукта", "Имя партнера", "Количество", "Дата продажи"])
        self.layout.addWidget(table)

        for data in self.db.take_sales_info(partner_static_name.PartnerStaticName.get_partner_name()):
            item = QTreeWidgetItem(table)
            item.setText(0, data['production_name_fk'])
            item.setText(1, data['partner_name_fk'])
            item.setText(2, str(data['count_products']))
            item.setText(3, str(data['date_prod']))

        back_btn = QPushButton("Назад")
        from frames import partner_frame
        back_btn.clicked.connect(
            lambda: self.controller.switch_frame(partner_frame.PartnerFrame)
        )
        self.layout.addWidget(back_btn)