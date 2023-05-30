from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from currency_converter import CurrencyConverter

c = CurrencyConverter()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        val1 = QLineEdit()
        val2 = QLineEdit()
        summ = QLineEdit()
        rest = QLineEdit()
        btn = QPushButton("Конвертировать")
        err = QLabel('')
        err.setStyleSheet('color: red')

        val1.setPlaceholderText('Валюта 1')
        val2.setPlaceholderText('Валюта 2')
        summ.setPlaceholderText('Сумма')
        rest.setPlaceholderText('Результат')

        summ.setValidator(QDoubleValidator())
        rest.setDisabled(True)

        def on_btn_click():
            cur1 = val1.text()
            cur2 = val2.text()
            num = summ.text()

            if len(cur1) == 0:
                err.setText('Введите валюту 1')
                return

            if len(cur2) == 0:
                err.setText('Введите валюту 2')
                return

            if len(num) == 0:
                err.setText('Введите сумму')
                return

            num = float(num)

            try:
                res = c.convert(num, cur1, cur2)
                rest.setText(str(res))
                err.setText('')
            except:
                err.setText('Ошибка конвертации')

        btn.clicked.connect(on_btn_click)

        layout.addWidget(QLabel("Конвертер"))
        layout.addWidget(val1)
        layout.addWidget(val2)
        layout.addWidget(summ)
        layout.addWidget(rest)
        layout.addWidget(err)
        layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("Конвертер")
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
