import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout,QFrame,QMainWindow,QHBoxLayout
from PyQt5.QtCore import Qt

import text_button
import small_button
class Frame_title(QFrame):
    def __init__(self,parent) -> None:
        super(Frame_title,self).__init__(parent)
        # self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 15, 120, 20))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # # 设置frame背景色
        self.setStyleSheet("QFrame{"
                           "background-color:rgb(60,60,60);"
                           "}")
        self.window_small_button = small_button.RoundButton(self)
        self.window_small_button.setText("")
        self.window_small_button.setObjectName("window_small_button")
        self.window_small_button.setGeometry(QtCore.QRect(370,10,30,30))

        self.window_close_button = small_button.RoundButton(self)
        self.window_close_button.setStyleSheet("QPushButton {"
                           "border-radius: 10px;"  # 设置圆角的半径
                           "background-color: rgb(253, 89, 77);"  # 设置按钮的背景颜色
                           "color: white;"  # 设置文字颜色
                           "}"
                           "QPushButton:hover {"
                           "background-color: rgb(254, 171, 165);"  # 鼠标悬浮时的背景颜色
                           "}"
                           "QPushButton:pressed {"
                           "background-color: rgb(253, 89, 77);"  # 鼠标按下时的背景颜色
                           "}"
                           )
        self.window_close_button.setText("")
        self.window_close_button.setObjectName("window_close_button")
        self.window_close_button.setGeometry(QtCore.QRect(415,10,30,30))
        # 设置布局
        
        # self.horizontalLayout.addWidget(self.window_small_button)
        # self.horizontalLayout.addWidget(self.window_close_button)
 
        # 设置布局
        # self.setLayout(self.horizontalLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
 
# 创建一个窗口
    window = QWidget()
    
    # 创建
    centralwidget = QtWidgets.QWidget(window)
    centralwidget.setGeometry(QtCore.QRect(0, 0, 1000,500))
    centralwidget.setStyleSheet('background-color: #FFA07A;')
# 创建自定义的Frame实例
    custom_frame = Frame_title(centralwidget)
    custom_frame.setGeometry(QtCore.QRect(0, 0, 460,100))
    # custom_frame.setStyleSheet("background-color:rgb(60,60,60);")
# 将自定义的Frame添加到窗口布局中
 
# 显示窗口
    window.show()
 
# 运行应用
    sys.exit(app.exec_())