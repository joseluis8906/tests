#-*- coding: utf-8 -*-

from PyQt4 import QtGui

class BarraMenuView(QtGui.QMenuBar):
    def __init__(self, parent):
        super(BarraMenuView, self).__init__(parent)
        
        accion_salir = QtGui.QAction(QtGui.QIcon('exit.png'), '&Salir', self)
        accion_salir.setStatusTip(u'Salir')
        accion_salir.triggered.connect(QtGui.qApp.quit)
        
        self.archivo = self.addMenu(u'&Archivo')
        self.archivo.addAction(accion_salir)
        
        accion_dialogo = QtGui.QAction(QtGui.QIcon('configuracion.png'), u'&Búsqueda', self)
        accion_dialogo.setStatusTip(u'Búsqueda')
        accion_dialogo.triggered.connect(self.parent().dialogo_busqueda)
        
        self.opciones = self.addMenu(u'&Opciones')
        self.opciones.addAction(accion_dialogo)
      
    def configuracion(self):
        print("llamando a configuración")