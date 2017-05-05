#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoDec, CampoCad
from controllers.dialogo_busqueda_controller import initData, translateView, Buscar

class DialogoBusquedaView(QtGui.QDialog):
  def __init__(self, parent=None):
    super(DialogoBusquedaView, self).__init__(parent)
    
    self.grupo_busqueda = QtGui.QGroupBox(self)
    self.label_busqueda = QtGui.QLabel(self)
    self.text_busqueda = QtGui.QLineEdit(self)
    self.boton_buscar = QtGui.QPushButton(self)
    self.tabla = QtGui.QTableWidget(self)
    
    self.contenedor_busqueda = QtGui.QVBoxLayout(self)
    self.contenedor_busqueda.addWidget(self.label_busqueda)
    self.contenedor_busqueda.addWidget(self.text_busqueda)
    self.contenedor_busqueda.addWidget(self.boton_buscar)
    self.contenedor_busqueda.addWidget(self.tabla)
    
    self.grupo_busqueda.setLayout(self.contenedor_busqueda)
    
    self.contenedor = QtGui.QVBoxLayout(self)
    
    self.contenedor.addWidget(self.grupo_busqueda)
    
    self.setLayout(self.contenedor)
    
    self.boton_buscar.clicked.connect(self.buscar)
    self.translate_view()

  init_data = initData
  translate_view = translateView
  buscar = Buscar
    
