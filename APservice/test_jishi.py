import sys
from time import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,  QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from APservice.Ui_timer import Ui_MainWindow1
from APservice.service import convert,convert1
# from APservice.service import *
from APservice import service
from APdatabase import plan
# from APdatabase.plan import planid_x,kemu_x,eirong_x,shichang_x
import APdatabase.a2 as a2
import time as timeUtil
# from APservice.scor import *
# from APservice import scor
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist,QMediaContent#添加音频控制


def get():
    return getvalue2()

class Timer(QMainWindow, Ui_MainWindow1):
    # print(planid_x,kemu_x,eirong_x,shichang_x,"引入")
    def __init__(self, parent=None):
        # 继承主窗口类

        super(Timer, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        #
        # self.player = QMediaPlayer(self)
        # self.playlist = QMediaPlaylist(self)
        # self.playlist.setPlaybackMode(QMediaPlaylist.Once)


        # 初始化设置
        self.init_setting()


    def initUI(self):
        global L,T,C,P
        L = int(a2.getvalue('shichang_x'))
        C = int(L*2/3)
        P = int(L*1/2)
        # print(C,type(C),P,type(P))
        T = {"科目":a2.getvalue('kemu_x'),"内容":a2.getvalue('neirong_x'),"计划时长":a2.getvalue('shichang_x')}

        # 设定 label 的样式
        self.label.setStyleSheet("QLabel{background:rgb(0, 0, 0,100);}"
                                 "QLabel{color:rgb(250, 250, 250, 250); font-size:80px; font-weight:bold}")
        self.label.setFrameShadow(QFrame.Raised)

        # self.label_show.setStyleSheet("QLabel{background:rgb(0, 0, 0);}"
        #                          "QLabel{color:rgb(20, 150, 200, 250); font-size:20px; font-weight:bold}")
        self.label_show.setFrameShadow(QFrame.Raised)
        # initUI.setStyleSheet("#MainWindow1{border-image:url(image/3.jpg)}")

        # 创建 QTimer 对象
        # 将 QTimer 实例与 showTime 函数绑定
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        # self.timer.start(5)

        # 执行初始化按钮状态
        self.setPushButton()

        # 将按钮与对应函数绑定
        self.pushButton.clicked.connect(self.startTimer1)
        self.pushButton_2.clicked.connect(self.pauseTimer)
        self.pushButton_3.clicked.connect(self.clearTimer)
        self.pushButton_3.clicked.connect(self.update1)
        self.pushButton_2.clicked.connect(self.dafen)
        # 添加按钮：

    def init_setting(self):
        # 初始化设置
        self._start_time = None
        self._pause_flag = False
        self._pause_time = 0
        self._restart_time = 0
        self._pause_total = 0
        self.label.setText("00:00:00")
        self.label.setStyleSheet("QLabel{background:rgb(0, 0, 0,100);}"
                                 "QLabel{color:rgb(0, 255, 17, 250); font-size:80px; font-weight:bold}")
        self.label_show.setText("")
        text2 = str(T)
        self.label_show.setText(text2)
        self.label_show.setStyleSheet("QLabel{background:rgb(0, 0, 0,100);}"
                                 "QLabel{color:rgb(20, 150, 200, 250); font-size:30px; font-weight:bold}")



    @property
    def _current_time(self):
        # 返回当前时间
        return time()
    def dafen(self):
        defen,ok = QInputDialog.getDouble(self,"得分",'请打分',0.01,0,100,2)

        if ok:
            self.lineEdit_defen.setText(str(defen))
            planID = int(a2.getvalue('planid_x'))
            result = service.exec("update tb_plan set defen=%s,wancheng_shifou=%s where planID=%s",
                                  (defen, 1, planID))

    def showTime(self):#
        # 如果暂停标志为真，self._pause_total 属性要加上暂停时间
        # 并设置暂停标志为假
        global run_time
        if self._pause_flag:
            self._pause_total +=  self._restart_time - self._pause_time
            self._pause_flag = False
        # 计算运行时间
        run_time = self._current_time - self._pause_total - self._start_time#run_time为float类型，需要和计划时长的数据整理后使用
        timeUtil.sleep(0.9)

        #测试此处改造下："if"5分钟倒计时预警前提示"计时"，"elseif"5分钟预警期提示"倒计时"，"else"超出后："红色超时提示"
        if int(run_time/60) < C:#5:#此处10代表计划时长的实例#此处没问题
            text = convert(run_time)
            # sleep(10)#测试暂停1秒，计时是否正常走
            # if int(run_time/60)==P:#过1/2提示声音提示，待完成
            #     song = QMediaContent(QUrl.fromLocalFile(filename))
            #     self.playlist.addMedia(song)
            #     self.player.play()

            self.label.setStyleSheet("QLabel{background:rgb(0, 0, 0,150);}"
                                          "QLabel{color:rgb(0, 255, 17, 250); font-size:80px; font-weight:bold}")

        elif int(run_time/60) < L and int(run_time/60) >= C:

            # if int(run_time/60)==C:#过2/3提醒
                # song = QMediaContent(QUrl.fromLocalFile(filename))
                # self.playlist.addMedia(song)
                # self.player.play()

            # 颜色预警

            text = convert(float(L*60) - run_time)

            self.label.setStyleSheet("QLabel{background:rgb(0, 0, 0,200);}"
                                     "QLabel{color:rgb(255, 187, 0, 250); font-size:80px; font-weight:bold}")
            # 橙色倒计时提醒
        else:
            text = convert(run_time - float(L*60))#颜色预警
            self.label.setStyleSheet("QLabel{background:rgb(0, 0, 0,250);}"
                                     "QLabel{color:rgb(255, 0, 0, 250); font-size:80px; font-weight:bold}")
            # 红色超时示警
            # song = QMediaContent(QUrl.fromLocalFile(filename))
            # self.playlist.addMedia(song)
            # self.player.play()
        self.label.setText(text)




    def startTimer1(self):
        # 发出计时信号
        self.timer.start(0)
        # 如果 self._pause_flag 为真，更新开始时间
        # 否则，更新重启时间
        if not self._pause_flag:
            self._start_time = self._current_time
        else:
            self._restart_time = self._current_time
        # 设置按钮属性
        self.setPushButton(btn1=False, btn2=True, btn3=True)


    def pauseTimer(self):
        self._pause_flag = True
        self._pause_time =  self._current_time
        # 停止发送信号
        self.timer.stop()
        self.setPushButton(btn1=True, btn2=False, btn3=True)


    def clearTimer(self):
        # 还原至初始状态
        self.init_setting()
        self.timer.stop()
        self.setPushButton()
        # plan.query(slef)

    #添加倒计时闹铃，进度条和番茄闹铃#待完善优化
    #添加数据库更新：开始时间、结束时间、休息时间、打分、完成标签、较平均分等变化情况
    def update1(self):#设置数据库更新
        global planID

        planID = int(a2.getvalue('planid_x'))

        shichang = convert1(int(run_time))


        result = service.exec("update tb_plan set zuotishichang=%s,wancheng_shifou=%s where planID=%s",(shichang,1,planID))

        if result > 0:  # 如果结果大于0，说明添加成功

            QMessageBox.information(None, '提示', '恭喜帅哥又击毙一只兔子！', QMessageBox.Ok)
            self.close()
            self.m = plan.Ui_MainWindow()#重启后刷新
            self.m.show()


        else:
                QMessageBox.information(None, '提示', '数据库更新不成功！', QMessageBox.Ok)


    def setPushButton(self, *, btn1=True, btn2=False, btn3=False):
        # 设置按钮属性
        self.pushButton.setEnabled(btn1)
        self.pushButton_2.setEnabled(btn2)
        self.pushButton_3.setEnabled(btn3)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())