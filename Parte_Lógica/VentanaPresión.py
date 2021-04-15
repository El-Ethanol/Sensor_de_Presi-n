from PyQt5 import QtWidgets        
from PyQt5.QtCore import QTime, QTimer
from Parte_Gráfica.VentanaPresiónDiseño import Ui_PressureWindow
from Parte_Lógica.VentanaPrincipal import MainWindow

#Ventana Presión.
class WindowPresion(QtWidgets.QMainWindow, Ui_PressureWindow):
    
    def General(self, parent=None): 
        super(WindowPresion, self).General(parent)
        
       #Importar parte gráfica
        self.setupUi(self)
        
       #Contador para actualizar presión
        timer=QTimer(self)
        timer.timeout.connect(self.showpressure)
        timer.start(0)
        
   #Actualizador de Presión    
    def showpressure(self): 
        MainWindow.presion
        HoraActual=QTime.currentTime()
        Tiempo=HoraActual.toString('hh:mm:ss')
        Press=str(MainWindow.presion)
        self.labelp_2.setText("Hora:  " + Tiempo)
        self.labelp_3.setText("Presión:  " + Press + " Torr")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = WindowPresion()
    window.show()
    app.exec_()