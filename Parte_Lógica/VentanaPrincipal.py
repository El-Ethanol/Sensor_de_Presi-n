# pylint: disable-msg=E0611
# pylint: disable wildcard-import
import time
import pyqtgraph as pg
import pyqtgraph.exporters
import pandas as pd 
import serial as ser
import os
from Parte_Gráfica.VentanaPresiónDiseño import WindowPresion
from PyQt5 import QtWidgets        
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QMessageBox, QAction
from pyqtgraph.Qt import QtGui
from Parte_Lógica.VentanaPresión import Ui_MainWindow


pSerial = ser.Serial('/dev/ttyUSB2',baudrate=9600,timeout=1)
if pSerial.is_open:
    pSerial.close()
pSerial.open()
pSerial.flushInput()
pSerial.flushOutput()
x='@249DL?;FF'
y=[]
Xm = []    
ptr = 0
t=[]

class MainWindow1(QtWidgets.QMainWindow, Ui_MainWindow): #Main Window
     
      stop_signal = pyqtSignal()
     
      def __init__(self, parent=None):
         super(MainWindow1, self).__init__(parent)
         self.setupUi(self)
         self.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 35, 35);") 
         self.count = 0
         self.data1=[]
         self.data2=[]
         self.start = False
         timer1 = QTimer(self)
         timer1.timeout.connect(self.showTime)
         timer1.start(100)

      # Sensor Buttons:
         self.b1.clicked.connect(self.start_action)#Iniciar Sensor
         self.b25.clicked.connect(self.reset_action)#Reiniciar Sensor
         self.b2.clicked.connect(self.pause_action)#Detener Sensor
        
      #Other buttons  
         self.b3.clicked.connect(self.presionventana)#Presión Actual
         self.b4.clicked.connect(self.grafventana)#Gráfica
         self.b5.clicked.connect(self.guardarg)#Guardar Gráfica
         self.b6.clicked.connect(self.guardard)#Guardar Datos
         self.b1_2.clicked.connect(self.determinado)#Determinado
         self.b1_3.clicked.connect(self.indeterminado)#Indeterminado
        
         quit = QAction("Quit", self)#Close
         quit.triggered.connect(self.closeEvent)
         

         self.show()

    # Definitions
    
      def showTime(self):
         global presion, tabla, y, Xm, t, ptr
         if self.start:
            z=pSerial.read_until(b'\r')
            z=z.decode()
            s=z.split(';')
            a=s[1].split('\r')
            presion=float(a[0]) 
            if len(s)==1:
               pass
            else:
               a=s[1].split('\r')
               now=time.strftime("%X")
               time.sleep(1)
            try:
               presion=float(a[0])
            except Exception:
               z=pSerial.read_until(b'\r')
               z=z.decode()
               s=z.split(';')
               a=s[1].split('\r')
               presion=float(a[0])
            self.count = self.count+1
            y.append((now,presion))
            tabla=pd.DataFrame(y,columns=['Hora','Presión']) 
            print(tabla)
            t.append(ptr)
            Xm.append(presion)
            ptr=ptr+1
            if self.count == tiempo1:
               self.start = False
            else:
               pass
               
                
      def start_action(self):
         self.start = True

         if pSerial.is_open:
           pSerial.close()

         pSerial.open()
         pSerial.flushInput()
         pSerial.flushOutput()
         pSerial.write(x.encode())

         if self.count == tiempo1:
           self.start = False
  
      def pause_action(self):
         self.start = False
  
      def reset_action(self):
         self.start = False
         self.count = 0
          
      def presionventana(self):
         self.window = QtWidgets.QMainWindow()
         self.ui1 = WindowPresion()
         self.ui1.setupUi(self.window)
         self.window.show()
     
      def grafventana(self):
         self.win=pg.GraphicsWindow()
         self.win.setWindowTitle("Gráfica")
         self.layout = QtGui.QGridLayout()
         self.layout.setParent(self.win)
         self.win.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 35, 35);") 

         self.curve=pg.PlotWidget()
         self.win.setLayout(self.layout)

         self.saveBtn = QtGui.QPushButton("Gráfica Actual")
         self.saveBtn.setParent(self.win)
         self.saveBtn.show()

         self.stopBtn = QtGui.QPushButton("Detener")
         self.stopBtn.setParent(self.win)
         self.stopBtn.show()

         self.layout.addWidget(self.saveBtn, 1, 0)
         self.layout.addWidget(self.stopBtn, 2, 0)
         self.layout.addWidget(self.curve, 0, 3, 2, 3 )

         self.saveBtn.clicked.connect(self.iniciog)
         self.stopBtn.clicked.connect(self.pausarg)

         self.curve.plot(t,Xm,pen=pg.mkPen('r', width=2))
         self.curve.setLabel(axis='left', text='Presión (Torr)')
         self.curve.setLabel(axis='bottom', text='Tiempo (s)')                
         pg.mkColor('r')
         if len(y)>11:
            self.curve.setXRange(len(y)-11,len(y)-1,padding=0)
         else: pass                    
         self.curve.setPos(0,0)

         self.startg = False
         timerg = QTimer(self)
         timerg.timeout.connect(self.updater)
         timerg.start(100)

         self.win.show()

      def iniciog(self):
         self.startg=True

      def pausarg(self):
         self.startg=False
      
      def updater(self):
         if self.startg:
            self.curve.plot(t,Xm,pen=pg.mkPen('r', width=2))
            if len(y)>11:
              self.curve.setXRange(len(y)-11,len(y)-1,padding=0)
            else: pass                   

      def grafventana1(self):
         self.dialog.show()
          
      def determinado(self):
         global tiempo1,tiempo2
         text= QtWidgets.QInputDialog.getText(self, 'Tiempo...', '¿Cuántos segundos?:')   
         if text[1]:
            tiempo = text[0]
         tiempo1=float(tiempo)
         tiempo2=False
         
      def indeterminado(self):
         global tiempo1, tiempo2
         tiempo2=True
         tiempo1=-1

          
      def closeEvent(self,event):
          close = QMessageBox()
          close.setWindowTitle("Salir...")
          close.setText("¿Deseas salir?")
          close.setIcon(QMessageBox.Question)
          close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
          close.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(64, 64, 64);")
          close = close.exec()

          if close == QMessageBox.Yes:
             event.accept()
          else:
             event.ignore()
             
      def guardard(self):
         text= QtWidgets.QInputDialog.getText(self, 'Guardar Como:', 'Guardar Como:')   
         if text[1]:
            nombre = text[0] + ".csv"
            tabla.to_csv(r'/home/detectores/Software/mks_control/Datos_Presion/datos1.csv',index=False)
            path="/home/detectores/Software/mks_control/Datos_Presion/"+ nombre
            os.rename("/home/detectores/Software/mks_control/Datos_Presion/datos1.csv",path)
             
      def guardarg(self):
         text= QtWidgets.QInputDialog.getText(self, 'Guardar Como:', 'Guardar Como:')   
         if text[1]:
            nombre = text[0] + ".png"
            path="/home/detectores/Software/mks_control/Graficas_Presion/"+nombre
            exporter = pg.exporters.ImageExporter(self.curve.plotItem)
            exporter.export(path)
           
        
if __name__ == "__main__":
   app = QtWidgets.QApplication([])
   window = MainWindow1()
   window.show()
   app.exec_()
   
# pylint: disable-msg=E0611
# pylint: disable wildcard-import