#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoCad
from controllers.datos_personal_empresarial_controller import initData, translateView, updateData, checkValidacion, Save, autoCompleteNombre, Pregunta

class DatosPersonalEmpresarialView(QtGui.QGroupBox):
  def __init__(self, parent=None):
    super(DatosPersonalEmpresarialView, self).__init__(parent)
    
    self.label_nit = QtGui.QLabel(self)
    self.text_nit = CampoCad(self, u"Nit del Beneficiario")
    self.label_nombre = QtGui.QLabel(self)
    self.text_nombre = CampoCad(self, u"Nombre del Beneficiario")
    
    self.fila_beneficiario = QtGui.QVBoxLayout()
    self.fila_beneficiario.addWidget(self.label_nit)
    self.fila_beneficiario.addWidget(self.text_nit)
    self.fila_beneficiario.addWidget(self.label_nombre)
    self.fila_beneficiario.addWidget(self.text_nombre)
    
    self.setLayout(self.fila_beneficiario)
    self.text_nit.editingFinished.connect(self.auto_complete_nombre)
    self.translate_view()
  
  init_data = initData  
  translate_view = translateView
  update_data = updateData
  auto_complete_nombre = autoCompleteNombre
  check_validacion = checkValidacion
  save = Save
  pregunta = Pregunta