import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPen, QPainter, QBrush, 
                         QLinearGradient, QConicalGradient, QRadialGradient)
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QFrame, QSizePolicy,QPushButton,QVBoxLayout)


 
class RoundButton(QPushButton):
    def __init__(self, parent):
        super(RoundButton, self).__init__(parent)
        self.setFixedSize(20, 20)  # 设置按钮的固定大小
        self.setStyleSheet("QPushButton {"
                           "border-radius: 10px;"  # 设置圆角的半径
                           "background-color: rgb(254, 183, 30);"  # 设置按钮的背景颜色
                           "color: white;"  # 设置文字颜色
                           "}"
                           "QPushButton:hover {"
                           "background-color: rgb(254, 214, 129);"  # 鼠标悬浮时的背景颜色
                           "}"
                           "QPushButton:pressed {"
                           "background-color: rgb(254, 183, 30);"  # 鼠标按下时的背景颜色
                           "}"
                           )
    
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setFixedSize(25,25)
        return super().mousePressEvent(e)
    
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setFixedSize(20,20)
        return super().mouseReleaseEvent(e)

if __name__ == "__main__":
    class ExampleApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()
 
        def initUI(self):
            self.setGeometry(300, 300, 250, 150)
            self.setWindowTitle('Round Button Example')
            self.button = RoundButton("")
 
            layout = QVBoxLayout()
            layout.addWidget(self.button)
            self.setLayout(layout)
    app = QApplication([])
    mainWin = ExampleApp()
    mainWin.show()
    app.exec_()