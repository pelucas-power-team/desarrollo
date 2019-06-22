import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modulos import generico as play.Cmano

class Clogica(Cmano):
    def __init__(self):
        super().__init__()
        self.baza = []
        if numj == 2:

            self.mi_baza, self.mis_puntos = self.fordenar(self.baza, self.dic, self.triunfo)
            for i in range(len(mi_baza)):
                for j in range(len(dic[0])):
                    if mi_baza[i] == dic[j]:
                        baza_out.append(int(dic[1][j], base=10))

            for i in range(len(ref_global[0])):
                if ref_global[0][i] == triunfo:
                    triunfo_carta = int(ref_global[1][i], base=10)

            triunfo_str = list(str(triunfo_carta))

            for i in range(len(baza_out)):
                aux = baza_out[i]
                baza_str.append(list(str(aux)))

            if baza_str[0][0] == baza_str[1][0]:
                gana_puntos = mis_puntos[1]
                if mi_baza[1] == baza[0]:

                else:
            else:
                if baza_str[0][0] == triunfo_str[0]:
                    gana_puntos = mis_puntos[0]
                else:
                    if baza[0] == mi_baza[0]:
                        gana_puntos = mis_puntos[0]
                    else:
                        gana_puntos = mis_puntos[1]







    total_jugador1 =
    total_jugador2 =
