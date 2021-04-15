#Parte Lógica de la Ventana Principal

import time
import pyqtgraph as pg
import pyqtgraph.exporters
import pandas as pd 
import serial as ser
import os
from Parte_Gráfica.VentanaPresiónDiseño import WindowPresion
from Parte_Lógica.VentanaPresión import Ui_MainWindow
from PyQt5 import QtWidgets        
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QAction
from pyqtgraph.Qt import QtGui

#Ventana Principal
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): #Main Window
     
      def __init__(self, parent=None):
         super(MainWindow, self).__init__(parent)
         
        #Diseño
         self.setupUi(self)
         self.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 35, 35);") 
         
        #Variables
         self.count = 0
         self.commando='@249DL?;FF'
         self.TP=[]
         self.t=[]
         self.DatosGraf=[]
         self.paso=0
         self.start = False
         
        #Cerrar puerto y borrar caché
         if self.pSerial.is_open:
            self.pSerial.close()
         self.pSerial.open()
         self.pSerial.flushInput()
         self.pSerial.flushOutput()
         
        #Temporizador
         timer1 = QTimer(self)
         timer1.timeout.connect(self.Datos)
         timer1.start(100)
      
      #Botones
        #Botones Sensor
         self.b1_4.clicked.connect(self.start_action)#Iniciar Sensor
         self.b25_2.clicked.connect(self.reset_action)#Reiniciar Sensor
         self.b2_2.clicked.connect(self.pause_action)#Detener Sensor
        
        #Botones Tiempo
         self.b1_5.clicked.connect(self.T_Determinado)#Determinado
         self.b1_6.clicked.connect(self.T_Indeterminado)#Indeterminado      

        #Botones Guardado
         self.b5_2.clicked.connect(self.guardarg)#Guardar Gráfica
         self.b6_2.clicked.connect(self.guardard)#Guardar Datos
        
        #Botones Pres y Graf
         self.b3_2.clicked.connect(self.presionventana)#Presión Actual
         self.b4_2.clicked.connect(self.grafventana)#Gráfica
        
        #Botones Puertos
         self.radioButton.toggled.connect(self.BotonSelec)#TTYUSB0
         self.radioButton_2.toggled.connect(self.BotonSelec)#TTYUSB1
         self.radioButton_3.toggled.connect(self.BotonSelec)#TTYUSB2
         
        #Botones Selección
         self.pushButton.connect(self.OpenFileDatos)#Seleccion Datos
         self.pushButton_2.connect(self.OpenFileGraf)#Seleccion Graf
         
        #Botones Cerrar
         quit = QAction("Quit", self)#Close
         quit.triggered.connect(self.closeEvent)

         self.show()

 #Funciones ligadas a los botones
    
     #Funciones para elegir ruta
      def OpeFileDatos(self):
          fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
          self.lineEdit.setText("fileName")
      
      def OpeFileGraf(self):
          fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
          self.lineEdit_2.setText("fileName")
      
     #Funcion para elegir puerto 
      def BotonSelec(self):
          if self.radioButton.isChecked():
              self.pSerial = ser.Serial('/dev/ttyUSB0',baudrate=9600,timeout=1)
          elif self.radioButton_2.isChecked():
              self.pSerial = ser.Serial('/dev/ttyUSB1',baudrate=9600,timeout=1)
          elif self.radioButton_2.isChecked():
              self.pSerial = ser.Serial('/dev/ttyUSB2',baudrate=9600,timeout=1)
     
     #Funcion obtención de datos             
      def Datos(self):
         global tabla
         if self.start:
            z=self.pSerial.read_until(b'\r')
            z=z.decode()
            s=z.split(';')
            a=s[1].split('\r')
            self.presion=float(a[0]) 
            if len(s)==1:
               pass
            else:
               a=s[1].split('\r')
               now=time.strftime("%X")
               time.sleep(1)
            try:
               self.presion=float(a[0])
            except Exception:
               z=self.pSerial.read_until(b'\r')
               z=z.decode()
               s=z.split(';')
               a=s[1].split('\r')
               self.presion=float(a[0])
            self.count = self.count+1
            self.TP.append((now,self.presion))
            tabla=pd.DataFrame(self.TP,columns=['Hora','Presión']) 
            self.t.append(self.paso)
            self.DatosGraf.append(self.presion)
            self.paso=self.paso+1
            if self.count == tiempo1:
               self.start = False
            else:
               pass
               
     #Botones Iniciar, Pausar, Reiniciar          
      
      def start_action(self):
         self.start = True
         if self.pSerial.is_open:
           self.pSerial.close()
         self.pSerial.open()
         self.pSerial.flushInput()
         self.pSerial.flushOutput()
         self.pSerial.write(self.commando.encode())
         if self.count == tiempo1:
           self.start = False
  
      def pause_action(self):
         self.start = False
  
      def reset_action(self):
         self.start = False
         self.count = 0
         
     #Funcion ventana presion
      
      def presionventana(self):
         self.window = QtWidgets.QMainWindow()
         self.ui1 = WindowPresion()
         self.ui1.setupUi(self.window)
         self.window.show()
     
     #Funciones ventana grafica
      def grafventana(self):
          
       #Diseño ventana
         self.win=pg.GraphicsWindow()
         self.win.setWindowTitle("Gráfica")
         self.layout = QtGui.QGridLayout()
         self.layout.setParent(self.win)
         self.win.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(35, 35, 35);") 
        
       #Grafica datos
         self.curve=pg.PlotWidget()
         self.win.setLayout(self.layout)

       #Botones 
         self.startBtn = QtGui.QPushButton("Gráfica Actual") #Botón iniciar gráfica.
         self.startBtn.setParent(self.win)
         self.startBtn.show()

         self.stopBtn = QtGui.QPushButton("Detener") #Botón detener gráfica.
         self.stopBtn.setParent(self.win)
         self.stopBtn.show()

        #Organización botones     
         self.layout.addWidget(self.startBtn, 1, 0)
         self.layout.addWidget(self.stopBtn, 2, 0)
         self.layout.addWidget(self.curve, 0, 3, 2, 3 )

        #Conexión botones
         self.startBtn.clicked.connect(self.Inicio_G)
         self.stopBtn.clicked.connect(self.Pausar_G)
        
       #Gráfica y diseño
         self.curve.plot(self.t,self.DatosGraf,pen=pg.mkPen('r', width=2))
         self.curve.setLabel(axis='left', text='Presión (Torr)')
         self.curve.setLabel(axis='bottom', text='Tiempo (s)')                
         pg.mkColor('r')
         
        #Rango del eje x
         if len(self.TP)>11:
            self.curve.setXRange(len(self.TP)-11,len(self.TP)-1,padding=0)
         else: 
             pass                    
         self.curve.setPos(0,0)

       #Contador para auto-actualizar
         self.startg = False
         timerg = QTimer(self)
         timerg.timeout.connect(self.Actualizador)
         timerg.start(100)

         self.win.show()

     #Funciones de los botones de las gráfica
      def Inicio_G(self):
         self.startg=True

      def Pausar_G(self):
         self.startg=False
      
      def Actualizador(self):
         if self.startg:
            self.curve.plot(self.t,self.DatosGraf,pen=pg.mkPen('r', width=2))
            if len(self.TP)>11:
              self.curve.setXRange(len(self.TP)-11,len(self.TP)-1,padding=0)
            else: 
                pass                  
        
     #Funciones para determinar el tiempo
      def T_Determinado(self):
         global tiempo1,tiempo2
         text= QtWidgets.QInputDialog.getText(self, 'Tiempo...', '¿Cuántos segundos?:')   
         if text[1]:
            tiempo = text[0]
         tiempo1=float(tiempo)
         tiempo2=False
         
      def T_Indeterminado(self):
         global tiempo1, tiempo2
         tiempo2=True
         tiempo1=-1
          
     #Cerrar ventana
      def closeEvent(self,event):
         #Diseño ventana 
          self.close = QMessageBox()
          self.close.setWindowTitle("Salir...")
          self.close.setText("¿Deseas salir?")
          self.close.setIcon(QMessageBox.Question)
          self.close.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
          self.close.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(64, 64, 64);")
          self.close = self.close.exec()

         #Acciones
          if self.close == QMessageBox.Yes:
             event.accept()
          else:
             event.ignore()
             
     #Guardado datos y graf
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
   window = MainWindow()
   window.show()
   app.exec_()
   
# pylint: disable-msg=E0611
# pylint: disable wildcard-import