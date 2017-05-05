#-*- coding: utf-8 -*-

import datetime
from PyQt4 import QtGui
from campos import CampoNum, CampoCad
from controllers.orden_controller import initData, translateView, updateData, checkValidacion, Save

class OrdenView(QtGui.QGroupBox):
  def __init__(self, parent=None):
    super(OrdenView, self).__init__(parent)

    self.label_numero = QtGui.QLabel(self)
    self.text_numero = CampoNum(self, u"Número de orden")
    self.label_fecha = QtGui.QLabel(self)
    self.date_fecha = QtGui.QDateEdit(self)
    self.label_bien_servicio = QtGui.QLabel(self)
    self.text_bien_servicio = CampoNum(self, u"Bien/servicio")
    self.label_rubro = QtGui.QLabel(self)
    self.text_rubro = CampoCad(self, u"Rubro")
    
    self.fila_orden = QtGui.QHBoxLayout()
    self.fila_orden.addWidget(self.label_numero)
    self.fila_orden.addWidget(self.text_numero)
    self.fila_orden.addWidget(self.label_fecha)
    self.fila_orden.addWidget(self.date_fecha)
    self.fila_orden.addWidget(self.label_bien_servicio)
    self.fila_orden.addWidget(self.text_bien_servicio)
    self.fila_orden.addWidget(self.label_rubro)
    self.fila_orden.addWidget(self.text_rubro)

    self.setLayout(self.fila_orden)
    self.translate_view()

  init_data = initData
  translate_view = translateView
  update_data = updateData
  check_validacion = checkValidacion
  save = Save