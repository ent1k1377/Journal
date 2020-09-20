# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 118))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.authorization = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.authorization.setFont(font)
        self.authorization.setAlignment(QtCore.Qt.AlignCenter)
        self.authorization.setWordWrap(False)
        self.authorization.setObjectName("authorization")
        self.verticalLayout.addWidget(self.authorization)
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setGeometry(QtCore.QRect(210, 180, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_line.setFont(font)
        self.login_line.setObjectName("login_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(210, 240, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_line.setFont(font)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.login = QtWidgets.QLabel(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(210, 156, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(210, 216, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.signIn = QtWidgets.QPushButton(self.centralwidget)
        self.signIn.setGeometry(QtCore.QRect(210, 280, 271, 23))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.signIn.setFont(font)
        self.signIn.setObjectName("signIn")
        self.noAccount = QtWidgets.QLabel(self.centralwidget)
        self.noAccount.setGeometry(QtCore.QRect(500, 280, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.noAccount.setFont(font)
        self.noAccount.setAutoFillBackground(False)
        self.noAccount.setStyleSheet("color: rgb(0, 0, 255);")
        self.noAccount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.noAccount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.noAccount.setObjectName("noAccount")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(290, 150, 291, 21))
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.error.setObjectName("error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
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
        self.authorization.setText(_translate("MainWindow", "Авторизация"))
        self.login.setText(_translate("MainWindow", "Логин:"))
        self.password.setText(_translate("MainWindow", "Пароль:"))
        self.signIn.setText(_translate("MainWindow", "Вход"))
        self.noAccount.setText(_translate("MainWindow", "Нет аккаунта"))
