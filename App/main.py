# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets, uic


import sys
# sys.path.append("C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\Generateur-de-mot-de-passe\\App\\classes")
from classes.password import Password


class Window():

    def __init__(self):
        self.checkbox1 = False
        self.checkbox2 = False
        self.checkbox3 = False
        self.checkbox4 = False

    def print_values(self):

        if(self.checkbox1 and self.checkbox2 and self.checkbox3 and self.checkbox4):
            new_password = Password("alphanum")
            print(new_password.gen_password())

    def checkbox_touched(self):
        self.checkbox1 = not self.checkbox1

    def checkbox_2_touched(self):
        self.checkbox2 = not self.checkbox2

    def checkbox_3_touched(self):
        self.checkbox3 = not self.checkbox3

    def checkbox_4_touched(self):
        self.checkbox4 = not self.checkbox4


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    call = uic.loadUi("ui/app.ui")
    win = Window()
    call.pushButton.clicked.connect(win.print_values)
    call.checkBox.clicked.connect(win.checkbox_touched)
    call.checkBox_2.clicked.connect(win.checkbox_2_touched)
    call.checkBox_3.clicked.connect(win.checkbox_3_touched)
    call.checkBox_4.clicked.connect(win.checkbox_4_touched)
    call.show()
    app.exec()
