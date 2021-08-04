# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from classes.password import Password


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.checkbox1 = False
        self.checkbox2 = False
        self.checkbox3 = False
        self.checkbox4 = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(90, 160, 261, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 190, 291, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 220, 301, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 250, 461, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 340, 451, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 381, 20))
        self.label.setStyleSheet("font: 75 20pt \"Umpush\";\n"
                                 "color{\n"
                                 "rgb(137, 255, 210)\n"
                                 "}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 300, 191, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 57, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 300, 57, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 60, 51, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(
            "../img/Webp.net-resizeimage.png"))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.clear(mode=self.clipboard.Clipboard)
        #self.clipboard.setGeometry(QtCore.QRect(360, 300, 57, 15))
        self.clipboard.setObjectName("clipboard")
        self.pushButton.clicked.connect(self.print_values)

        self.checkBox.clicked.connect(self.checkbox_touched)
        self.checkBox_2.clicked.connect(self.checkbox_2_touched)
        self.checkBox_3.clicked.connect(self.checkbox_3_touched)
        self.checkBox_4.clicked.connect(self.checkbox_4_touched)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def print_values(self):

        print(self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4)
        len_password = self.lineEdit.text()
        regexPass = []
        if(self.checkbox1):
            regexPass.append('numeric')
        if(self.checkbox2):
            regexPass.append('alphalower')
        if(self.checkbox3):
            regexPass.append('alphaupper')
        if(self.checkbox4):
            regexPass.append('specialschars')
        print(regexPass)
        new_password = Password("", int(len_password))
        passw = new_password.gen_password(regexPass)
        self.message_box_creation("Mot de passe créé", passw)
        self.clipboard.setText(passw)

    def message_box_creation(self, title, text):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.exec()

    def checkbox_touched(self):
        self.checkbox1 = not self.checkbox1

    def checkbox_2_touched(self):
        self.checkbox2 = not self.checkbox2

    def checkbox_3_touched(self):
        self.checkbox3 = not self.checkbox3

    def checkbox_4_touched(self):
        self.checkbox4 = not self.checkbox4

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Generateur de mots de passe"))
        self.checkBox.setText(_translate(
            "MainWindow", "Avec des chiffres [ 0 1 2 3 4 5 6 7 8 9 ]"))
        self.checkBox_2.setText(_translate(
            "MainWindow", "Avec des lettres minuscules [ a b c ... x y z ]"))
        self.checkBox_3.setText(_translate(
            "MainWindow", " Avec des lettres majuscules [ A B C ... X Y Z ]"))
        self.checkBox_4.setText(_translate(
            "MainWindow", "Avec des caractères spéciaux [ ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . < > / ? | ]"))
        self.pushButton.setText(_translate(
            "MainWindow", "Generer le mot de passe"))
        self.label.setText(_translate(
            "MainWindow", "Gestionnaire de mots de passe"))
        self.label_2.setText(_translate("MainWindow", "Longueur"))
        self.label_3.setText(_translate("MainWindow", "max:32"))
        self.clipboard.setText(_translate(
            "MainWindow", "Le mot de passe sera affiché ici"))


if (__name__ == "__main__"):

    app = QtWidgets.QApplication(sys.argv)
    main_win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_win)

    main_win.show()
    sys.exit(app.exec_())