import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modulos import prueba_repartir_2j as play


def logica(self):
    triunfo = list(self.mi_baraja[12])
    palo_triunfo = triunfo[0]
    valor_triunfo = triunfo[1:2]
    # las dos siguientes hay que ponerlas en función de la carta seleccionada en la interfaz
    mi_baza_j1 = list() #es el jugador que saca primero
    mi_baza_j2 = list() #es el jugador que saca segundo
    if palo_triunfo == mi_baza_j1[0] and palo_triunfo == mi_baza_j2[0]:
        mostradas = [mi_baza_j1[1:2], mi_baza_j2[1:2]]
        gana = max(mostradas)
        ganador = [palo_triunfo, gana]
    elif palo_triunfo == mi_baza_j1[0] and palo_triunfo != mi_baza_j2[0]:
        gana = mi_baza_j1[1:2]
        ganador = [palo_triunfo,gana]
    elif palo_triunfo != mi_baza_j1[0] and palo_triunfo == mi_baza_j2[0]:
        gana = mi_baza_j2[1:2]
        ganador = [palo_triunfo, gana]
    elif palo_triunfo != mi_baza_j1[0] and palo_triunfo != mi_baza_j2[0]:
        if mi_baza_j1[0] == mi_baza_j2[0]:
            mostradas = [mi_baza_j1[1:2], mi_baza_j2[1:2]]
            gana = max(mostradas)
            ganador = [mi_baza_j1[0],gana]
        else
            ganador = mi_baza_j1



    total_jugador1 =
    total_jugador2 =

