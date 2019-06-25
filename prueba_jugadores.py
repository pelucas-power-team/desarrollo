import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from modulos import ventanas as wind
from PyQt5.QtGui import QPixmap


# Cargar nuestro formulario *.ui
main_class = uic.loadUiType("interfaces/main.ui")[0]

# Crear la Clase MyWindowClass con el formulario cargado.
class MainWindowClass(QMainWindow, main_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.fondo_imagen = 'interfaces/fondo.png'
        self.icono2p = 'interfaces/2PL.PNG'
        self.icono4p = 'interfaces/4PL.PNG'
        self.fondo.setPixmap(QPixmap(self.fondo_imagen))
        self.jugar_2.setIcon(QtGui.QIcon(self.icono2p))
        self.jugar_2.setIconSize(QtCore.QSize(75,50))
        self.jugar_4.setIcon(QtGui.QIcon(self.icono4p))
        self.jugar_4.setIconSize(QtCore.QSize(75, 50))
        self.player_2 = wind.Window_player_2(None)
        #self.player_4 = wind.Window_player_4(None)

        self.jugar_2.clicked.connect(self.fopen_window_2)
        #self.jugar_4.clicked.connect(self.fopen_window_4

    def fopen_window_2(self):
        MainWindowClass.close(self)
        self.player_2.show()

    '''def fopen_window_4(self):
        MainWindowClass.close(self)
        self.player_4.fwindow'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindowClass(None)
    MainWindow.show()
    app.exec_()