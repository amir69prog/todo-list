# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(457, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\\ui\\../images/icon_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:rgb(184, 184, 184)")
        self.task = QtWidgets.QLineEdit(Form)
        self.task.setGeometry(QtCore.QRect(10, 10, 431, 51))
        self.task.setStyleSheet("background-color:transparent;\n"
"border: 2px solid rgb(31, 31, 31) ;\n"
"border-radius:20px;\n"
"color:rgb(31, 31, 31);\n"
"font: 12pt \\\"Open Sans\\\";\n"
"padding:5px;")
        self.task.setObjectName("task")
        self.done = QtWidgets.QPushButton(Form)
        self.done.setGeometry(QtCore.QRect(360, 100, 31, 31))
        self.done.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px solid rgb(31, 31, 31);    \n"
"    border-radius:12px;\n"
"}")
        self.done.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\\ui\\../images/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.done.setIcon(icon1)
        self.done.setIconSize(QtCore.QSize(25, 25))
        self.done.setObjectName("done")
        self.time = QtWidgets.QTimeEdit(Form)
        self.time.setGeometry(QtCore.QRect(150, 100, 141, 31))
        self.time.setStyleSheet("background-color:transparent;\n"
"border: 2px solid rgb(31, 31, 31) ;\n"
"border-radius:10px;\n"
"font: 12pt \\\"Open Sans\\\";\n"
"padding:5px;")
        self.time.setObjectName("time")
        self.date = QtWidgets.QDateEdit(Form)
        self.date.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.date.setStyleSheet("background-color:transparent;\n"
"border: 2px solid rgb(31, 31, 31) ;\n"
"border-radius:10px;\n"
"font: 12pt \\\"Open Sans\\\";\n"
"padding:5px;")
        self.date.setObjectName("date")
        self.delete_2 = QtWidgets.QPushButton(Form)
        self.delete_2.setGeometry(QtCore.QRect(310, 100, 31, 31))
        self.delete_2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px solid rgb(31, 31, 31);    \n"
"    border-radius:12px;\n"
"}")
        self.delete_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\\ui\\../images/deleteed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_2.setIcon(icon2)
        self.delete_2.setIconSize(QtCore.QSize(25, 25))
        self.delete_2.setObjectName("delete_2")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(410, 100, 31, 31))
        self.save.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px solid rgb(31, 31, 31);    \n"
"    border-radius:12px;\n"
"}")
        self.save.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("..\\ui\\../images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon3)
        self.save.setIconSize(QtCore.QSize(25, 25))
        self.save.setObjectName("save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.done.setToolTip(_translate("Form", "Done"))
        self.delete_2.setToolTip(_translate("Form", "Delete"))
        self.save.setToolTip(_translate("Form", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
