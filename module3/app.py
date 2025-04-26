from PySide6.QtWidgets import *
import sys
from Database import db
from frames import partner_frame
from partner_static_name import PartnerStaticName

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Мастер пол')
        self.resize(1200, 720)

        # вызов класса Database
        self.db = db.Database()

        # контейнер для фреймов
        self.frames_container = QStackedWidget()

        frame_start = partner_frame.PartnerFrame(self)
        self.frames_container.addWidget(frame_start)

        # создание разметки
        layout = QVBoxLayout(self)
        layout.addWidget(self.frames_container)

    def switch_frame(self, frame_new, partner_name = None):
        '''
        Функция переключения между фреймами
        :param frame_new: новый фрейм куда переходим
        :param partner_name: имя партнера
        :return: None
        '''
        # если не пустой добавляем имя в статический класс
        if partner_name != None:
            PartnerStaticName.set_partner_name(partner_name)

        new_frame = frame_new(controller = self)
        self.frames_container.removeWidget(new_frame)
        self.frames_container.addWidget(new_frame)
        self.frames_container.setCurrentWidget(new_frame)



style = '''
    #title_frame {
        font-size: 26px;
        font-weight: bold;
        qproperty-alignment: AlignCenter;
    }
    #qlabel-card-right{
        font-size: 26px;
        qproperty-alignment: AlignRight;
        padding-right: 20px;
        }
    #qlabel-card-main {
        font-size: 20px;
        padding-left: 20px;
    }
    #qlabel-card{
        font-size: 18px;
        padding-left: 20px;
    }
    #partner_card {
        background-color: #F4E8D3;
        border: 2px solid gray;
    }
    QPushButton {
        background-color: #67BA80;
        color: #FFFFFF;
        font-size: 18px;
        margin-right: 20px;
        margin-left: 20px;
    }
    #text_hint {
        font-size: 18px;
        padding-left: 20px;
    }
    QLineEdit {
        margin-left: 20px;
        margin-right: 20px;
        padding-left: 10px;
    }
    QComboBox {
        margin-left: 20px;
        margin-right: 20px;
        padding-left: 10px
        }
    '''

app = QApplication(sys.argv)
main_class = MainApplication()
app.setStyleSheet(style)
app.setFont('Segoe UI')
main_class.show()
app.exec()

