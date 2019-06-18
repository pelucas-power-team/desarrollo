import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modulos import prueba_repartir_2j as play

# Cargar nuestro formulario *.ui
form_class_1 = uic.loadUiType("./interfaces/prueba_triunfo_2j.ui")[0]
#form_class_2 = uic.loadUiType("prueba_triunfo_4.ui")[0]

# Crear la Clase MyWindowClass con el formulario cargado.
class Window_player_2(QMainWindow, form_class_1):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.carpeta = 'BarajaEsp/'
        self.formato = '.png'
        self.mi_mano = []
        self.mis_puntos = []
        self.mano = None
        self.triunfo = None
        self.mi_triunfo = None
        self.mazo = None
        self.boton_repartir.clicked.connect(self.fcargarmano)

    def fcargarmano(self):
        self.mano = play.Cmano()
        self.triunfo = play.Ctriunfo()
        self.mazo = play.Cdorso()

        img_dorso = self.mazo.fdorso(self.carpeta,self.formato)
        self.i_mazo.setPixmap(img_dorso)

        [self.mi_mano, self.mis_puntos,self.mi_triunfo] = self.mano.frepartir(self.carpeta, self.formato,2)
        img_triunfo = self.triunfo.ftriunfo(self.carpeta, self.formato, self.mi_triunfo)
        self.i_triunfo.setPixmap(img_triunfo)

        self.carta_1.setPixmap(self.mi_mano[0])
        self.carta_2.setPixmap(self.mi_mano[1])
        self.carta_3.setPixmap(self.mi_mano[2])
        self.carta_4.setPixmap(self.mi_mano[3])
        self.carta_5.setPixmap(self.mi_mano[4])
        self.carta_6.setPixmap(self.mi_mano[5])
        self.carta_21.setPixmap(img_dorso)
        self.carta_22.setPixmap(img_dorso)
        self.carta_23.setPixmap(img_dorso)
        self.carta_24.setPixmap(img_dorso)
        self.carta_25.setPixmap(img_dorso)
        self.carta_26.setPixmap(img_dorso)






"""class Window_player_4(QMainWindow, form_class_2):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.player = play.play4"""
