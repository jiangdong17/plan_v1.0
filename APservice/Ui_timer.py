from PyQt5 import QtCore, QtGui, QtWidgets
# from APdatabase.plan import planid_x,kemu_x,eirong_x,shichang_x#测试选取及倒入是否成功

class Ui_MainWindow1(object):
    # print(planid_x)#测试倒入是否成功
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 570)
        MainWindow1.setStyleSheet("#MainWindow1{border-image:url(image/1.jpg)}")

        self.centralwidget = QtWidgets.QWidget(MainWindow1)#弹出对话框
        self.centralwidget.setObjectName("centralwidget")

        # self.label_defen = QtWidgets.QLabel(self.centralwidget)
        # self.label_defen.setGeometry(QtCore.QRect(30,20,41,16))
        # self.label_defen.setObjectName("label_defen")

        # self.lineEdit_defen = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_defen.setGeometry(QtCore.QRect(70,20, 41, 16))
        # self.lineEdit_defen.setObjectName("label_defen")#出对话框


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/timer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow1.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 162, 91, 51))
        self.pushButton.setObjectName("pushButton")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 149, 2, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 230, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 300, 91, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 200, 450, 100))

        self.label_show = QtWidgets.QLabel(self.centralwidget)#显示计划内容标签
        self.label_show.setGeometry(QtCore.QRect(100, 50, 600, 50))





        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")


        self.label_show.setFont(font)
        self.label_show.setText("")
        self.label_show.setObjectName("label_show")


        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "小样，看我怎么收拾你！"))
        self.pushButton.setText(_translate("MainWindow1", "开始"))
        self.pushButton.setStyleSheet("QPushButton{background:rgb(0, 0, 0,50);}"
                                        "QPushButton{color:rgba(20, 150, 200, 250); font-size:25px; font-weight:bold}")
        self.pushButton_2.setText(_translate("MainWindow1", "暂停、打分"))
        self.pushButton_2.setStyleSheet("QPushButton{background:rgb(0, 0, 0,50);}"
                                        "QPushButton{color:rgba(20, 150, 200, 250); font-size:15px; font-weight:bold}")

        self.pushButton_3.setText(_translate("MainWindow1", "完成"))
        self.pushButton_3.setStyleSheet("QPushButton{background:rgb(0, 0, 0,50);}"
                                        "QPushButton{color:rgba(20, 150, 200, 250); font-size:25px; font-weight:bold}")

        # self.label_defen.setText(_translate("MainWindow1","请打分"))

# import txt_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
