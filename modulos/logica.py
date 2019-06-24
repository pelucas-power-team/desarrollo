import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modulos import generico as play

class Clogica(play.Cmano):
    def __init__(self):
        super().__init__()
        self.abajo = 0
        self.arriba = 1
        self.mi_baza = None
        self.baza_out = []
        self.baza_str = []

    def flogica(self, numj, baza, dic):
        triunfo_carta = None
        triunfo_str = []
        puntos_arriba = 0
        puntos_abajo = 0

        if numj == 2:
            self.mi_baza, self.mis_puntos = self.fordenar(baza, dic, self.triunfo)
            for i in range(len(baza)):
                for j in range(len(dic[0])):
                    if baza[i] == dic[0][j]:
                        self.baza_out.append(int(dic[1][j], base=10))

            for i in range(len(dic[0])):
                if dic[0][i] == self.triunfo:
                    triunfo_carta = int(dic[1][i], base=10)

            triunfo_str.append(list(str(triunfo_carta)))

            for i in range(len(self.baza_out)):
                aux = self.baza_out[i]
                self.baza_str.append(list(str(aux)))

            if self.baza_str[0][0] == self.baza_str[1][0]:
                gana_puntos = sum(self.mis_puntos)

                if self.mi_baza[1] == baza[self.abajo]:
                     puntos_abajo += gana_puntos
                     if self.abajo == 1:
                         self.abajo = 0
                         self.arriba = 1
                         ganador = 'j2'
                         return (puntos_arriba, puntos_abajo, ganador)
                else:
                    puntos_arriba += gana_puntos
                    if self.arriba == 1:
                        self.arriba = 0
                        self.abajo = 1
                        ganador = 'j1'
                        return (puntos_arriba, puntos_abajo, ganador)
            else:
                if self.baza_str[0][0] == triunfo_str[0]:
                    gana_puntos = sum(self.mis_puntos)
                    if self.mi_baza[0] == baza[self.abajo]:
                        puntos_abajo += gana_puntos
                        if self.abajo == 1:
                            self.abajo = 0
                            self.arriba = 1
                            ganador = 'j2'
                            return (puntos_arriba, puntos_abajo, ganador)
                    else:
                        puntos_arriba += gana_puntos
                        if self.arriba == 1:
                            self.arriba = 0
                            self.abajo = 1
                            ganador = 'j1'
                            return (puntos_arriba, puntos_abajo, ganador)
                else:
                    gana_puntos = sum(self.mis_puntos)
                    if self.abajo == 0:
                        puntos_abajo += gana_puntos
                        ganador = 'j2'
                        return (puntos_arriba, puntos_abajo, ganador)
                    else:
                        puntos_arriba += gana_puntos
                        ganador = 'j1'
                        return (puntos_arriba, puntos_abajo, ganador)

