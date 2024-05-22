import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
 
class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        self.initUI()
 
    def initUI(self):
        button = QPushButton('按钮', self)
        button.setStyleSheet("background-color: rgb(255, 0, 0);")  # 设置按钮背景为红色
        button.resize(100, 30)
        button.move(50, 50)
 
        self.setGeometry(100, 100, 200, 100)
        self.show()
 
def main():
    app = QApplication(sys.argv)
    mainWin = TransparentWindow()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()