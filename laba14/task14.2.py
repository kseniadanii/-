from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):

    def on_btn_click(self):

        self.count += 1
        count = self.count

        if count < 10:
            text = 'Закликай меня UwU'
        elif count < 20:
            text = 'Не останавливайся!'
        elif count < 30:
            text = 'Давай ещё!'
        elif count < 50:
            text = 'Да ты хорош!'
        elif count < 75:
            text = 'Вот это да!'
        elif count < 100:
            text = 'Я больше не могу!'
        else:
            text = 'Ты меня закликал!'
            self.widget_msg.setStyleSheet("""
            color: green;
            """)
            self.widget_btn.setDisabled(True)

        self.widget_count.setText(str(count))
        self.widget_msg.setText(text)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.count = 0

        self.widget_count = QLabel(str(self.count))
        self.widget_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_count.setStyleSheet("""
        font-size: 24pt;
        font-weight: 900;
        """)

        self.widget_msg = QLabel('Начинай!')
        self.widget_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget_btn = QPushButton('Клик')


        self.widget_btn.clicked.connect(self.on_btn_click)

        layout.addWidget(self.widget_count)
        layout.addWidget(self.widget_msg)
        layout.addWidget(self.widget_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("Кликер")
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()