from PyQt5.QtWidgets import QWidget
from  PyQt5.QtWidgets import QComboBox,QGridLayout,QPushButton,QRadioButton,QLineEdit,QVBoxLayout

from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import pyqtSignal,pyqtSlot

class switchCombo(QWidget):
    signal = pyqtSignal(object)
    def __init__(self,switches):
        super().__init__()
        self.switches=switches
        self.initUI()

    def initUI(self):

        # w1=QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        # # w1.setSizePolicy(sizePolicy)
        # w1.setStyleSheet("QWidget{\n"
        self.setStyleSheet("QWidget{\n"
                                  # "    background-color:white;\n"
                                  # "    border-radius:25px;\n"
                                  "    border-width:0px;\n"
                                  "}")

        self.grid_layout=QGridLayout()
        self.setLayout(self.grid_layout)
        self.gridlayout_last_x = 0

        self.radioList=[]

        #comboBox1
        self.combo1 = QComboBox()
        self.combo1.setObjectName("0_0")
        self.combo1.addItems(self.switches)
        #addWidget的6个参数说明:控件名，行，列，占用行数，占用列数，对齐方式
        self.grid_layout.addWidget(self.combo1, 0, 0, 1, 1)

        #comboBox2
        self.combo2 =QComboBox()
        self.combo2.setObjectName("0_1")
        self.combo2.addItems(['True','False'])
        self.grid_layout.addWidget(self.combo2,0, 1, 1, 1)

        # self.conditions[self.combo1.currentText()]=self.combo2.currentText()
        # radio1
        self.radio1 = QRadioButton()
        self.radio1.setObjectName("0_2")
        self.radio1.setAutoExclusive(False)
        self.radioList.append(self.radio1)
        self.grid_layout.addWidget(self.radio1, 0, 2, 1, 1)

        self.pushButton1 = QPushButton("添加条件")
        self.pushButton1.setObjectName("pushButton_1")
        self.grid_layout.addWidget(self.pushButton1, 0, 3, 1, 1)
        self.pushButton1.clicked.connect(self.on_clicked_button1)

        self.pushButton2 = QPushButton("删除条件")
        self.pushButton2.setObjectName("pushButton_2")
        self.grid_layout.addWidget(self.pushButton2, 0, 4, 1, 1)
        self.pushButton2.clicked.connect(self.on_clicked_button2)

        self.pushButton3 = QPushButton("确定")
        self.pushButton3.setObjectName("pushButton_3")
        self.grid_layout.addWidget(self.pushButton3, 1, 3, 1, 1)
        self.pushButton3.clicked.connect(self.on_clicked_button3)

        self.setWindowTitle('开关量条件')

        # self.setGeometry(300, 800, 500, 500)

        self.show()

    def on_clicked_button1(self):

        self.gridlayout_last_x +=1
        combox_add_1= QComboBox()
        combox_add_1.addItems(self.switches)
        combox_add_1.setObjectName("%d_0"%self.gridlayout_last_x)
        self.grid_layout.addWidget(combox_add_1, self.gridlayout_last_x, 0, 1, 1)

        combox_add_2 = QComboBox()
        combox_add_2.addItems(["True","False"])
        combox_add_2.setObjectName("%d_1"%self.gridlayout_last_x)
        self.grid_layout.addWidget(combox_add_2, self.gridlayout_last_x, 1, 1, 1)

        # radio
        radio = QRadioButton()
        radio.setAutoExclusive(False)
        radio.setObjectName("%d_2"%self.gridlayout_last_x)
        self.radioList.append(radio)
        self.grid_layout.addWidget(radio, self.gridlayout_last_x, 2, 1, 1)

    def on_clicked_button2(self):
        ComboRemoveList=[]
        RadioRemoveList=[]
        for i in self.radioList:
            if i.isChecked():
                ComboRemoveList.extend([i.objectName().split("_")[0]+"_0",i.objectName().split("_")[0]+"_1"])
                RadioRemoveList.extend([i.objectName().split("_")[0]+"_2"])
        for i in ComboRemoveList:
            removeCombo=self.findChild(QComboBox,i)
            #布局和控件的关系是啥啊。。。一脸懵逼
            self.grid_layout.removeWidget(removeCombo)
            removeCombo.deleteLater()
        for i in RadioRemoveList:
            removeRadio=self.findChild(QRadioButton,i)

            self.radioList.remove(removeRadio)
            #布局和控件的关系是啥啊。。。一脸懵逼
            self.grid_layout.removeWidget(removeRadio)
            removeRadio.deleteLater()
        self.adjustSize()

        # self.grid_layout.removeItem(self.pushButton2)

    def on_clicked_button3(self):
        children=self.children()
        QComboChilds=[]
        conditions={}
        j=0
        # try:
        for i in children:
            if  isinstance(i,QComboBox):
                QComboChilds.append(i)
        while QComboChilds:
            key=QComboChilds.pop(0).currentText()
            value=QComboChilds.pop(0).currentText()
            conditions[key]=value
        self.signal.emit(conditions)
        # except:
        #     print("发生错误")

class anaCombo(QWidget):
    _signal = pyqtSignal(object)
    def __init__(self,analogs):
        super().__init__()

        self.analogs=analogs
        self.initUI()

    def initUI(self):

        # w1=QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        # # w1.setSizePolicy(sizePolicy)
        # w1.setStyleSheet("QWidget{\n"
        self.setStyleSheet("QWidget{\n"
                                  # "    background-color:white;\n"
                                  # "    border-radius:25px;\n"
                                  "    border-width:0px;\n"
                                  "}")
        self.radioList=[]

        self.grid_layout=QGridLayout()
        self.setLayout(self.grid_layout)
        self.gridlayout_last_x = 0

        #comboBox1
        self.combo = QComboBox()
        self.combo.setObjectName("0_0")
        self.combo.addItems(self.analogs)
        #addWidget的6个参数说明:控件名，行，列，占用行数，占用列数，对齐方式
        self.grid_layout.addWidget(self.combo, 0, 0, 1, 1)


        self.fixedCombo1=self._getFixedCombo([">="," >","="],"0_1")
        self.fixedCombo1.currentIndexChanged.connect(lambda :self._checkLineEdit(self.fixedCombo1))
        self.grid_layout.addWidget(self.fixedCombo1,0, 1, 1, 1)
        #
        self.lineEdit1= self._getLineEdit("0_2")
        self.grid_layout.addWidget(self.lineEdit1,0, 2, 1, 1)

        self.fixedCombo2 = self._getFixedCombo(["<=", " <"], "0_3")
        self.grid_layout.addWidget(self.fixedCombo2, 0, 3, 1, 1)

        self.lineEdit2 = self._getLineEdit("0_4")
        self.grid_layout.addWidget(self.lineEdit2, 0, 4, 1, 1)

        self.radio1 = QRadioButton()
        self.radio1.setObjectName("0_5")
        self.radio1.setAutoExclusive(False)
        self.radioList.append(self.radio1)
        self.grid_layout.addWidget(self.radio1, 0, 5, 1, 1)

        self.pushButton1 = QPushButton("添加条件")
        self.pushButton1.setObjectName("pushButton_1")
        self.grid_layout.addWidget(self.pushButton1, 0, 6, 1, 1)
        self.pushButton1.clicked.connect(self.on_clicked_button1)

        self.pushButton2 = QPushButton("删除条件")
        self.pushButton2.setObjectName("pushButton_2")
        self.grid_layout.addWidget(self.pushButton2, 0, 7, 1, 1)
        self.pushButton2.clicked.connect(self.on_clicked_button2)

        self.pushButton3 = QPushButton("确定")
        self.pushButton3.setObjectName("pushButton_3")
        self.grid_layout.addWidget(self.pushButton3, 1, 6, 1, 1)
        self.pushButton3.clicked.connect(self.on_clicked_button3)


        # self.setGeometry(300, 800, 500, 500)

        self.setWindowTitle("模拟量条件")

        self.show()

    def _getFixedCombo(self,items,name):
        fixedCombo= QComboBox()
        fixedCombo.addItems(items)
        fixedCombo.setStyleSheet("QComboBox::drop-down{border-style: none;}")
        fixedCombo.setObjectName(name)
        fixedCombo.setFixedSize(35, 20)
        fixedCombo.setObjectName(name)
        return fixedCombo

    def _getFixedLineEdit(self, text,name):
        fixedlineEdit =QLineEdit()
        fixedlineEdit.setText(text)
        fixedlineEdit.setFixedSize(25, 20)
        fixedlineEdit.setObjectName(name)
        fixedlineEdit.setReadOnly(True)
        fixedlineEdit.setStyleSheet("QLineEdit{background-color:grey;border:0px;}")
        return fixedlineEdit

    def _getLineEdit(self, name):
        lineEdit = QLineEdit()
        lineEdit.setObjectName(name)
        lineEdit.setFixedSize(25, 20)
        return lineEdit

    def on_clicked_button1(self):
        self.gridlayout_last_x +=1
        # row=str(self.gridlayout_last_x)
        row=self.gridlayout_last_x

        combo = QComboBox()
        combo.setObjectName(str(row)+"_0")
        combo.addItems(self.analogs)
        # addWidget的6个参数说明:控件名，行，列，占用行数，占用列数，对齐方式
        self.grid_layout.addWidget(combo, row, 0, 1, 1)

        fixedCombo1= self._getFixedCombo([">="," >","=="],str(row)+"_1")
        fixedCombo1.currentIndexChanged.connect(lambda :self._checkLineEdit(fixedCombo1))
        self.grid_layout.addWidget(fixedCombo1, row, 1, 1, 1)

        lineEdit1 = self._getLineEdit(str(row)+"_2")
        self.grid_layout.addWidget(lineEdit1, row, 2, 1, 1)

        fixedCombo2 = self._getFixedCombo(["<=", " <"], str(row) + "_3")
        self.grid_layout.addWidget(fixedCombo2, row, 3, 1, 1)

        lineEdit2 = self._getLineEdit(str(row)+"_4")
        self.grid_layout.addWidget(lineEdit2, row, 4, 1, 1)

        radio = QRadioButton()
        radio.setObjectName(str(row)+"_5")
        radio.setAutoExclusive(False)
        self.radioList.append(radio)
        self.grid_layout.addWidget(radio, row, 5, 1, 1)

    def on_clicked_button2(self):
        ComboRemoveList=[]
        QLineEditRemoveList=[]
        RadioRemoveList=[]

        for i in self.radioList:
            prefix=i.objectName().split("_")[0]
            if i.isChecked():
                ComboRemoveList.extend([prefix+ "_0",prefix+ "_1",prefix+ "_3"])
                QLineEditRemoveList.extend([prefix+ "_2",prefix+ "_4"])
                RadioRemoveList.extend([i.objectName().split("_")[0] + "_5"])
        for i in ComboRemoveList:
            removeCombo=self.findChild(QComboBox,i)
            #布局和控件的关系是啥啊。。。一脸懵逼
            self.grid_layout.removeWidget(removeCombo)
            removeCombo.deleteLater()
        for i in RadioRemoveList:
            removeRadio=self.findChild(QRadioButton,i)
            self.radioList.remove(removeRadio)
            #布局和控件的关系是啥啊。。。一脸懵逼
            self.grid_layout.removeWidget(removeRadio)
            removeRadio.deleteLater()
        for i in QLineEditRemoveList:
            removeLine=self.findChild(QLineEdit,i)
            self.grid_layout.removeWidget(removeLine)
            removeLine.deleteLater()
        self.adjustSize()
        # self.grid_layout.removeItem(self.pushButton2)

    def on_clicked_button3(self):
        childrens=self.children()
        conditions={}
        for i in childrens:
            if isinstance(i,QComboBox):
                if i.objectName().endswith('0'):
                    key=i.currentText()
                    value=""
                else:
                    value+=i.currentText()
            if isinstance(i,QLineEdit):
                if value[-2:] in ["=="," <","<="]:
                    value+=i.text()
                    conditions[key]=value
                else:
                    value+=i.text()
        self._signal.emit(conditions)

class searchCombo(QWidget):


    _signal=pyqtSignal(object)
    def __init__(self,searches):
        super().__init__()
        self.searches=searches
        self.initUI()
    def initUI(self):

        # w1=QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        # # w1.setSizePolicy(sizePolicy)
        # w1.setStyleSheet("QWidget{\n"
        self.setStyleSheet("QWidget{border-width:0px;}")

        self.Glayout=QGridLayout()
        self.setLayout(self.Glayout)

        #comboBox1
        self.combo1 = QComboBox()
        self.combo1.adjustSize()
        self.combo1.setObjectName("0_0")
        self.combo1.addItems(self.searches)
        #addWidget的6个参数说明:控件名，行，列，占用行数，占用列数，对齐方式
        self.Glayout.addWidget(self.combo1,0,0,1,1,)

        #comboBox2
        self.combo2 =QComboBox()
        self.combo2.adjustSize()
        self.combo2.setObjectName("1_0")
        self.combo2.addItems(self.searches)
        self.Glayout.addWidget(self.combo2, 1, 0, 1, 1, )


        self.pushButton = QPushButton("确定")
        self.pushButton.setObjectName("0_1")
        self.Glayout.addWidget(self.pushButton,0,1,1,1)
        self.pushButton.clicked.connect(self.on_clicked_button)

        # self.setFixedSize(400,300)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle("查询字段")
        self.show()
    def on_clicked_button(self):
        conditions=[]
        conditions.extend([self.combo1.currentText(),self.combo2.currentText()])
        self._signal.emit(conditions)




