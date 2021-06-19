# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# # from PyQt5.QtCore import QDate,QTime
# from PyQt5.QtWidgets import *
#
# sys.path.append("../")  # 返回上层路径
# from APservice.test_jishi import Timer
# from APservice import service, test_jishi
# import pymysql
# import APdatabase.a2 as a2
# from APdatabase import planIN, planedit
#
# a2.init()


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate,QTime,QDateTime
from PyQt5.QtWidgets import *
from APservice import service
import pymysql
from APdatabase import plan


class show_MainWindow(QMainWindow):

    def __init__(self):
        super(show_MainWindow, self).__init__()

        self.setupUi(self)

    def setupUi(self, Ui_show):
        Ui_show.setObjectName("Ui_show")
        Ui_show.resize(800, 600)
        Ui_show.setStyleSheet("#Ui_show{border-image:url(image/1.jpg)}")
        self.centralwidget = QtWidgets.QWidget(Ui_show)
        self.centralwidget.setObjectName("centralwidget")

        self.plan_list = QtWidgets.QTableWidget(self.centralwidget)
        self.plan_list.setGeometry(QtCore.QRect(60, 20, 600, 350))
        self.plan_list.setObjectName("plan_list")
        self.plan_list.setColumnCount(3)
        self.plan_list.setRowCount(0)


        Ui_show.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_show)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        Ui_show.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_show)
        self.statusbar.setObjectName("statusbar")
        Ui_show.setStatusBar(self.statusbar)



        QtCore.QMetaObject.connectSlotsByName(Ui_show)
        self.query1()



    def query1(self):  # 待完善：显示全部、显示完成、显示未完成、选取日期等
        self.plan_list.setRowCount(0)  # 清空表格中的所有行
        # 调用服务类中的公共方法执行查询语句#设置计划的数据库
        result = service.query("select planID,date,kemu,neirong,shichang,zuotishichang,happyshichang,defen from tb_plan where wancheng_shifou =%s", 1)

        row = len(result)  # 取得记录个数，用于设置表格的行数

        self.plan_list.setRowCount(row)  # 设置表格行数
        self.plan_list.setColumnCount(8)  # 设置表格列数
        # if a2.setvalue（）      #设置只显示未完成的数据
        # 设置表格的标题名称
        self.plan_list.setHorizontalHeaderLabels(["ID", '日期', '科目', '内容', "计划时长","实际用时","玩耍时间","得分"])
        for i in range(row):  # 遍历行
            for j in range(self.plan_list.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格

                self.plan_list.setItem(i, j, data)  # 设置每个单元格的数据


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "击毙的小兔子"))
