"""
Модуль для обновления информации о партнере

Содержит класс UpdatePartnerInfo для редактирования данных существующего партнера
"""
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, 
    QLineEdit, QComboBox
)
from PySide6.QtCore import Qt
from partner_static_name import PartnerStaticName
from frames import partner_frame
from send_message_box import send_I_message, send_W_message, send_C_message
from check_input_data import start_check

class UpdatePartnerInfo(QWidget):
    """
    Класс для обновления информации о партнере
    
    Предоставляет интерфейс для редактирования данных существующего партнера
    """
    def __init__(self, controller):
        """
        Инициализация фрейма обновления информации о партнере
        
        :param controller: Основной контроллер приложения
        """
        super().__init__()
        self.controller = controller
        self.db = controller.db
        self.partner_name = PartnerStaticName.get_partner_name()
        self.partner_info = None
        self.layout = QVBoxLayout(self)
        
        # Получение информации о партнере
        self.get_partner_info()
        self.setup_ui()

    def get_partner_info(self):
        """
        Получение информации о партнере из БД
        """
        self.partner_info = self.db.take_partner_info(self.partner_name)
        
        if not self.partner_info:
            send_C_message(f"Партнер {self.partner_name} не найден")
            self.controller.switch_frame(partner_frame.PartnerFrame)

    def setup_ui(self):
        """
        Создание интерфейса фрейма обновления информации о партнере
        """
        # Проверка наличия данных о партнере
        if not self.partner_info:
            return
            
        # Заголовок
        title = QLabel(f'Редактирование партнера {self.partner_name}')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # Форма редактирования данных
        self.create_edit_form()
        
        # Кнопки управления
        self.create_buttons()

    def create_edit_form(self):
        """
        Создание формы редактирования данных партнера
        """
        # Тип партнера
        self.create_label("Тип партнера:")
        self.partner_type = QComboBox()
        self.partner_type.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        
        # Устанавливаем текущий тип партнера из базы данных
        current_type = self.partner_info['type_partner'].strip()
        index = self.partner_type.findText(current_type)
        if index >= 0:
            self.partner_type.setCurrentIndex(index)
            
        self.layout.addWidget(self.partner_type)
        
        # Наименование партнера
        self.create_label("Наименование партнера:")
        self.partner_name_edit = self.create_line_edit(self.partner_info['partner_name'], 100)
        
        # Директор
        self.create_label("Имя директора:")
        self.partner_direktor = self.create_line_edit(self.partner_info['director'], 250)
        
        # Электронная почта
        self.create_label("Адрес электронной почты:")
        self.partner_email = self.create_line_edit(self.partner_info['email_partner'], 100)
        
        # Телефон
        self.create_label("Номер телефона:")
        self.partner_phone = self.create_line_edit("+7" + self.partner_info['partner_phone'], 13)
        self.partner_phone.setInputMask('+7 000 000 00 00')
        
        # Юридический адрес
        self.create_label("Юридический адрес:")
        self.partner_address = self.create_line_edit(self.partner_info['ur_adres'], 350)
        
        # ИНН
        self.create_label("ИНН партнера:")
        self.partner_inn = self.create_line_edit(self.partner_info['inn_partner'], 10)
        
        # Рейтинг
        self.create_label("Рейтинг партнера (1-10):")
        self.partner_rate = self.create_line_edit(self.partner_info['rate_partner'], 2)

    def create_buttons(self):
        """
        Создание кнопок управления
        """
        # Кнопка обновления информации
        update_button = QPushButton("Обновить")
        update_button.clicked.connect(self.update_partner)
        self.layout.addWidget(update_button)
        
        # Кнопка возврата к списку партнеров
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.return_to_partner_frame)
        self.layout.addWidget(back_button)

    def create_label(self, text):
        """
        Создание метки с текстом
        
        :param text: Текст метки
        """
        label = QLabel(text)
        label.setObjectName("text_hint")
        self.layout.addWidget(label)

    def create_line_edit(self, text, max_length):
        """
        Создание поля ввода текста
        
        :param text: Текст по умолчанию
        :param max_length: Максимальная длина текста
        :return: Поле ввода текста
        """
        line_edit = QLineEdit()
        line_edit.setText(text)
        line_edit.setMaxLength(max_length)
        self.layout.addWidget(line_edit)
        return line_edit

    def update_partner(self):
        """
        Обновление информации о партнере в базе данных
        """
        # Сбор данных из формы
        partner_info = {
            "type_partner": self.partner_type.currentText(),
            "partner_name": self.partner_name_edit.text(),
            "director": self.partner_direktor.text(),
            "email_partner": self.partner_email.text(),
            "partner_phone": self.partner_phone.text()[3:],
            "ur_adres": self.partner_address.text(),
            "inn_partner": self.partner_inn.text(),
            "rate_partner": self.partner_rate.text()
        }
        
        # Проверка данных и обновление в БД
        if send_W_message("Проверьте введенные данные!") < 20000:
            if self.db.update_partner_info(self.partner_name, partner_info):
                send_I_message("Данные успешно обновлены!")
                self.return_to_partner_frame()
                return
                
        send_C_message("Данные не были обновлены!")

    def return_to_partner_frame(self):
        """
        Возврат к фрейму партнеров
        """
        self.controller.switch_frame(partner_frame.PartnerFrame)
