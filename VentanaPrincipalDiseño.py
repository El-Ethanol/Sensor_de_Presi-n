#Parte Gráfica de la Ventana Principal

from PyQt5 import QtCore, QtGui, QtWidgets

#Ventana Principal
class Ui_MainWindow(object):
      
   def setupUi(self, MainWindow): #Definición Interfaz y Botones
        
    #Ventana Base
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 536)
        MainWindow.setStyleSheet("background-color: rgb(45, 45,45); border-color: rgb(56, 56, 56);alternate-background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
     #Pestañas 
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 451, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabs.setFont(font)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setStyleSheet("background-color: rgb(45, 45, 45);color: rgb(255, 255, 255); selection-color: rgb(255, 255, 255); border-color: rgb(45, 45, 45);")
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabs.setIconSize(QtCore.QSize(25, 25))
        self.tabs.setElideMode(QtCore.Qt.ElideLeft)
        self.tabs.setObjectName("Tabs")
        
    #Pestaña Inicio
    
     #Nombre Pestaña
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet('QTabWidger::tab {background-color: red;}')
  
     #Organización Botones Sensor
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(46, 200, 361, 67))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
     #Botones Sensor 
        self.b1_4 = QtWidgets.QPushButton(self.layoutWidget_2) #Botón Iniciar Sensor
        self.b1_4.setStyleSheet("background-color: rgb(56, 56, 56); color: rgb(255, 255, 255);")
        self.b1_4.setObjectName("b1_4")
        self.horizontalLayout_4.addWidget(self.b1_4)
        self.b2_2 = QtWidgets.QPushButton(self.layoutWidget_2) #Botón Pausar Sensor
        self.b2_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.b2_2.setObjectName("b2_2")
        self.horizontalLayout_4.addWidget(self.b2_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.b25_2 = QtWidgets.QPushButton(self.layoutWidget_2) #Botón Reiniciar Sensor
        self.b25_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.b25_2.setObjectName("b25_2")
        self.verticalLayout_5.addWidget(self.b25_2)
     
     #Organización Botones Tiempo
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(50, 100, 351, 61))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        
     #Título Tiempo de Recolección
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(64, 64, 64, 72); color: rgb(0, 222, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
     #Botones Tiempo
        self.b1_5 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.b1_5.setStyleSheet("background-color: rgb(56, 56, 56); color: rgb(255, 255, 255);")
        self.b1_5.setObjectName("b1_5")
        self.horizontalLayout_5.addWidget(self.b1_5)
        self.b1_6 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.b1_6.setStyleSheet("background-color: rgb(56, 56, 56); color: rgb(255, 255, 255);")
        self.b1_6.setObjectName("b1_6")
        self.horizontalLayout_5.addWidget(self.b1_6)
        
     #Organización Botones de Guardado
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 410, 371, 61))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
    
     #Botones de Guardado
        self.b6_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.b6_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.b6_2.setObjectName("b6_2")
        self.horizontalLayout_6.addWidget(self.b6_2)
        self.b5_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.b5_2.setStyleSheet("background-color: rgb(56, 56, 56); color: rgb(255, 255, 255);")
        self.b5_2.setObjectName("b5_2")
        self.horizontalLayout_6.addWidget(self.b5_2)
        
     #Título Sensor de Presión
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 368, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(0, 222, 0); background-color: rgb(56, 56, 56);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
    
     #Organización Gráfica y Presión Actual
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 290, 161, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
     #Botones Gráfica y Presión Actual
        self.b3_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.b3_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.b3_2.setObjectName("b3_2")
        self.verticalLayout_4.addWidget(self.b3_2)
        self.b4_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.b4_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(56, 56, 56);")
        self.b4_2.setObjectName("b4_2")
        self.verticalLayout_4.addWidget(self.b4_2)
        
    #Pestaña Configuración

     #Nombre Pestaña
        self.tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
    
     #Grupo Puertos
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 155, 95))
        self.groupBox.setStyleSheet("background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        
      #Botones Puertos
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(True)
        self.radioButton.setObjectName("radioButton")
        
     #Grupo Guardado Automático
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(220, 30, 191, 95))
        self.groupBox_3.setStyleSheet("background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
      
       #Botón Guardado Automático
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 30, 89, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 50, 150, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setAutoRepeat(True)
                
     #Grupo Directorios
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 391, 201))
        self.groupBox_2.setStyleSheet("background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
    
      #Lineas de Entrada
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 291, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 120, 291, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
    
      #Etiquetas Líneas de Entrada
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 56, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 41, 16))
        self.label_6.setObjectName("label_6")
        
      #Botones de Selección
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(260, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabs.addTab(self.tab_2, "")
        
    #Pestaña Ayuda
  
     #Nombre Pestaña
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
     #Título más información
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
    
     #URL GitHub
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(64, 64, 64); color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        urlLink=" <a href=\"https://github.com/El-Ethanol/Sensor_de_Presion.git\"> <font color=white> GitHub </font> </a>" 
        self.label_4.setText(urlLink)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
    
     #Nombre y año
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(95, 460, 261, 20))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tabs.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_4.setBuddy(self.tabs)
        
    #Redirección para renombrar
        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


   def retranslateUi(self, MainWindow): #Función para renombrar botones, etiquetas y demás objetos.
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor de Presión"))
        self.b1_4.setText(_translate("MainWindow", "Iniciar Sensor"))
        self.b2_2.setText(_translate("MainWindow", "Pausar Sensor"))
        self.b25_2.setText(_translate("MainWindow", "Reiniciar Sensor"))
        self.label_3.setText(_translate("MainWindow", "Tiempo de recolección:"))
        self.b1_5.setText(_translate("MainWindow", "Determinado"))
        self.b1_6.setText(_translate("MainWindow", "Indeterminado"))
        self.b6_2.setText(_translate("MainWindow", "Guardar datos (.cvs)"))
        self.b5_2.setText(_translate("MainWindow", "Guardar Gráfica (.png)"))
        self.label.setText(_translate("MainWindow", "Sensor de Presión"))
        self.b3_2.setText(_translate("MainWindow", "Presión Actual"))
        self.b4_2.setText(_translate("MainWindow", "Gráfica"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Inicio"))
        self.groupBox.setTitle(_translate("MainWindow", "Puerto del Sensor:"))
        self.radioButton_3.setText(_translate("MainWindow", "TTYUSB0"))
        self.radioButton_2.setText(_translate("MainWindow", "TTYUSB1"))
        self.radioButton.setText(_translate("MainWindow", "TTYUSB2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Directorios de guardado:"))
        self.lineEdit.setText(_translate("MainWindow", "C:/home/detectores/Software/mks_control/Grafica_Presion/"))
        self.lineEdit_2.setText(_translate("MainWindow", "C:/home/detectores/Software/mks_control/Datos_Presion/"))
        self.label_5.setText(_translate("MainWindow", "Gráfica:"))
        self.label_6.setText(_translate("MainWindow", "Datos:"))
        self.pushButton.setText(_translate("MainWindow", "Seleccionar."))
        self.pushButton_2.setText(_translate("MainWindow", "Seleccionar."))
        self.groupBox_3.setTitle(_translate("MainWindow","Guardado Automático:"))
        self.radioButton_4.setText(_translate("MainWindow", "Activado"))
        self.radioButton_5.setText(_translate("MainWindow", "Desactivado"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("MainWindow", "Ayuda"))
        self.label_2.setText(_translate("MainWindow", "    Para más información:"))
        self.label_7.setText(_translate("MainWindow", "Ethan Campos Méndez, México 2021"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Configuración"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# pylint: disable-msg=E0611
# pylint: disable wildcard-import