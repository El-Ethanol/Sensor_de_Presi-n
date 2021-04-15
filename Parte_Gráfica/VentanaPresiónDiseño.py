#Parte Gráfica Ventana Presión.

from PyQt5 import QtCore, QtGui, QtWidgets

#Ventana Presión
class Ui_PressureWindow(object):
    
    def setupUi(self, PressureWindow): #Definición interfaz y etiquetas
        
       #Ventana Base
        PressureWindow.setObjectName("NewWindoe")
        PressureWindow.resize(410, 270)
        PressureWindow.setStyleSheet("background-color: rgb(45, 45,45); border-color: rgb(56, 56, 56);alternate-background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(PressureWindow)
        self.centralwidget.setObjectName("centralwidget")
        PressureWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PressureWindow)
        self.statusbar.setObjectName("statusbar")
        PressureWindow.setStatusBar(self.statusbar)
        
       #Título Presión Actual
        self.labelp = QtWidgets.QLabel(self.centralwidget)
        self.labelp.setGeometry(QtCore.QRect(20, 10, 368, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.labelp.setFont(font)
        self.labelp.setAutoFillBackground(False)
        self.labelp.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.labelp.setScaledContents(False)
        self.labelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelp.setObjectName("labelp")
        
       #Título Hora
        self.labelp_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelp_2.setGeometry(QtCore.QRect(40, 70, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelp_2.setFont(font)
        self.labelp_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelp_2.setObjectName("labelp_2")
        
       #Título Presión
        self.labelp_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelp_3.setGeometry(QtCore.QRect(20, 150, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelp_3.setFont(font)
        self.labelp_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelp_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelp_3.setObjectName("labelp_3")
        
       #Redirección para renombrar
        self.retranslateUi(PressureWindow)
        QtCore.QMetaObject.connectSlotsByName(PressureWindow)

    def retranslateUi(self, PressureWindow): #Renombre de etiquetas.
        _translate = QtCore.QCoreApplication.translate
        PressureWindow.setWindowTitle(_translate("PressureWindow", "Presión Actual"))
        self.labelp.setText(_translate("PressureWindow", "Presión Actual"))
        self.labelp_2.setText(_translate("PressureWindow", "Hora:  "))
        self.labelp_3.setText(_translate("PressureWindow", "Presión: Torr"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PressureWindow = QtWidgets.QMainWindow()
    ui = Ui_PressureWindow()
    ui.setupUi(PressureWindow)
    PressureWindow.show()
    sys.exit(app.exec_())

# pylint: disable-msg=E0611
# pylint: disable wildcard-import