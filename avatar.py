# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avatar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 340, 121, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/1.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 340, 121, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Voucher-143/prof.Pamela/qt designer/LinkExternoAula/img/ezequiel.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 340, 121, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/sanji-careca.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 340, 131, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Downloads/goku-careca.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(620, 340, 131, 121))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Pictures/bald luffy.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.radioButton_wigglytuff = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_wigglytuff.setGeometry(QtCore.QRect(50, 470, 95, 20))
        self.radioButton_wigglytuff.setObjectName("radioButton_wigglytuff")
        self.radioButton_ezequiel = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_ezequiel.setGeometry(QtCore.QRect(190, 470, 95, 20))
        self.radioButton_ezequiel.setObjectName("radioButton_ezequiel")
        self.radioButton_sanji = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_sanji.setGeometry(QtCore.QRect(330, 470, 95, 20))
        self.radioButton_sanji.setObjectName("radioButton_sanji")
        self.radioButton_goku = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_goku.setGeometry(QtCore.QRect(470, 470, 111, 20))
        self.radioButton_goku.setObjectName("radioButton_goku")
        self.radioButton_luffy = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_luffy.setGeometry(QtCore.QRect(620, 470, 121, 20))
        self.radioButton_luffy.setObjectName("radioButton_luffy")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 0, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 70, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 120, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 170, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 220, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(50, 270, 55, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_nome_completo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome_completo.setGeometry(QtCore.QRect(160, 70, 291, 22))
        self.lineEdit_nome_completo.setObjectName("lineEdit_nome_completo")
        self.lineEdit_nome_de_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome_de_usuario.setGeometry(QtCore.QRect(160, 120, 291, 22))
        self.lineEdit_nome_de_usuario.setObjectName("lineEdit_nome_de_usuario")
        self.lineEdit_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_idade.setGeometry(QtCore.QRect(160, 170, 291, 22))
        self.lineEdit_idade.setObjectName("lineEdit_idade")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(160, 220, 291, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(160, 270, 291, 22))
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(50, 310, 151, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setGeometry(QtCore.QRect(330, 500, 121, 28))
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.radioButton_wigglytuff.setText(_translate("MainWindow", "Wigglytuff"))
        self.radioButton_ezequiel.setText(_translate("MainWindow", "Ezequiel"))
        self.radioButton_sanji.setText(_translate("MainWindow", "Sanji Calvo"))
        self.radioButton_goku.setText(_translate("MainWindow", "Gokuzão Calvo"))
        self.radioButton_luffy.setText(_translate("MainWindow", "Luffymose Calvo"))
        self.label_6.setText(_translate("MainWindow", "Preencha seus dados"))
        self.label_7.setText(_translate("MainWindow", "Nome completo:"))
        self.label_8.setText(_translate("MainWindow", "Nome de Usuário:"))
        self.label_9.setText(_translate("MainWindow", "Idade:"))
        self.label_10.setText(_translate("MainWindow", "E-mail:"))
        self.label_11.setText(_translate("MainWindow", "Senha:"))
        self.label_12.setText(_translate("MainWindow", "Escolha seu Personagem:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
