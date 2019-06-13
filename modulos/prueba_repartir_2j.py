import sys
import random as r
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QTransform

# Cargar nuestro formulario *.ui
form_play2 = uic.loadUiType("./interfaces/prueba_triunfo_2j.ui")[0]


# Crear la Clase MyWindowClass con el formulario cargado.
class play2(QMainWindow, form_play2):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.orden = [8, 9]
        self.mi_carpeta = 'BarajaEsp/'
        self.formato = '.png'
        self.mi_baraja = [1 for i in range(4) for j in range(10)]

        self.fdorso(self.formato, self.mi_carpeta)

        self.boton_repartir.clicked.connect(self.frepartir)

    def frepartir(self):
        carta = [0 for i in range(12)]
        mi_mano1 = [0 for i in range(6)]
        mi_mano2 = [0 for i in range(6)]
        carpeta = self.mi_carpeta
        formato = self.formato

        self.mi_baraja = self.desordenar()

        for i in range(12):
            mi_carta = self.mi_baraja[i]
            carta[i] = carpeta + str(mi_carta) + formato
            if  i < 6 :
                mi_mano1[i] = QPixmap(carta[i])
            else:
                mi_mano2[i-6] = QPixmap(carta[i])

        self.carta_1.setPixmap(mi_mano1[0])
        self.carta_2.setPixmap(mi_mano1[1])
        self.carta_3.setPixmap(mi_mano1[2])
        self.carta_4.setPixmap(mi_mano1[3])
        self.carta_5.setPixmap(mi_mano1[4])
        self.carta_6.setPixmap(mi_mano1[5])
        self.carta_21.setPixmap(mi_mano2[0])
        self.carta_22.setPixmap(mi_mano2[1])
        self.carta_23.setPixmap(mi_mano2[2])
        self.carta_24.setPixmap(mi_mano2[3])
        self.carta_25.setPixmap(mi_mano2[4])
        self.carta_26.setPixmap(mi_mano2[5])

        self.ftriunfo(self.formato, self.mi_carpeta, self.mi_baraja[12])

    def fdorso(self, formato, carpeta):

        mi_dorso = carpeta + '0' + formato
        mi_imagen_dorso = QPixmap(mi_dorso)
        self.mazo.setPixmap(mi_imagen_dorso)

    def ftriunfo(self, formato, carpeta, carta):
        mi_triunfo = carpeta + str(carta) + formato
        mi_imagen_triunfo = QPixmap(mi_triunfo)
        mi_imagen_triunfo = mi_imagen_triunfo.transformed(QTransform().rotate(90))
        self.triunfo.setPixmap(mi_imagen_triunfo)

    def desordenar(self):
        k = 0
        for i in range(1,5):
            for j in range(1,11):
                if j not in self.orden:
                    self.mi_baraja[k] = str(i) + str(j)
                else:
                    self.mi_baraja[k] = str(i) + str(0) + str(j)
                k += 1
        r.shuffle(self.mi_baraja)
        return  self.mi_baraja


"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()"""