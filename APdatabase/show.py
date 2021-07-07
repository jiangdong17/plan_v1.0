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
from datetime import datetime,date,timedelta


class show_MainWindow(QMainWindow):

    def __init__(self):

        super(show_MainWindow, self).__init__()

        self.setupUi(self)


    def setupUi(self,Ui_show):
        Ui_show.setObjectName("Ui_show")
        Ui_show.resize(800, 600)
        Ui_show.setStyleSheet("#Ui_show{border-image:url(image/1.jpg)}")
        Ui_show.centralwidget = QtWidgets.QWidget(Ui_show)
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


        # 新增日期选择按钮
        self.dataIN = QtWidgets.QDateEdit(Ui_show)
        self.dataIN.setGeometry(QtCore.QRect(690, 80, 80, 32))
        self.dataIN.setObjectName("dataIN")
        self.dataIN.setDateTime(QDateTime.currentDateTime())


        #
        self.dataIN2 = QtWidgets.QDateEdit(Ui_show)
        self.dataIN2.setGeometry(QtCore.QRect(690, 120, 80, 32))
        self.dataIN2.setObjectName("dataIN2")
        self.dataIN2.setDateTime(QDateTime.currentDateTime())


        self.dateBNT = QtWidgets.QPushButton(Ui_show)
        self.dateBNT.setGeometry(QtCore.QRect(670, 160, 120, 32))
        self.dateBNT.setObjectName("dateBNT")

        self.query()

        self.dateBNT.clicked.connect(self.datein)
        self.retranslateUi(Ui_show)

    #
    def datein(self):#新增日期选择
        global D1,D2
        date1 = self.dataIN.text()
        D1 = datetime.strptime(date1, "%Y/%m/%d").date()
        date2 = self.dataIN2.text()
        D2 = datetime.strptime(date2, "%Y/%m/%d").date()

        self.query1()#新增日期选择


    def query(self):  # 待完善：显示全部、显示完成、显示未完成、选取日期等
        now_time = datetime.today()  # 结束时间
        now_date = now_time.date()


        self.plan_list.setRowCount(0)  # 清空表格中的所有行
        # 调用服务类中的公共方法执行查询语句#设置计划的数据库
        result = service.query("select over_date,kemu,neirong,shichang,zuotishichang,defen from tb_plan where wancheng_shifou =%s and over_date=%s", 1,now_date)

        row = len(result)  # 取得记录个数，用于设置表格的行数

        self.plan_list.setRowCount(row)  # 设置表格行数
        self.plan_list.setColumnCount(6)  # 设置表格列数
        self.plan_list.setStyleSheet("QTableWidget{background:rgb(0, 0, 0,50);}"
                                     "QTableWidget{color:rgb(172, 255, 47, 250); font-size:20px; font-weight:bold}")
        # if a2.setvalue（）      #设置只显示未完成的数据
        # 设置表格的标题名称
        self.plan_list.setHorizontalHeaderLabels(['完成日期', '科目', '内容', "计划时长","实际用时","得分"])
        for i in range(row):  # 遍历行
            for j in range(self.plan_list.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格

                self.plan_list.setItem(i, j, data)  # 设置每个单元格的数据


    def query1(self):  # 待完善：显示全部、显示完成、显示未完成、选取日期等


        self.plan_list.setRowCount(0)  # 清空表格中的所有行
        # 调用服务类中的公共方法执行查询语句#设置计划的数据库

        result = service.query(
            "select over_date,kemu,neirong,shichang,zuotishichang,defen from tb_plan where wancheng_shifou =%s and %s <= over_date and %s >= over_date",
            1,D1,D2)

        row = len(result)  # 取得记录个数，用于设置表格的行数

        self.plan_list.setRowCount(row)  # 设置表格行数
        self.plan_list.setColumnCount(6)  # 设置表格列数
        self.plan_list.setStyleSheet("QTableWidget{background:rgb(0, 0, 0,50);}"
                                     "QTableWidget{color:rgb(172, 255, 47, 250); font-size:20px; font-weight:bold}")
        # if a2.setvalue（）      #设置只显示未完成的数据
        # 设置表格的标题名称
        self.plan_list.setHorizontalHeaderLabels(['完成日期', '科目', '内容', "计划时长","实际用时","得分"])
        for i in range(row):  # 遍历行
            for j in range(self.plan_list.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格

                self.plan_list.setItem(i, j, data)  # 设置每个单元格的数据



    def retranslateUi(self,Ui_show):

        _translate = QtCore.QCoreApplication.translate
        Ui_show.setWindowTitle(_translate("Ui_show", "击毙的小兔子"))
        self.dateBNT.setText(_translate("Ui_show", "选择起止日期"))




