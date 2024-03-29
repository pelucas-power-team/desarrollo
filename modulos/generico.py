
import random as r
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap, QTransform

class Cbaraja():
    def __init__(self):
        self.__mi_baraja = [0 for i in range(40)]
        self.__auxbaraja = []
        self.__auxpuntos = []
        self.__mis_puntos = []
        self.__puntuables =[[108, 208, 308, 408],[109, 209, 309, 409], [110, 210, 310, 410],[13, 23, 33, 43], [11, 21, 31, 41]]
        self.__orden =[8, 9]

    def __fcrearbaraja(self):
        baraja = [0 for i in range(40)]
        k = 0
        for i in range(1,5):
            for j in range(1,11):
                if j not in self.__orden:
                    self.__mi_baraja[k] = int(str(i) + str(j),base = 10)
                    baraja[k] = int(str(i) + str(j),base = 10)
                    if j != 10 :
                        self.__auxbaraja.append(str(i) + '0' +  str(j))
                    else:
                        self.__auxbaraja.append(str(i) + str(j))
                else:
                    self.__mi_baraja[k] = int(str(i) + str(0) + str(j),base = 10)
                    baraja[k] = int(str(i) + str(0) + str(j),base = 10)
                    self.__auxbaraja.append(str(self.__mi_baraja[k]))
                k+=1

        puntos = self.__fpuntos(self.__mi_baraja)
        diccionario = [baraja,self.__auxbaraja, puntos]

        return(self.__mi_baraja,diccionario)

    def __fbarajar(self):
        self.__mi_baraja, __dic = self.__fcrearbaraja()
        r.shuffle(self.__mi_baraja)
        return(self.__mi_baraja, __dic)

    def __fpuntos(self,baraja):

        for i in range(len(baraja)):
            if baraja[i] in self.__puntuables[0]:
                self.__mis_puntos.append(2)
            elif baraja[i] in self.__puntuables[1]:
                self.__mis_puntos.append(3)
            elif baraja[i] in self.__puntuables[2]:
                self.__mis_puntos.append(4)
            elif baraja[i] in self.__puntuables[3]:
                self.__mis_puntos.append(10)
            elif baraja[i] in self.__puntuables[4]:
                self.__mis_puntos.append(11)
            else:
                self.__mis_puntos.append(0)

        return (self.__mis_puntos)

    def getBaraja(self):
        baraja, dic = self.__fbarajar()
        puntos = self.__fpuntos(baraja)
        return (baraja, puntos,dic)

class Cmano(Cbaraja):
    def __init__(self):
        super().__init__()
        self.baraja = []
        self.puntos = []
        self.mi_mano1 = []
        self.mi_mano2 =[]
        self.mi_mano3 = []
        self.mi_mano4 = []
        self.mano_j1 = []
        self.mano_j2 = []
        self.mano_j3 = []
        self.mano_j4 = []
        self.puntos_j1 = []
        self.puntos_j2 = []
        self.puntos_j3 = []
        self.puntos_j4 = []
        self.mi_mano_orden1 = []
        self.mi_mano_orden2 = []
        self.mi_mano_orden3 = []
        self.mi_mano_orden4 = []
        self.mis_puntos1 = []
        self.mis_puntos2 = []
        self.mis_puntos3 = []
        self.mis_puntos4 = []
        self.carta = []
        self.triunfo = None
        self.dic = None

    def frepartir(self,carp, forma,numj):
        self.baraja, self.puntos, self.dic = self.getBaraja()

        if numj == 2:
            for i in range(12):
                if i<6:
                    self.mano_j1.append(self.baraja[i])
                else:
                    self.mano_j2.append(self.baraja[i])

            self.triunfo = self.baraja[12]
            self.mano_j1, self.puntos_j1 = self.fordenar(self.mano_j1,self.dic,self.triunfo)
            self.mano_j2, self.puntos_j2 = self.fordenar(self.mano_j2, self.dic,self.triunfo)

            for i in range(12):
                if i<6:
                    mi_carta = self.mano_j1[i]
                    self.mi_mano_orden1.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano1.append(QPixmap(self.carta[i]))
                else:
                    mi_carta = self.mano_j2[i-6]
                    self.mi_mano_orden2.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano2.append(QPixmap(self.carta[i]))
            return (self.mi_mano1, self.mano_j1, self.mi_mano2, self.mano_j2, self.mis_puntos1, self.mis_puntos2, self.triunfo, self.dic, self.baraja)

        '''elif numj == 4:
            #Esto todavia hay que adaptarlo para que ordene bien las cartas
            for i in range(24):
                if i < 6:
                    self.mano_j1.append(self.baraja[i])
                elif 12>i>6:
                    self.mano_j2.append(self.baraja[i])
                elif 18>i>12:
                    self.mano_j3.append(self.baraja[i])
                else:
                    self.mano_j4.append(self.baraja[i])

            self.triunfo = self.baraja[24]
            self.mano_j1, self.puntos_j1 = self.fordenar(self.mano_j1, self.dic, self.triunfo)
            self.mano_j2, self.puntos_j2 = self.fordenar(self.mano_j2, self.dic, self.triunfo)
            self.mano_j3, self.puntos_j3 = self.fordenar(self.mano_j3, self.dic, self.triunfo)
            self.mano_j4, self.puntos_j4 = self.fordenar(self.mano_j4, self.dic, self.triunfo)

            for i in range(24):
                if i < 6:
                    mi_carta = self.mano_j1[i]
                    self.mi_mano_orden1.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano1.append(QPixmap(self.carta[i]))
                elif 12>i>6:
                    mi_carta = self.mano_j2[i-6]
                    self.mi_mano_orden1.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano2.append(QPixmap(self.carta[i]))
                elif 18>i>12:
                    mi_carta = self.mano_j3[i-12]
                    self.mi_mano_orden1.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano3.append(QPixmap(self.carta[i]))
                else:
                    mi_carta = self.mano_j3[i - 18]
                    self.mi_mano_orden1.append(mi_carta)
                    self.carta.append(carp + str(mi_carta) + forma)
                    self.mi_mano4.append(QPixmap(self.carta[i]))
            return (self.mi_mano1, self.mi_mano2,
                    self.mi_mano3, self.mi_mano4,
                    self.mis_puntos1, self.mis_puntos2,
                    self.mis_puntos3, self.mis_puntos4,
                    self.triunfo, self.dic)'''


    def fordenar(self,mano_ori,ref_global,triunfo):
        mano = []
        puntos = []
        mano_str = []
        mano_salida = []
        triunfo_carta = None
        triunfos = []
        aux_1 = []
        aux_2 = []


        for i in range(len(ref_global[0])):
            for j in range(len(mano_ori)):
                if ref_global[0][i] == mano_ori[j]:
                    mano.append(int(ref_global[1][i],base=10))
                    puntos.append(ref_global[2][i])

        for i in range(len(ref_global[0])):
            if ref_global[0][i] == triunfo:
                triunfo_carta = int(ref_global[1][i],base = 10)

        triunfo_str = list(str(triunfo_carta))

        for i in range(len(mano)):
            aux = mano[i]
            mano_str.append(list(str(aux)))


        for i in range(1, len(mano_str)):
            for j in range(0, len(mano_str) - i):
                if (puntos[j + 1] < puntos[j]) and (mano_str[j+1][0] == mano_str[j][0]):
                    almacen = puntos[j]
                    puntos[j] = puntos[j + 1]
                    puntos[j + 1] = almacen
                    almacen = mano[j]
                    mano[j] = mano[j + 1]
                    mano[j + 1] = almacen

        for i in range(len(mano)):
            if mano_str[i][0] == triunfo_str[0]:
                triunfos.append(mano[i])
            else:
                aux_1.append(mano[i])

        for i in range(len(mano)):
            if mano[i] not in triunfos:
                aux_2.append(mano[i])

        for i in range(len(mano)):
            if i < len(triunfos):
                mano[i] = triunfos[i]
            else:
                mano[i] =aux_2[i-len(triunfos)]

        for j in (mano):
            for i in range(len(ref_global[0])):
                if int(ref_global[1][i]) == j:
                    mano_salida.append(ref_global[0][i])

        return mano_salida, puntos

    def frobar(self, numbazas, mano1, mano1_num,carta_1, mano2, mano2_num, carta_2, baraja, puntos):
        if numbazas == 20:
            triunfo = baraja[12]
            del baraja[0:13]
            baraja.append(triunfo)
            if puntos>0:
                for i in range(len(mano2_num)):
                    if mano2_num[i] == carta_2:
                        mano2_num[i] = baraja[0]
                        mano2[i] = 'BarajaEsp' + str(carta_2) + '.png'
                for i in range(len(mano1_num)):
                    if mano1_num[i] == carta_1:
                        mano1_num[i] = baraja[1]
                        mano1[i] = 'BarajaEsp' + str(carta_1) + '.png'
            else:
                for i in range(len(mano2_num)):
                    if mano2_num[i] == carta_2:
                        mano2_num[i] = baraja[1]
                        mano2[i] = 'BarajaEsp' + str(carta_2) + '.png'
                for i in range(len(mano1_num)):
                    if mano1_num[i] == carta_1:
                        mano1_num[i] = baraja[0]
                        mano1[i] = 'BarajaEsp' + str(carta_1) + '.png'
        elif 20>numbazas>6:
            del baraja[0:1]
            if puntos > 0:
                for i in range(len(mano2_num)):
                    if mano2_num[i] == carta_2:
                        mano2_num[i] = baraja[0]
                        mano2[i] = 'BarajaEsp' + str(carta_2) + '.png'
                for i in range(len(mano1_num)):
                    if mano1_num[i] == carta_1:
                        mano1_num[i] = baraja[1]
                        mano1[i] = 'BarajaEsp' + str(carta_1) + '.png'
            else:
                for i in range(len(mano2_num)):
                    if mano2_num[i] == carta_2:
                        mano2_num[i] = baraja[1]
                        mano2[i] = 'BarajaEsp' + str(carta_2) + '.png'
                for i in range(len(mano1_num)):
                    if mano1_num[i] == carta_1:
                        mano1_num[i] = baraja[0]
                        mano1[i] = 'BarajaEsp' + str(carta_1) + '.png'

        numbazas-=1
        return(numbazas, mano1, mano2,baraja)


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

class Cbotones():
    def ficonos(self,carta,icono):
        carta.setIcon(QtGui.QIcon(icono))
        carta.setIconSize(QtCore.QSize(100,150))

    def fcartas(self,boton,icono,carta_jugada,carta):
        self.ficonos(boton,icono)
        icarta_jugada = QPixmap(carta_jugada)
        carta.setPixmap(icarta_jugada)

    def fcambiocarta(self,carta,icono):
        icarta_jugada = QPixmap(icono)
        carta.setPixmap(icarta_jugada)
