import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 800, 800)
        self.setWindowTitle("Эмулятор Аквариум")

        # Установка фона
        self.setStyleSheet("background-color: #e0f7fa;")  # Голубой цвет фона

        # Текст "Эмулятор Аквариум"
        self.title_label = QLabel("Эмулятор Аквариум", self)
        self.title_label.setGeometry(325, 20, 700, 20)
        self.title_label.setStyleSheet("color: black;")  # Черный цвет текста

        # Интерфейс с кнопками
        self.setupButtons()

        # Текущая метка
        self.current_label = None

    def setupButtons(self):
        # Первая кнопка "Накормить рыб"
        self.button1 = QPushButton(self)
        self.button1.setText("Накормить рыб")
        self.button1.setGeometry(150, 50, 200, 50)
        self.button1.setStyleSheet("background-color: #bdbdbd; color: black;")  # Серый цвет для кнопки и черный цвет текста
        self.button1.clicked.connect(self.showEatLabel)

        # Вторая кнопка "Почистить аквариум"
        self.button2 = QPushButton(self)
        self.button2.setText("Почистить аквариум")
        self.button2.setGeometry(370, 50, 200, 50)
        self.button2.setStyleSheet("background-color: #bdbdbd; color: black;")  # Серый цвет для кнопки и черный цвет текста
        self.button2.clicked.connect(self.showClearLabel)

        # Третья кнопка "Поменять воду"
        self.button3 = QPushButton(self)
        self.button3.setText("Поменять воду")
        self.button3.setGeometry(590, 50, 200, 50)
        self.button3.setStyleSheet("background-color: #bdbdbd; color: black;")  # Серый цвет для кнопки и черный цвет текста
        self.button3.clicked.connect(self.showWaterLabel)

        # Кнопка "Правила"
        self.rules_button = QPushButton(self)
        self.rules_button.setText("Правила")
        self.rules_button.setGeometry(35, 50, 100, 50)
        self.rules_button.setStyleSheet("background-color: #bdbdbd; color: black;")  # Серый цвет для кнопки и черный цвет текста
        self.rules_button.clicked.connect(self.showRules)

    def showEatLabel(self):
        self.hideCurrentLabel()
        new_label = QLabel("Накормить рыб", self)
        new_label.setGeometry(100, 150, 200, 50)
        new_label.setStyleSheet("color: black;")  # Черный цвет текста
        new_label.show()
        self.current_label = new_label

    def showClearLabel(self):
        self.hideCurrentLabel()
        new_label = QLabel("Почистить аквариум", self)
        new_label.setGeometry(100, 150, 200, 50)
        new_label.setStyleSheet("color: black;")  # Черный цвет текста
        new_label.show()
        self.current_label = new_label

    def showWaterLabel(self):
        self.hideCurrentLabel()
        new_label = QLabel("Поменять воду", self)
        new_label.setGeometry(100, 150, 200, 50)
        new_label.setStyleSheet("color: black;")  # Черный цвет текста
        new_label.show()
        self.current_label = new_label

    def showRules(self):
        self.hideCurrentLabel()
        rules_text = """Правило 1: Не перекармливайте рыб.
Правило 2: Регулярно чистите аквариум.
Правило 3: Поменяйте воду в аквариуме раз в неделю."""
        new_label = QLabel(rules_text, self)
        new_label.setGeometry(100, 150, 600, 50)
        new_label.setStyleSheet("color: black;")  # Черный цвет текста
        new_label.show()
        self.current_label = new_label

    def hideCurrentLabel(self):
        if self.current_label:
            self.current_label.hide()
            self.current_label.deleteLater()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

main()



















