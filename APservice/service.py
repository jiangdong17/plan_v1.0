import pymysql


# userName="" # 记录用户名

# 打开数据库连接
def open():

    db = pymysql.connect(host="localhost", user="root", password="jh213448", database="db_plan", charset="utf8mb4")
    return db # 返回连接对象


# 执行数据库的增、删、改操作
def exec(sql,values):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标

    try:
        cursor.execute(sql,values) # 执行增删改的SQL语句

        db.commit() # 提交数据

        return 1 # 执行成功

    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败

    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接
def exec1(sql):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标

    try:
        cursor.execute(sql) # 执行增删改的SQL语句

        db.commit() # 提交数据

        return 1 # 执行成功

    except:
        db.rollback() # 发生错误时回滚
        return 0 # 执行失败

    finally:
        cursor.close() # 关闭游标
        db.close() # 关闭数据库连接



# 带参数的精确查询
def query(sql,*keys):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql,keys) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果



# 不带参数的模糊查询
def query2(sql):
    db=open() # 连接数据库
    cursor = db.cursor() # 使用cursor()方法获取操作游标
    cursor.execute(sql) # 执行查询SQL语句
    result = cursor.fetchall() # 记录查询结果
    cursor.close() # 关闭游标
    db.close() # 关闭数据库连接
    return result # 返回查询结果


def convert(raw_time):
    hour = round(raw_time // 3600)
    minute = round((raw_time % 3600) // 60)
    second = int(raw_time % 60)
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(hour, minute, second)
def convert1(raw_time):
    minute = round(raw_time // 60)
    return minute


# def play_music():
#     import pyaudio
#
#     import wave
#
#     import sys
#     from PyQt5 import QtCore, QtMultimedia, QtGui
#     import PyQt5
#
#     chunk = 1024
#
#     wf = wave.open('1.wav', 'rb')
#
#     p = pyaudio.PyAudio()
#
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#
#                     channels=wf.getnchannels(),
#
#                     rate=wf.getframerate(),
#
#                     output=True)
#
#     data = wf.readframes(chunk)
#
#     while len(data) > 0:
#
#         stream.write(data)
#
#         data = wf.readframes(CHUNK)
#
#     stream.stop_stream()
#
#     stream.close()
#
#     p.terminate()
# #
# def add(self):#
#     pass
#
# def openADDUI(self):
#     pass
# play_music()
def play():
    import winsound

    # winsound.Beep(600,1000)

    import os

    os.system("paplay 1.wav")
