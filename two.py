# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 240)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.list_absent = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.list_absent.setFont(font)
        self.list_absent.setObjectName("list_absent")
        self.verticalLayout_2.addWidget(self.list_absent)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.to_print_list = QtWidgets.QPushButton(Form)
        self.to_print_list.setObjectName("to_print_list")
        self.verticalLayout.addWidget(self.to_print_list)
        self.save_list = QtWidgets.QPushButton(Form)
        self.save_list.setObjectName("save_list")
        self.verticalLayout.addWidget(self.save_list)
        self.add_to_report = QtWidgets.QPushButton(Form)
        self.add_to_report.setObjectName("add_to_report")
        self.verticalLayout.addWidget(self.add_to_report)
        self.create_report = QtWidgets.QPushButton(Form)
        self.create_report.setObjectName("create_report")
        self.verticalLayout.addWidget(self.create_report)
        self.close_pr = QtWidgets.QPushButton(Form)
        self.close_pr.setObjectName("close_pr")
        self.verticalLayout.addWidget(self.close_pr)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вывод"))
        self.label.setText(_translate("Form", "Список недостающих актов:"))
        self.to_print_list.setText(_translate("Form", "Распечатать"))
        self.save_list.setText(_translate("Form", "Сохранить"))
        self.add_to_report.setText(_translate("Form", "Добавить в отчёт"))
        self.create_report.setText(_translate("Form", "Сформировать отчёт"))
        self.close_pr.setText(_translate("Form", "Закрыть программу"))
