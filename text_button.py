
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
 
class RoundButton(QPushButton):
    def __init__(self, parent):
        super(RoundButton, self).__init__(parent)
        self.setFixedSize(40, 40)  # 设置按钮的固定大小
        self.setStyleSheet("QPushButton {"
                           "border-radius: 15px;"  # 设置圆角的半径
                           "background-color: rgb(53, 168, 82);"  # 设置按钮的背景颜色
                           "color: white;"  # 设置文字颜色
                           "}"
                           "QPushButton:hover {"
                           "background-color: rgb(38, 155, 85);"  # 鼠标悬浮时的背景颜色
                           "}"
                           "QPushButton:pressed {"
                           "background-color: rgb(3, 155, 85);"  # 鼠标按下时的背景颜色
                           "}")

class RoundButton_2(QPushButton):
    def __init__(self, parent):
        super(RoundButton_2, self).__init__(parent)
        self.setFixedSize(40, 40)  # 设置按钮的固定大小
        self.setStyleSheet("QPushButton {"
                           "border-radius: 15px;"  # 设置圆角的半径
                           "background-color: rgb(50, 100, 80);"  # 设置按钮的背景颜色
                           "color: white;"  # 设置文字颜色
                           "}"
                           "QPushButton:hover {"
                           "background-color: rgb(30, 150, 80);"  # 鼠标悬浮时的背景颜色
                           "}"
                           "QPushButton:pressed {"
                           "background-color: rgb(3, 150, 80);"  # 鼠标按下时的背景颜色
                           "}")
 



if __name__ == "__main__":
    class ExampleApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
 
        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Round Button Example')
            self.button = RoundButton(" ")
            self.button_2 = RoundButton_2(" ")
            # self.button.setGeometry(QtCore.QRect(100,30,20,20))

 
            layout = QVBoxLayout()
            layout.addWidget(self.button)
            layout.addWidget(self.button_2)
            self.setLayout(layout)
    app = QApplication([])
    mainWin = ExampleApp()
    mainWin.show()
    app.exec_()
 