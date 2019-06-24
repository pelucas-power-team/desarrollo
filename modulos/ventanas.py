import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from modulos import generico as play
from modulos import logica as log

# Cargar nuestro formulario *.ui
form_class_1 = uic.loadUiType("./interfaces/prueba_triunfo_2j.ui")[0]
#form_class_2 = uic.loadUiType("./interfaces/prueba_triunfo_4.ui")[0]

# Crear la Clase MyWindowClass con el formulario cargado.
class Window_player_2(QMainWindow, form_class_1):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.botones = [self.carta_1, self.carta_2, self.carta_3, self.carta_4, self.carta_5, self.carta_6]
        self.icono = './interfaces/icono.png'
        self.icono_transparente = './interfaces/iconot.png'
        self.carpeta = 'BarajaEsp/'
        self.formato = '.png'
        self.baraja = []
        self.mi_mano1 = []
        self.mi_mano1_num = []
        self.mi_mano2 = []
        self.mi_mano2_num = []
        self.puntos_j1_num = 0
        self.puntos_j2_num = 0
        self.mis_puntos1 = []
        self.mis_puntos2 = []
        self.mano = None
        self.una_baza = None
        self.triunfo = None
        self.mi_triunfo = None
        self.mazo = None
        self.dic = None
        self.carta_j1 = None
        self.carta_j2 = None
        self.num_player = 2
        self.num_bazas = 20
        self.carta_borrar = None
        self.fcargarbotones(self.botones,self.icono)
        self.mi_senal = QtCore.pyqtSignal(int)
        self.logica = None
        self.carta_sel1 = None
        self.carta_sel2 = None
        self.carta_sel1_num = None
        self.carta_sel2_num = None
        self.baza_num = [None, None]
        self.boton_repartir.clicked.connect(self.frepartir)
        self.botones[0].clicked.connect(self.ftirada)
        self.botones[1].clicked.connect(self.ftirada)
        self.botones[2].clicked.connect(self.ftirada)
        self.botones[3].clicked.connect(self.ftirada)
        self.botones[4].clicked.connect(self.ftirada)
        self.botones[5].clicked.connect(self.ftirada)
        self.boton_turno.clicked.connect(self.fcambiojugador)
        self.boton_baza.clicked.connect(self.fbaza)

    def freiniciarbotones(self):
        for i in range(len(self.botones)):
            self.botones[i].setChecked(False)

    def fcarta(self,i,j,mano):
        cartas = play.Cbotones()
        cartas.fcartas(self.botones[i],self.icono, mano[j], self.i_carta_j1)

    def fcargarbotones(self,nombres,icono):
        cartas = play.Cbotones()
        if len(icono) == 22:
            for i in range(len(nombres)):
                cartas.ficonos(nombres[i],icono)
        else:
            for i in range(len(nombres)):
                cartas.ficonos(nombres[i],icono[i])

    def frepartir(self):
        self.mano = play.Cmano()
        self.triunfo = play.Ctriunfo()
        self.mazo = play.Cdorso()
        self.cartas = play.Cbotones()

        self.mi_mano1, self.mi_mano1_num,\
        self.mi_mano2, self.mi_mano2_num,\
        self.mis_puntos1, self.mis_puntos2,\
        self.mi_triunfo, self.dic, self.baraja = self.mano.frepartir(self.carpeta, self.formato,self.num_player)

        self.fmostar(self.mi_mano1,self.mi_triunfo,self.carpeta,self.formato)

    def fmostar(self, mano, triunfo, carpeta, formato):
        img_dorso = self.mazo.fdorso(carpeta, formato)
        self.i_mazo.setPixmap(img_dorso)
        img_triunfo = self.triunfo.ftriunfo(carpeta, formato, triunfo)
        self.i_triunfo.setPixmap(img_triunfo)

        self.fcargarbotones(self.botones, mano)
        self.carta_21.setPixmap(img_dorso)
        self.carta_22.setPixmap(img_dorso)
        self.carta_23.setPixmap(img_dorso)
        self.carta_24.setPixmap(img_dorso)
        self.carta_25.setPixmap(img_dorso)
        self.carta_26.setPixmap(img_dorso)

    def ftirada(self):
        k = None
        if self.botones[0].isChecked():
            k = 0
            self.carta_borrar = self.carta_26
        elif self.botones[1].isChecked():
            k = 1
            self.carta_borrar = self.carta_25
        elif self.botones[2].isChecked():
            k = 2
            self.carta_borrar = self.carta_24
        elif self.botones[3].isChecked():
            k = 3
            self.carta_borrar = self.carta_23
        elif self.botones[4].isChecked():
            k = 4
            self.carta_borrar = self.carta_22
        elif self.botones[5].isChecked():
            k = 5
            self.carta_borrar = self.carta_21

        if self.carta_sel1 == None:
            self.carta_sel1 = self.mi_mano1[k]
            self.carta_sel1_num = self.mi_mano1_num[k]
            self.fcarta(k, k, self.mi_mano1)
        else:
            self.carta_sel2 = self.mi_mano2[k]
            self.carta_sel2_num = self.mi_mano2_num[k]
            self.baza = [self.carta_sel1_num, self.carta_sel2_num]
            self.fcarta(k, k, self.mi_mano2)

    def fcambiojugador(self):
        cartas = play.Cbotones()
        self.freiniciarbotones()

        self.fmostar(self.mi_mano2, self.mi_triunfo, self.carpeta, self.formato)
        cartas.fcambiocarta(self.carta_borrar, self.icono_transparente)

        cartas.fcambiocarta(self.i_carta_j1, self.icono)
        cartas.fcambiocarta(self.i_carta_j2, self.carta_sel1)

    def fbaza(self):
        self.una_baza = log.Clogica()
        mano_nueva = play.Cmano()


        puntos_arriba, puntos_abajo = self.una_baza.flogica(self.num_player, self.baza,self.dic)

        if puntos_abajo > 0:
            self.puntos_j2_num +=puntos_abajo
        else:
            self.puntos_j1_num += puntos_arriba

        self.puntos_j1.setText('Puntos: {}'.format(self.puntos_j1_num))
        self.puntos_j2.setText('Puntos: {}'.format(self.puntos_j2_num))


        self.num_bazas, self.mi_mano1,\
        self.mi_mano2, self.baraja\
            = mano_nueva.frobar(self.num_bazas,self.mi_mano1,self.mi_mano1_num,
                                self.carta_sel1_num, self.mi_mano2,self.mi_mano2_num,
                                self.carta_sel2_num, self.baraja, puntos_abajo)

        if puntos_abajo > 0:
            ganador = 'j2'
        else:
            ganador = 'j1'

        self.fnuevoturno(self.mi_mano1,self.mi_mano2,ganador)

    def fnuevoturno(self, mano1, mano2, ganador):
        self.freiniciarbotones()
        cartas = play.Cbotones()
        mazo = play.Cdorso()
        img_dorso = mazo.fdorso(self.carpeta, self.formato)
        self.carta_21.setPixmap(img_dorso)
        self.carta_22.setPixmap(img_dorso)
        self.carta_23.setPixmap(img_dorso)
        self.carta_24.setPixmap(img_dorso)
        self.carta_25.setPixmap(img_dorso)
        self.carta_26.setPixmap(img_dorso)
        if ganador == 'j2':
            self.fcargarbotones(self.botones,mano2)
            cartas.fcambiocarta(self.i_carta_j1, self.icono)
            cartas.fcambiocarta(self.i_carta_j2, self.icono)

        elif ganador == 'j1':
            self.fcargarbotones(self.botones,mano1)
            cartas.fcambiocarta(self.i_carta_j1, self.icono)
            cartas.fcambiocarta(self.i_carta_j2, self.icono)




'''class Window_player_4(QMainWindow, form_class_2):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.carpeta = 'BarajaEsp/'
        self.formato = '.png'
        self.mi_mano1 = []
        self.mi_mano2 = []
        self.mi_mano3 = []
        self.mi_mano4 = []
        self.mis_puntos1 = []
        self.mis_puntos2 = []
        self.mis_puntos3 = []
        self.mis_puntos4 = []
        self.mano = None
        self.triunfo = None
        self.mi_triunfo = None
        self.mazo = None
        self.dic = None
        self.boton_repartir.clicked.connect(self.fcargarmano)
        self.num_player = 4

    def fcargarmano(self):
        self.mano = play.Cmano()
        self.triunfo = play.Ctriunfo()
        self.mazo = play.Cdorso()

        img_dorso = self.mazo.fdorso(self.carpeta,self.formato)
        self.i_mazo.setPixmap(img_dorso)

        self.mi_mano1,self.mi_mano2,self.mi_mano3,self.mi_mano4,\
        self.mis_puntos1,self.mis_puntos2,self.mis_puntos3,self.mis_puntos4,\
        self.mi_triunfo,self.dic = self.mano.frepartir(self.carpeta, self.formato,self.num_player)

        img_triunfo = self.triunfo.ftriunfo(self.carpeta, self.formato, self.mi_triunfo)
        self.i_triunfo.setPixmap(img_triunfo)

        self.carta_1.setPixmap(self.mi_mano1[0])
        self.carta_2.setPixmap(self.mi_mano1[1])
        self.carta_3.setPixmap(self.mi_mano1[2])
        self.carta_4.setPixmap(self.mi_mano1[3])
        self.carta_5.setPixmap(self.mi_mano1[4])
        self.carta_6.setPixmap(self.mi_mano1[5])
        self.carta_21.setPixmap(img_dorso)
        self.carta_22.setPixmap(img_dorso)
        self.carta_23.setPixmap(img_dorso)
        self.carta_24.setPixmap(img_dorso)
        self.carta_25.setPixmap(img_dorso)
        self.carta_26.setPixmap(img_dorso)
        self.carta_31.setPixmap(img_dorso)
        self.carta_32.setPixmap(img_dorso)
        self.carta_33.setPixmap(img_dorso)
        self.carta_34.setPixmap(img_dorso)
        self.carta_35.setPixmap(img_dorso)
        self.carta_36.setPixmap(img_dorso)
        self.carta_41.setPixmap(img_dorso)
        self.carta_42.setPixmap(img_dorso)
        self.carta_43.setPixmap(img_dorso)
        self.carta_44.setPixmap(img_dorso)
        self.carta_45.setPixmap(img_dorso)
        self.carta_46.setPixmap(img_dorso)'''
