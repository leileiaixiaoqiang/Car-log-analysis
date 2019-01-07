from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from Figure import  MyFigure
from subWindow import *


from db.mongo import Mongo
class mainWin(QWidget):
    def __init__(self):
        super().__init__()
        self._initUI()

        # self.draw_signal.connect(self.draw_widget)

    def _initUI(self):

        # self.setGeometry(0,0,640,480)
        self.setFixedSize(1200,600)
        # self.setGeometry(300,300,1200,600)

        self.VWidget=QWidget(self)
        self.VWidget.setGeometry(0,0,250,self.height())
        self.VLayout=QVBoxLayout(self.VWidget)

        self.button1=QPushButton('选择二进制文件',self)
        self.button1.clicked.connect(self.on_click_button1)
        self.VLayout.addWidget(self.button1)

        self.button2=QPushButton('选择模板文件',self)
        self.button2.clicked.connect(self.on_click_button2)
        self.VLayout.addWidget(self.button2)

        self.button3=QPushButton('开始解析',self)
        self.button3.clicked.connect(self.on_click_button3)
        self.VLayout.addWidget(self.button3)

        spacerItem1 =QSpacerItem(250,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.VLayout.addItem(spacerItem1)

        self.button4 = QPushButton('选择开关量条件', self)
        self.button4.clicked.connect(self.on_click_button4)
        self.VLayout.addWidget(self.button4)

        self.button5 = QPushButton('选择模拟量条件', self)
        self.button5.clicked.connect(self.on_click_button5)
        self.VLayout.addWidget(self.button5)

        self.button6 = QPushButton('选择查询字段', self)
        self.button6.clicked.connect(self.on_click_button6)
        self.VLayout.addWidget(self.button6)

        self.button7 = QPushButton('画图', self)
        self.button7.clicked.connect(self.on_click_button7)
        self.VLayout.addWidget(self.button7)

        spacerItem2 =QSpacerItem(250,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.VLayout.addItem(spacerItem2)

        self.tree1=QTreeWidget(self)
        self.tree1.setColumnCount(2)
        self.tree1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tree1.setObjectName("treeWidget1")
        self.tree1.setHeaderHidden(True)

        root1=QTreeWidgetItem(self.tree1)
        root1.setText(0,"开关量")
        root2 = QTreeWidgetItem(self.tree1)
        root2.setText(0, "模拟量")
        root3 = QTreeWidgetItem(self.tree1)
        root3.setText(0, "查询字段")

        self.VLayout.addWidget(self.tree1)

        self.tree2 = QTreeWidget(self)
        self.tree2.setColumnCount(2)  # 设置部件的列数为2
        self.tree2.setColumnWidth(0,250)
        self.tree2.setHeaderLabels(['Key', 'Value'])  # 设置头部信息对应列的标识符
        self.tree2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tree2.setObjectName("treeWidget2")
        self.tree2.setGeometry(250,0,400,self.height())

        self.plotWidget=QWidget(self)
        self.plotWidget.setGeometry(650,0,self.width()-650,self.height())
        self.gridLayout=QGridLayout(self.plotWidget)

        self.fig1=MyFigure()
        self.gridLayout.addWidget(self.fig1)

        self.fig2 = MyFigure()
        self.gridLayout.addWidget(self.fig2)

        self.show()

    def draw_widget(self):
        self.fig1.plotcos()
        self.fig2.plotcos()
        self.fig1.draw()
        self.fig2.draw()

    def on_click_button1(self):
        self.binFilePath=QFileDialog.getOpenFileName(caption='选择二进制文件')[0]

    def on_click_button2(self):
        self.xmlFilePath=QFileDialog.getOpenFileName(caption='选择模板文件',filter="xml Files (*.xcp)")[0]

    def on_click_button3(self):
        # print("这里需要对模板文件和二进制文件进行解析")
        # 这里进行数据库的连接
        filePath=self.binFilePath
        self.db=Mongo(filePath)


    #开关量响应
    def on_click_button4(self):
        try:
            switches = self.db.findSwitches()
            self.switches=switchCombo(switches)
            self.switches.signal.connect(self.dealSwitches)
        except:
            print("请先选择二进制文件")
    #处理开关量信息
    def dealSwitches(self,text):
        print(text)
        print("模拟量")

    #模拟量响应
    def on_click_button5(self):
        try:
            analogs = self.db.findAnalogs()
            self.analogs = anaCombo(analogs)
            self.analogs._signal.connect(self.dealAnalogs)
        except:
            # print("请先选择二进制文件")
            print('choose binary file')

    def dealAnalogs(self,text):
        print(text)
        print("analogs")

    #选择字段响应
    def on_click_button6(self):
        try:
            searches = self.db.findSearches()
            self.searches = searchCombo(searches)
            self.searches._signal.connect(self.dealSearches)
        except:
            print("choose binary file first")

    def dealSearches(self,text):
        print(text)

    def on_click_button7(self):
        self.fig1.plotcos()
        self.fig2.plotcos()
        self.fig1.draw()
        self.fig2.draw()



        root4 = QTreeWidgetItem(self.tree1)
        root4.setText(0, "啦啦啦")
        # self.tree1.drawTree()
    def tree_struct1(self,parent,data):
        # for data in datas:
        #     root = QTreeWidgetItem(parent)
        #     root.setText(0,str(data['_id']))
        #     root.setText(1, str(len(data)))
        #     if flag:
        #         parent.addTopLevelItem(root)
        #         p = []
        #         for k, v in data.items():
        #             child = QTreeWidgetItem(root)
        #             child.setText(0, k)
        #             child.setText(1, str(v))
        #             p.append(child)
        #         root.addChildren(p)
        #         flag=False
        #     else:
        #         child=QTreeWidgetItem(root)
        #         child.setText(0,'1')
        #         child.setText(1,'2')
        pass

