from PySide6.QtWidgets import (
    QMessageBox
)

def send_I_message(message_text: str):
    '''
    Функция создания и демонстрации Информационного сообщения
    :param message_text: Текст сообщения
    :return: UID кнопки, которую нажали
    '''
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Information)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    user_result = message.exec()
    return user_result


def send_W_message(message_text: str):
    '''
    Функция создания и демонстрации Предупреждающего сообщения
    :param message_text: Текст сообщения
    :return: UID кнопки, которую нажали
    '''
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Warning)
    message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    user_result = message.exec()
    return user_result


def send_C_message(message_text: str):
    '''
    Функция создания и демонстрации Запрещающего сообщения
    :param message_text: Текст сообщения
    :return: UID кнопки, которую нажали
    '''
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Critical)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    user_result = message.exec()
    return user_result