from PySide6.QtWidgets import *
from partner_static_name import PartnerStaticName
from frames import partner_frame
from send_message_box import *

class AddPartnerInfo(QWidget):
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
        title = QLabel('Добавление партнера')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)


        # установка полей
        self.create_lable_pattern("Введите Тип партнера: ")
        self.partner_type = QComboBox()
        self.partner_type.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        self.layout.addWidget(self.partner_type)
        self.create_lable_pattern("Введите наименование партнера: ")
        self.partner_name = self.create_qlineedit_pattern("Строй - Построй", 100)
        self.create_lable_pattern("Введите имя директора: ")
        self.partner_direktor = self.create_qlineedit_pattern("Иванов Иван Иванович", 250)
        self.create_lable_pattern("Введите адрес электронной почты: ")
        self.partner_email = self.create_qlineedit_pattern("stroy@postroy.com", 100)
        self.create_lable_pattern("Введите номер телефона: ")
        self.partner_phone = self.create_qlineedit_pattern("+7 000 000 00 00", 13)
        self.partner_phone.setInputMask('+7 000 000 00 00')
        self.create_lable_pattern("Введите юридический адрес: ")
        self.partner_address = self.create_qlineedit_pattern("123456, Россия, Москва, ул. Пушкина, д. 39", 350)
        self.create_lable_pattern("Введите Рейтинг партнера (0-10): ")
        self.partner_rate = self.create_qlineedit_pattern("10", 2)
        self.create_lable_pattern("Введите ИНН партнера: ")
        self.partner_inn = self.create_qlineedit_pattern("3746388791", 10)

        self.update_buttom = QPushButton("Добавить")
        self.update_buttom.clicked.connect(self.update_partner_info)
        self.layout.addWidget(self.update_buttom)

        self.back_buttom = QPushButton("Назад")
        self.layout.addWidget(self.back_buttom)
        self.back_buttom.clicked.connect(lambda: self.controller.switch_frame(partner_frame.PartnerFrame))

    def create_lable_pattern(self, message):
        '''
        Функция создания лейблов для ввода
        :param message: текст подсказки
        :return: None
        '''
        text_hint = QLabel(message)
        text_hint.setObjectName("text_hint")
        self.layout.addWidget(text_hint)


    def create_qlineedit_pattern(self, hint_text, max_length):
        '''
        :param start_text: Текст в поле: Исчезающий текст
        :param max_length: максимальное кол-во символов
        :return: line_edit
        '''
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(hint_text)
        line_edit.setMaxLength(max_length)
        self.layout.addWidget(line_edit)

        return line_edit

    def update_partner_info(self):
        '''
        Функция обновления для редактирования данных
        :return: None
        '''
        partner_info = {
            "type_partner": self.partner_type.currentText(),
            "partner_name": self.partner_name.text(),
            "director": self.partner_direktor.text(),
            "email_partner": self.partner_email.text(),
            "partner_phone": self.partner_phone.text()[3:],
            "ur_adres": self.partner_address.text(),
            "inn_partner": self.partner_inn.text(),
            "rate_partner": self.partner_rate.text()
        }
        if send_W_message("Проверьте введенные данные!") < 20000:
            if self.db.add_partner_info(partner_info):
                send_I_message("Партнер успешно добавлен!")
                return
        else:
            send_C_message("Данные не были добавлены!")
            return
