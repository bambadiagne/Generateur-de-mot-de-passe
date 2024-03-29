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


class PasswordWidget(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        self.checkbox1 = False
        self.checkbox2 = False
        self.checkbox3 = False
        self.checkbox4 = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(90, 150, 301, 31))
        self.checkBox.setStyleSheet("QCheckBox\n"
                                    "{\n"
                                    "font-size: 13px;\n"
                                    "font-weight: bold;\n"
                                    "height: 30px;\n"
                                    " margin-left: 5px;\n"
                                    "width: 100px;\n"
                                    "height: 50px;\n"
                                    "font-family: Georgia, serif;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QCheckBox::indicator {\n"
                                    "    width: 20px;\n"
                                    "    height: 20px;\n"
                                    "}\n"
                                    "QCheckBox::hover {\n"
                                    "    color:rgb(114, 255, 243);\n"
                                    "}")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 190, 341, 21))
        self.checkBox_2.setStyleSheet("QCheckBox\n"
                                      "{\n"
                                      "font-size: 13px;\n"
                                      "font-weight: bold;\n"
                                      "height: 30px;\n"
                                      " margin-left: 5px;\n"
                                      "width: 100px;\n"
                                      "height: 50px;\n"
                                      "font-family: Georgia, serif;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QCheckBox::indicator {\n"
                                      "    width: 20px;\n"
                                      "    height: 20px;\n"
                                      "}\n"
                                      "QCheckBox::hover {\n"
                                      "    color:rgb(114, 255, 243);\n"
                                      "}")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 220, 361, 21))
        self.checkBox_3.setStyleSheet("QCheckBox\n"
                                      "{\n"
                                      "font-size: 13px;\n"
                                      "font-weight: bold;\n"
                                      "height: 30px;\n"
                                      " margin-left: 5px;\n"
                                      "width: 100px;\n"
                                      "height: 50px;\n"
                                      "font-family: Georgia, serif;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QCheckBox::indicator {\n"
                                      "    width: 20px;\n"
                                      "    height: 20px;\n"
                                      "}\n"
                                      "QCheckBox::hover {\n"
                                      "    color:rgb(114, 255, 243);\n"
                                      "}")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 250, 551, 21))
        self.checkBox_4.setStyleSheet("QCheckBox\n"
                                      "{\n"
                                      "font-size: 13px;\n"
                                      "font-weight: bold;\n"
                                      "height: 30px;\n"
                                      " margin-left: 5px;\n"
                                      "width: 100px;\n"
                                      "height: 50px;\n"
                                      "font-family: Georgia, serif;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QCheckBox::indicator {\n"
                                      "    width: 20px;\n"
                                      "    height: 20px;\n"
                                      "}\n"
                                      "QCheckBox::hover {\n"
                                      "    color:rgb(114, 255, 243);\n"
                                      "}")
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 340, 451, 41))
        self.pushButton.setStyleSheet("\n"
                                      "QPushButton{\n"
                                      "  display: block;\n"
                                      "  width: 200px;\n"
                                      "  height: 40px;\n"
                                      "  line-height: 40px;\n"
                                      "  font-size: 18px;\n"
                                      "  font-family:sans-serif;\n"
                                      "  text-decoration: none;\n"
                                      "  color: #333;\n"
                                      "  border: 2px solid #333;\n"
                                      "  letter-spacing: 2px;\n"
                                      "  text-align: center;\n"
                                      "  position: relative;\n"
                                      "  transition: all .35s;\n"
                                      "  border-radius:10px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QPushButton::after{\n"
                                      "  position: absolute;\n"
                                      "  content: \"\";\n"
                                      "  top: 0;\n"
                                      "  left: 0;\n"
                                      "  width: 0;\n"
                                      "  height: 100%;\n"
                                      "  background: #ff003b;\n"
                                      "  transition: all .35s;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover{\n"
                                      "  color: #fff;\n"
                                      "  background: rgb(114, 255, 243);\n"
                                      "  \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover::after{\n"
                                      "  width: 100%;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 451, 31))
        self.label.setStyleSheet("QLabel{\n"
                                 "font-family: Georgia, serif;\n"
                                 "font-size:30px;\n"
                                 "font-style:bold;\n"
                                 "color:rgb(114, 255, 243);\n"
                                 "}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 300, 191, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 57, 15))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font-family:Georgia, serif;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 410, 256, 101))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.clear(mode=self.clipboard.Clipboard)
        self.clipboard.setObjectName("clipboard")
        self.pushButton.clicked.connect(self.print_values)
        self.checkBox.clicked.connect(self.checkbox_touched)
        self.checkBox_2.clicked.connect(self.checkbox_2_touched)
        self.checkBox_3.clicked.connect(self.checkbox_3_touched)
        self.checkBox_4.clicked.connect(self.checkbox_4_touched)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 300, 57, 15))
        self.label_5.setObjectName("label_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def print_values(self):

        len_password = self.lineEdit.text()

        regex_pass = []
        if(self.checkbox1):
            regex_pass.append('numeric')
        if(self.checkbox2):
            regex_pass.append('alphalower')
        if(self.checkbox3):
            regex_pass.append('alphaupper')
        if(self.checkbox4):
            regex_pass.append('specialschars')

        if(not regex_pass):
            self.message_box_creation(
                "Erreur", "Veuillez cocher une ou plusieurs cases")

        elif(len_password.isdigit()):
            len_password = int(len_password)
            self.listWidget.clear()
            if(len_password > 0):
                new_password = Password("", int(len_password))
                passw = new_password.gen_password(regex_pass)
                self.listWidget.addItem(
                    QtWidgets.QListWidgetItem(passw, self.listWidget))
                self.message_box_creation(
                    "Mot de passe créé", "Copié dans le presse papier")
                self.clipboard.setText(passw)

            else:
                self.message_box_creation(
                    "Erreur", "Entrez un entier supérieur à 0")

        elif((not len_password.isdigit() and len_password.isalnum()) or len_password == ""):

            self.message_box_creation("Erreur", "Veuillez entrer un nombre")

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
        self.label_5.setText(_translate("MainWindow", ""))


def show():

    main_win = QtWidgets.QMainWindow()
    ui = PasswordWidget()
    ui.setupUi(main_win)
    main_win.show()
