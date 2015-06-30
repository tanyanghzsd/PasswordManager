#coding:utf-8
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys,os
import MySQLdb
#from pwdsaver_ui import Ui_Form

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(432, 567)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(100, 130, 256, 191))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 420, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 340, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(98, 40, 102, 18))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 80, 262, 25))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(101, 361, 135, 128))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 520, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 520, 171, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 500, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.search)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.addinfo)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.importfile)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "密码管理器3.0", None))
        self.pushButton_2.setText(_translate("Form", "确定", None))
        self.label.setText(_translate("Form", "添加信息", None))
        self.radioButton.setText(_translate("Form", "类型", None))
        self.radioButton_2.setText(_translate("Form", "账号", None))
        self.pushButton.setText(_translate("Form", "查询", None))
        self.label_2.setText(_translate("Form", "类型：", None))
        self.label_3.setText(_translate("Form", "账号：", None))
        self.label_4.setText(_translate("Form", "密码：", None))
        self.pushButton_3.setText(_translate("Form", "导入", None))
        self.label_5.setText(_translate("Form", "导入文件", None))




class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.pushButton_2.clicked.connect(self.addinfo)
        self.ui.pushButton_3.clicked.connect(self.importfile)
    
    def search(self):
        if (self.ui.radioButton.isChecked()):
            self.type(self.ui.lineEdit.text())
            
        if (self.ui.radioButton_2.isChecked()):
            self.useid(self.ui.lineEdit.text())

    def type(self,mytype):
        conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='',
                db='passwordsaver',
                charset='utf8'
                )
        cur=conn.cursor()
        
        sql='select * from 密码管理器 where 类型="%s"'%mytype
        item=cur.execute(sql)
        info=cur.fetchmany(item)
        self.ui.textBrowser.setText('')
        for ii in info:
            self.ui.textBrowser.append(ii[0])     
            self.ui.textBrowser.append(ii[1])
            self.ui.textBrowser.append(ii[2])
        cur.close()
        conn.close()

    def useid(self,myid):
        conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='',
                db='passwordsaver',
                charset='utf8'
                )
        cur=conn.cursor()
        sql='select * from 密码管理器 where 账号="%s"'% myid
        item=cur.execute(sql)
        info=cur.fetchmany(item)
        self.ui.textBrowser.setText('')
        for ii in info:
            self.ui.textBrowser.append(ii[0])           
            self.ui.textBrowser.append(ii[1])   
            self.ui.textBrowser.append(ii[2])
            
        cur.close()
        conn.close()

    def addinfo(self):
        self.add(self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text())
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_4.setText('')

    def add(self,mytype,myid,mypasswd):
        conn=MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='',
                db='passwordsaver',
                charset='utf8'
                )
        cur=conn.cursor()
        sql="insert into 密码管理器 values('%s','%s','%s')"%(mytype,myid,mypasswd)
        cur.execute(sql)
        conn.commit()    
        cur.close()
        conn.close()

    def importfile(self):
        
        self.ui.filepath=self.ui.lineEdit_5.text()
        self.importfile_2(self.ui.filepath)
        # self.ui.lineEdit_5.setText('')
        

    def importfile_2(self,filepath):
       
            # C:\\Users\\Sheldon\\Desktop\\password.txt
            # C:/Users/Sheldon/Desktop/mima.txt
            #filepath=filepath
        f=open(filepath,'r')
        for line in f:
            if line:
                content=line.split(',')
                if len(content)==3:
                    self.importdata(content[0],content[1],content[2])
                # else :
                #     self.importdata('您输入的“类型”或“账号”不存在','','')
        f.close()    
        #self.ui.lineEdit_5.setText('')


    def importdata(self,mytype,myid,mypasswd):
        conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='passwordsaver',
        charset='utf8'
        )

        cur=conn.cursor()
        sql="insert ignore into 密码管理器(类型,账号,密码)values('%s','%s','%s')"%(mytype,myid,mypasswd)
        cur.execute(sql)
        # sql="select *,count(distinct 账号) from 密码管理器 group by 账号"
        # cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_())