from PyQt5 import QtWidgets        
from PyQt5.QtCore import QTime, QTimer
from Parte_Gráfica.VentanaPresiónDiseño import Ui_NewWindoe, Ui_PressureWindow
import serial as ser
import time

pSerial = ser.Serial('/dev/ttyUSB2',baudrate=9600,timeout=1)
if pSerial.is_open:
    pSerial.close()
pSerial.open()
pSerial.flushInput()
pSerial.flushOutput()
x='@249DL?;FF'

class WindowPresion(QtWidgets.QMainWindow, Ui_PressureWindow): #Pressure Window
    
    def __init__(self, parent=None):
        super(WindowPresion, self).__init__(parent)
        self.setupUi(self)
        timer=QTimer(self)
        timer.timeout.connect(self.showpressure)
        timer.start(1000)
        
    def showpressure(self):
        pSerial.write(x.encode())
        z=pSerial.read_until(b'\r')
        z=z.decode()
        s=z.split(';')
        if len(s)==1:
            pass
        else:
            a=s[1].split('\r')
            time.sleep(1)
            try:
                presion=float(a[0])
            except Exception:
                z=pSerial.read_until(b'\r')
                z=z.decode()
                s=z.split(';')
                a=s[1].split('\r')
                presion=float(a[0])
        current_time=QTime.currentTime()
        label_time=current_time.toString('hh:mm:ss')
        label_p=str(presion)
        self.Aaaaaa.setText("Hora:  "+label_time)
        self.Aaaaaa_2.setText("Presión:  "+label_p+" Torr")
    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = WindowPresion()
    window.show()
    app.exec_()