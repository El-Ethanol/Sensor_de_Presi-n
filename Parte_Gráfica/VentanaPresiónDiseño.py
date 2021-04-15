# pylint: disable-msg=E0611
# pylint: disable wildcard-import

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewWindoe(object):
    def setupUi(self, NewWindoe):
        NewWindoe.setObjectName("NewWindoe")
        NewWindoe.resize(408, 271)
        NewWindoe.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(NewWindoe)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 368, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(56, 56, 56);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Aaaaaa = QtWidgets.QLabel(self.centralwidget)
        self.Aaaaaa.setGeometry(QtCore.QRect(40, 70, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Aaaaaa.setFont(font)
        self.Aaaaaa.setStyleSheet("color: rgb(255, 255, 255);")
        self.Aaaaaa.setAlignment(QtCore.Qt.AlignCenter)
        self.Aaaaaa.setObjectName("Aaaaaa")
        self.Aaaaaa_2 = QtWidgets.QLabel(self.centralwidget)
        self.Aaaaaa_2.setGeometry(QtCore.QRect(20, 150, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Aaaaaa_2.setFont(font)
        self.Aaaaaa_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Aaaaaa_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Aaaaaa_2.setObjectName("Aaaaaa_2")
        NewWindoe.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewWindoe)
        self.statusbar.setObjectName("statusbar")
        NewWindoe.setStatusBar(self.statusbar)

        self.retranslateUi(NewWindoe)
        QtCore.QMetaObject.connectSlotsByName(NewWindoe)

    def retranslateUi(self, NewWindoe):
        _translate = QtCore.QCoreApplication.translate
        NewWindoe.setWindowTitle(_translate("NewWindoe", "Presión Actual"))
        self.label.setText(_translate("NewWindoe", "Presión Actual"))
        self.Aaaaaa.setText(_translate("NewWindoe", "Hora:  "))
        self.Aaaaaa_2.setText(_translate("NewWindoe", "Presión: Torr"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewWindoe = QtWidgets.QMainWindow()
    ui = Ui_NewWindoe()
    ui.setupUi(NewWindoe)
    NewWindoe.show()
    sys.exit(app.exec_())
