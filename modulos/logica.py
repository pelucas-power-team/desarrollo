import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from modulos import prueba_repartir_2j as play

def logica(self):
    triunfo = list(self.baraja[1][12])#pensando en la baraja matriz, con las 2 denominaciones y la puntuación
    palo_triunfo = triunfo[0]
    valor_triunfo = triunfo[1:2]
    # las dos siguientes hay que ponerlas en función de la carta seleccionada en la interfaz
    mi_baza_j1 = list(baza_j1) #OJO!!!! es el jugador que saca primero
    mi_baza_j2 = list(baza_j2) #OJO!!!! es el jugador que saca segundo
    puntuacion_j1=0
    puntuacion_j2=0
    puntuacion_j3=0
    puntuacion_j4=0
    if numj == 2:
        if palo_triunfo == mi_baza_j1[0] and palo_triunfo == mi_baza_j2[0]:
            mostradas = [mi_baza_j1[1:2], mi_baza_j2[1:2]]
            gana = max(mostradas)
            ganador = [palo_triunfo, gana]
            if ganador in mi_mano1:
                puntuacion_j1=puntuacion_j1+puntos(mi_baza_j1)+puntos(mi_baza_j2)
            else:
                puntuacion_j2 = puntuacion_j2 + puntos(mi_baza_j1) + puntos(mi_baza_j2)
        elif palo_triunfo == mi_baza_j1[0] and palo_triunfo != mi_baza_j2[0]:
            gana = mi_baza_j1[1:2]
            ganador = [palo_triunfo,gana]
            puntuacion_j1 = puntuacion_j1 + puntos(mi_baza_j1) + puntos(mi_baza_j2)
        elif palo_triunfo != mi_baza_j1[0] and palo_triunfo == mi_baza_j2[0]:
            gana = mi_baza_j2[1:2]
            ganador = [palo_triunfo, gana]
            puntuacion_j2 = puntuacion_j2 + puntos(mi_baza_j1) + puntos(mi_baza_j2)
        elif palo_triunfo != mi_baza_j1[0] and palo_triunfo != mi_baza_j2[0]:
            if mi_baza_j1[0] == mi_baza_j2[0]:
                mostradas = [mi_baza_j1[1:2], mi_baza_j2[1:2]]
                gana = max(mostradas)
                ganador = [mi_baza_j1[0],gana]
                if ganador in mi_mano1:
                    puntuacion_j1 = puntuacion_j1 + puntos(mi_baza_j1) + puntos(mi_baza_j2)
                else:
                    puntuacion_j2 = puntuacion_j2 + puntos(mi_baza_j1) + puntos(mi_baza_j2)
            else:
                ganador = mi_baza_j1 #¿Cómo hacemos para tener en cuenta el jugador que es mano?



    total_jugador1 =
    total_jugador2 =
