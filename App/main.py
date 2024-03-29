# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui.password_ui import PasswordWidget
from ui.crack_ui import CrackWidget


class AppMainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 360, 301, 51))
        self.pushButton.setStyleSheet("\n"
                                      "QPushButton{\n"
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 360, 291, 51))
        self.pushButton_2.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "  width: 200px;\n"
                                        "  height: 40px;\n"
                                        "  line-height: 40px;\n"
                                        "  font-size: 18px;\n"
                                        "  font-family: sans-serif;\n"
                                        "  text-decoration: none;\n"
                                        "  color: #333;\n"
                                        "  border: 2px solid #333;\n"
                                        "  letter-spacing: 2px;\n"
                                        "  text-align: center;\n"
                                        "  position: relative;\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 571, 41))
        self.label.setStyleSheet("font: 20pt \"Lucida Calligraphy\";\n"
                                 "\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 201, 211))
        self.label_2.setObjectName("label_2")
        pixMap = QtGui.QPixmap("probleme.png")
        self.label_2.setPixmap(pixMap)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.window2 = PasswordWidget()
        self.genpassword = QtWidgets.QMainWindow()
        self.window2.setupUi(self.genpassword)
        self.pushButton.clicked.connect(self.show_gen_password)

        self.window3 = CrackWidget()
        self.crack_password_ui = QtWidgets.QMainWindow()
        self.window3.setupUi(self.crack_password_ui)
        self.pushButton_2.clicked.connect(self.show_crack_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate(
            "MainWindow", "generateur de mot de passe"))
        self.pushButton_2.setText(_translate(
            "MainWindow", "cracker de mot de passe"))
        self.label.setText(_translate(
            "MainWindow", "Application de gestion de mots de passe"))

    def show_gen_password(self):
        self.genpassword.show()

    def show_crack_widget(self):
        self.crack_password_ui.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_win = QtWidgets.QMainWindow()
    ui = AppMainWindow()
    ui.setupUi(main_win)
    main_win.show()
    sys.exit(app.exec_())


if (__name__ == "__main__"):
    main()
