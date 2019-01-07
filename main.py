from  ui.mainWindow import *
import sys

# '''
# 解决pycharm不报错的问题：https://blog.csdn.net/qq842977873/article/details/82505575
# '''
if __name__ == '__main__':
    app=QApplication(sys.argv)
    kasike = mainWin()
    app.exec_()
