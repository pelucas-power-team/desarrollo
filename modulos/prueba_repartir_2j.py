import sys
import random as r
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QTransform

class Cbaraja():
    def __init__(self):
        self.__mi_baraja = [0 for i in range(40)]
        self.__mis_puntos = []
        self.__puntuables =[[108, 208, 308, 408],[109, 209, 309, 409], [110, 210, 310, 410],[13, 23, 33, 43], [11, 21, 31, 41]]
        self.__orden =[8, 9]

    def __fcrearbaraja(self):
        k = 0
        for i in range(1,5):
            for j in range(1,11):
                if j not in self.__orden:
                    self.__mi_baraja[k] = int(str(i) + str(j),base = 10)
                else:
                    self.__mi_baraja[k] = int(str(i) + str(0) + str(j),base = 10)
                k+=1
        return(self.__mi_baraja)

    def __fbarajar(self):
        self.__mi_baraja = self.__fcrearbaraja()
        r.shuffle(self.__mi_baraja)
        return(self.__mi_baraja)

    def __fpuntos(self):

        for i in range(len(self.__mi_baraja)):
            if self.__mi_baraja[i] in self.__puntuables[0]:
                self.__mis_puntos.append(2)
            elif self.__mi_baraja[i] in self.__puntuables[1]:
                self.__mis_puntos.append(3)
            elif self.__mi_baraja[i] in self.__puntuables[2]:
                self.__mis_puntos.append(4)
            elif self.__mi_baraja[i] in self.__puntuables[3]:
                self.__mis_puntos.append(10)
            elif self.__mi_baraja[i] in self.__puntuables[4]:
                self.__mis_puntos.append(11)
            else:
                self.__mis_puntos.append(0)


        return (self.__mis_puntos)

    def getBaraja(self):
        baraja = self.__fbarajar()
        puntos = self.__fpuntos()
        return (baraja, puntos)

class Cmano(Cbaraja):
    def __init__(self):
        super().__init__()
        self.baraja = []
        self.puntos = []
        self.mi_mano = []
        self.mi_mano_orden = []
        self.mis_puntos = []
        self.carta = []
        self.triunfo = None



    def frepartir(self,carp, forma,numj):
        [self.baraja, self.puntos] = self.getBaraja()
        if numj == 2:
            for i in range(12):
                mi_carta = self.baraja[i]
                self.mi_mano_orden.append(mi_carta)
                self.mis_puntos.append(self.puntos[i])
                self.carta.append(carp + str(mi_carta) + forma)
                self.mi_mano.append(QPixmap(self.carta[i]))
            self.triunfo = self.baraja[12]
        elif numj == 4:
            for i in range(24):
                mi_carta = self.baraja[i]
                self.mi_mano_orden.append(mi_carta)
                self.mis_puntos.append(self.puntos[i])
                self.carta.append(carp + str(mi_carta) + forma)
                self.mi_mano.append(QPixmap(self.carta[i]))
            self.triunfo = self.baraja[12]

        return(self.mi_mano, self.mis_puntos, self.triunfo)

class Ctriunfo():
    def __init__(self):

        self.mi_triunfo = None
        self.mi_imagen_triunfo = None

    def ftriunfo(self, carpeta, formato,triunfo ):
        self.mi_triunfo = carpeta + str(triunfo) + formato
        self.mi_imagen_triunfo = QPixmap(self.mi_triunfo)
        self.mi_imagen_triunfo = self.mi_imagen_triunfo.transformed(QTransform().rotate(90))
        return(self.mi_imagen_triunfo)

class Cdorso():
    def __init__(self):
        self.mi_dorso = None
        self.mi_imagen_dorso = None

    def fdorso(self,carpeta, formato):
        self.mi_dorso = carpeta +'0' + formato
        self.mi_imagen_dorso = QPixmap(self.mi_dorso)
        return(self.mi_imagen_dorso)