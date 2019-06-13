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
        self.player = play.play2(None)


    def fwindow(self):
        self.player.show()




"""class Window_player_4(QMainWindow, form_class_2):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.player = play.play4"""
