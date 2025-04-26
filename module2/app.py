from PySide6.QtWidgets import *
import sys
from Database import db
from frames import partner_frame

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
    '''

app = QApplication(sys.argv)
main_class = MainApplication()
app.setStyleSheet(style)
app.setFont('Segoe UI')
main_class.show()
app.exec()

