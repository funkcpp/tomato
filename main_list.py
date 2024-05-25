# 2024/4/18 开发日志：修复了tableWight单元格选择的问题，修改tab名称,增加拖拽窗口功能
# 2024/4/19 开发日志: 新建标题栏（frame_title）
# 2024/4/20 开发日志: 删除lcd number边框 添加frame_title按键的动画 修改应用基础文字 修改tablewight bar
#                    隐藏了tablewight的边框
# 2024/4/24 开发日志：修复了点击tableWight空白处闪退的bug 
# 过了好久一直没开发
# 2024/5/4 开发日志：
# 2024/5/7 储存变量
# 2024/5/24  初始化 tableview 
# 2024/5/25 新增完成待办功能以及删除待办功能
import sys
import datetime,time
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import (QMainWindow,QApplication,QWidget,QListWidgetItem,QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout,QAbstractItemView
                             ,QFrame)
from Ui_windows_list import Ui_MainWindow
from PyQt5.QtCore import Qt,QDateTime,QDate,QTime,QTimer
from PyQt5.QtGui import QPalette, QBrush, QColor,QFontDatabase,QFont
from Ui_add_text import Ui_Add_text
import text_button
import frame_title
import subprocess
import save_text

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent) # super(MyMainWindow,self) 明确了调用的父类是 MyMainWindow 因为 MyMainWindow 继承了
                                                  # QMainWindow 和 Ui_MainWindow 
                                                  # 通俗的理解是super().__init__(parent) 是调用了父类的所有信息
                                                  # __init__() parent 加不加没有什么关系
                                                  # super(MyMainWindow,self) 这种 super(本类名,self)是python 2 的写法，python 3可以直接写
                                                  # 为 super().__init__()
        

        self.setupUi(self)

        self.move(1450,15) # 设置窗体初始位置
        self.transparent = 0.8
        self.index = 0 # 文本编号
        # 算了懒得改了，直接全部透明吧
        self.setWindowOpacity(self.transparent)
        self.q = True
        # 存储list的路径
        self.path = "F:\\tomato\\text_add.txt"
        # 更改字体
        font_id = QFontDatabase.addApplicationFont('F:\\tomato\\res\\mo導taiwanゴシック.ttf')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.setFont(QFont(font_family))
        
        # 取消边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 隐藏登录框以外的白色界面和边框以及标题栏
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 窗口置顶
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # 窗口固定大小
        self.setFixedWidth(460)
        self.setFixedHeight(650)

        self.setStyleSheet('background-color: white;')

        # 修改两个tab的名称
        self.tabWidget.setTabText(0,"Homepage")
        self.tabWidget.setTabText(1,"Setting")
        self.tableWidget.setWindowOpacity(self.transparent)
        self.setAutoFillBackground(True)


        # 添加frame_title
        self.frame_title = frame_title.Frame_title(self.centralwidget)
        self.frame_title.setGeometry(QtCore.QRect(0, 0, 460,100))
        self.frame_title.window_close_button.clicked.connect(self.close)
        self.frame_title.window_small_button.clicked.connect(self.small)
        
        # 调整前后顺序
        self.frame_title.raise_()
        self.tabWidget.raise_()
        
#-------------------------------------------------------------------------------------------------
        # lcdNumber 打印当前时间
        # 改变lcdNumber的显示位数，使其显示位数为8位
        self.lcdNumber.setDigitCount(8)
        
        # 利用Qtimer来打印动画
        self.time = QTimer(self)
        self.time.timeout.connect(self.get_local_time)
        self.time.start(1000)

        # 取消lcd number边框
        self.lcdNumber.setFrameStyle(QFrame.NoFrame)
#-----------------------------------------------------------------------------------------------
        

#-----------------------------------------------------------------------------------------
        # 建立文本输入框旁边的按钮
        self.text_pushbutton = text_button.RoundButton(self.tab)
        self.text_pushbutton.setGeometry(QtCore.QRect(345,490,30,30))
        self.text_pushbutton.clicked.connect(self.addtext)
        
        self.text_save_pushbutton = text_button.RoundButton_2(self.tab)
        self.text_save_pushbutton.setGeometry(QtCore.QRect(400,490,30,30))
        self.text_save_pushbutton.clicked.connect(self.save_add_text)
#-----------------------------------------------------------------------------------------
        
        # tableweight 属性调整

        # tableweight 的默认值
        self.col_= 3 # tablewidget初始列
        self.row_ = 10 # tablewidget 初始行
        self.init_size = 10 #文本一开始展示时的固定文字大小
        self.change_size = 14 #文本高亮后改变的文字大小

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setColumnCount(self.col_)
        self.tableWidget.setRowCount(self.row_)
        # 生成列：
        for i in range(self.col_):
            self.tableWidget.setHorizontalHeaderItem(i, item)
        # 生成行
        for i in range(self.row_):
            self.tableWidget.setVerticalHeaderItem(i, item)
        # 初始化
        for i in range(self.col_):
            for j in range(self.row_):
                self.tableWidget.setItem(j,i,QTableWidgetItem(""))
        
        # 对tableweight做出限制
        # 1.限制用户直接在tableweight上直接编译
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 2.禁用选择行为
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
 
        # 3.设置选择模式为不选择
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        # 4.取消黑色选择边框
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        

        # 增加tableWidget添加文本判断事件
        self.text_add_flag = [False for _ in range(self.row_)]
        # 增加点击事件
        self.text_show_flag = [False for _ in range(self.row_)]# 为了实现单击以后改变字体颜色功能
        # 增加事件是否完成判断
        self.text_done_flag = [False for _ in range(self.row_)]
        
        # 添加的文本
        self.text_add = []

        self.tableWidget.setStyleSheet("border: 0px;")
        # self.tableWidget.setStyleSheet("background-color:rgb(60,60,60);")
        self.tableWidget.setWindowOpacity(0.7)  # 设置整个控件的不透明度为50%)  # 设置整个控件的不透明度为50%
        self.tableWidget.setFont(QFont(font_family)) # 添加stylesheet样式后需要重新指定字体样式

        # 点击事件，使得待办更加醒目
        
        self.tableWidget.cellClicked.connect(self.click_cell)
        # self.tableWidget.cellClicked.connect(self.delete_text)
        
        # tablewidget初始化
        self.tableWidget_init()

        # 设置所有列都是自动列宽
        self.tableWidget.resizeColumnsToContents()
        #隐藏行列线
        self.tableWidget.setShowGrid(False)
        # 隐藏表头
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头线
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头线
        
        self.m_flag = False # 避免移动窗口和frame_title按钮产生冲突
 #-------------------------------------------------------------------------------------------------

    # 获取当前系统时间
    def get_local_time(self):
        local_time = datetime.time(hour=time.localtime()[3],minute=time.localtime()[4],second=time.localtime()[5])
        self.lcdNumber.display(str(local_time))
    
    # 无边框拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos() # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))# 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    
    def small(self):
        self.showMinimized()

    # 点击后更改cell中的文本字体大小
    def change_text_size(self,item,nums):
        font = item.font()
        font.setPointSize(nums) 
        item.setFont(font)

    # 点击cell触发的事件，包括高亮，完成代办以及删除代办
    def click_cell(self,row,col):
        item = self.tableWidget.item(row,col)
        if col == 1 and not(self.text_done_flag[row]):
            # 点击文本显示高亮
            self.show_text(row,col)
        
        if col == 0 and self.text_add_flag[row]:
            # 点击文本完成待办
            self.done_text(row,col)
        
        if self.text_add_flag[row] and col == 2:
            # 点击删除
            self.delete_text(row,col)
    
    # 显示文本高亮
    def show_text(self,row,col):
        item = self.tableWidget.item(row,col)
        if item and QtCore.Qt.RightButton and not (self.text_show_flag[row]):
            self.text_show_flag[row] = True
            item.setForeground(QColor(250,0,0))
            
            self.change_text_size(item,self.change_size)
            
            self.tableWidget.resizeColumnsToContents()
        else:
            if QtCore.Qt.RightButton and self.text_show_flag[row] :
                self.text_show_flag[row] = False
                item.setForeground(QColor(Qt.black))
                
                self.change_text_size(item,self.init_size)

                self.tableWidget.resizeColumnsToContents()


    # 删除文本
    def clear(self,row,col):
        for i in range(col):
            self.tableWidget.setItem(row,i,QTableWidgetItem(""))
    
    def delete_text(self,row,col):
        self.clear(row,col+1)
        self.text_add_flag[row] = False
        print(self.text_add_flag)
        print(1)
    
# 完成代办事件
    def done_text(self,row,col):
        
        item = self.tableWidget.item(row,1)
        item_2 = self.tableWidget.item(row,0)
        flag = self.text_done_flag[row]
        if item_2 and item and not(flag) and QtCore.Qt.LeftButton:
            self.text_done_flag[row] = True
            item.setForeground(QColor(212,212,212))
            
            self.change_text_size(item,self.init_size)

            item_2.setText("Y")
            item_2.setForeground(QColor(125,125,255))

            
            self.tableWidget.resizeColumnsToContents()
        else:
            if item and flag and QtCore.Qt.LeftButton:
                self.text_done_flag[row] = False
                item.setForeground(QColor(Qt.black))
                self.change_text_size(item,self.init_size)
                
                item_2.setText("N")
                item_2.setForeground(QColor(212,212,212))
                
                self.tableWidget.resizeColumnsToContents()
            

        print(item)


# 添加文本功能实现
    def addtext(self):
        col = 1
        text = self.textEdit.toPlainText()
        for i in range(len(self.text_add_flag)):
            if not(self.text_add_flag[i]):
                item = QTableWidgetItem(text)
                
                item_2 = QTableWidgetItem("N")
                item_2.setForeground(QColor(212,212,212))
                
                item_3 = QTableWidgetItem("C")
                item_3.setForeground(QColor(0,106,106))
                
                self.change_text_size(item,self.init_size)
                self.change_text_size(item_2,self.init_size)
                self.change_text_size(item_3,self.init_size)


                self.tableWidget.setItem(i,1,item)
                self.tableWidget.setItem(i,0,item_2)
                self.tableWidget.setItem(i,2,item_3)

                self.text_add_flag[i] = True
                self.tableWidget.resizeColumnsToContents()
                break
        self.textEdit.clear()
        print(self.text_add_flag)
    
# 提交并保存文本
    def save_add_text(self):
        text = self.textEdit.toPlainText()
        if text != "":
            save_text.save_add_text(self.path,text,str(self.index))
            self.index += 1
    
 # 初始化tableWidget
    def tableWidget_init(self):
        with open(self.path,"r") as file:
            
            data = file.readlines()
            file.close()
        # index 的初始化
        if data == []:
            self.index = 0
        else:
            index = 0
            for i in range(len(data[-1])):
                if data[-1][i] == "\t":
                    break
            index = int(data[-1][0:i]) + 1
            self.index = index
        if len(data) >= 10:
            data = data[-10:]
        
        # 初始化添加事件
        # data 中的数据结构是 index + text +  str(year) + str(mon)  + str(day) +  "T" + "\n"
        col = 1
        for row in range(0,len(data)):
            infor = data[row].split("\t")
            text = infor[1]
            self.text_add_flag[row] = True
            item = QTableWidgetItem(text)
            
            item_2 = QTableWidgetItem("N")
            item_2.setForeground(QColor(212,212,212))

            item_3 = QTableWidgetItem("C")
            item_3.setForeground(QColor(0,106,106))
            
            self.change_text_size(item,self.init_size)
            self.change_text_size(item_2,self.init_size)
            self.change_text_size(item_3,self.init_size)
            
            self.tableWidget.setItem(row,col,item)
            self.tableWidget.setItem(row,0,item_2)
            self.tableWidget.setItem(row,2,item_3)
            

        # print(self.index)
        # print(data)
        # print(1)

        

# 多窗口调用
class text_add_window (QMainWindow,Ui_Add_text):
    def __init__(self, parent=None) -> None:
        super(text_add_window,self).__init__(parent)

        self.setupUi(self)

    def open(self):
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    textWin = text_add_window()
    # 改变窗口的起始位置
    # myWin.move(1400,0)
    myWin.show()
    
    # 连接窗口
    # myWin.Add.clicked.connect(textWin.open)

    sys.exit(app.exec_())  