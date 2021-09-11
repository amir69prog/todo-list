# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 488)
        MainWindow.setStyleSheet("QMenuBar{\n"
"    background-color:rgb(31, 31, 31)\n"
"}\n"
"\n"
"QStatusBar{\n"
"    background-color:rgb(31, 31, 31)\n"
"}\n"
"\n"
"QWidget{\n"
"    background-color:rgb(31, 31, 31)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.first_frame = QtWidgets.QFrame(self.centralwidget)
        self.first_frame.setGeometry(QtCore.QRect(10, 0, 481, 111))
        self.first_frame.setStyleSheet("QLabel {\n"
"    \n"
"    font: 87 20pt \"Verdana Pro Cond Black\";\n"
"    color:rgb(184, 184, 184)\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color:transparent;\n"
"     border: 2px solid rgb(184, 184, 184) ;\n"
"       border-radius:20px;\n"
"    color: rgb(184, 184, 184);\n"
"    font: 12pt \"Open Sans\";\n"
"    padding:5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    border: 4px solid  rgb(184, 184, 184);\n"
"    border-radius:20px\n"
"}\n"
"\n"
"")
        self.first_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_frame.setObjectName("first_frame")
        self.task = QtWidgets.QLineEdit(self.first_frame)
        self.task.setGeometry(QtCore.QRect(10, 60, 421, 41))
        self.task.setText("")
        self.task.setObjectName("task")
        self.label = QtWidgets.QLabel(self.first_frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.insert = QtWidgets.QPushButton(self.first_frame)
        self.insert.setGeometry(QtCore.QRect(440, 60, 41, 41))
        self.insert.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\images\\icon_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert.setIcon(icon)
        self.insert.setIconSize(QtCore.QSize(45, 45))
        self.insert.setObjectName("insert")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(20, 130, 411, 311))
        self.list.setStyleSheet("QListWidget{\n"
"background-color:transparent;\n"
"     border: 2px solid rgb(184, 184, 184) ;\n"
"       border-radius:20px;\n"
"    color: rgb(184, 184, 184);\n"
"    font: 12pt \"Open Sans\";\n"
"    padding:10px;\n"
"}")
        self.list.setObjectName("list")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 150, 371, 21))
        self.widget.setStyleSheet("background-color:transparent;")
        self.widget.setObjectName("widget")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Todo List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
