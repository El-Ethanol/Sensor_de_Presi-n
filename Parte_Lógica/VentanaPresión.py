import serial as ser
import time
from PyQt5 import QtWidgets        
from PyQt5.QtCore import QTime, QTimer
from Parte_Gráfica.VentanaPresiónDiseño import Ui_PressureWindow
from Parte_Lógica.VentanaPrincipal import MainWindow

if MainWindow.pSerial.is_open:
    MainWindow.pSerial.close()
MainWindow.pSerial.open()
MainWindow.pSerial.flushInput()
MainWindow.pSerial.flushOutput()

class WindowPresion(QtWidgets.QMainWindow, Ui_PressureWindow): #Pressure Window
    
    def __init__(self, parent=None):
        super(WindowPresion, self).__init__(parent)
        self.setupUi(self)
        timer=QTimer(self)
        timer.timeout.connect(self.showpressure)
        timer.start(0)
        
    def showpressure(self):
        MainWindow.presion
        HoraActual=QTime.currentTime()
        Tiempo=HoraActual.toString('hh:mm:ss')
        Press=str(presion)
        self.labelp_2.setText("Hora:  " + Tiempo)
        self.labelp_3.setText("Presión:  " + Press + " Torr")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = WindowPresion()
    window.show()
    app.exec_()