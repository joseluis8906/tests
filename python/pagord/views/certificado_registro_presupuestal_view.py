#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoCad
from controllers.certificado_registro_presupuestal_controller import initData, translateView, updateData, checkValidacion, Save

class CertificadoRegistroPresupuestalView(QtGui.QGroupBox):
  def __init__(self, parent=None):
    super(CertificadoRegistroPresupuestalView, self).__init__(parent)
    
    self.conten_colum_certi_reg = QtGui.QHBoxLayout()
    self.columna_num_certi_reg = QtGui.QVBoxLayout()
    self.columna_fechas_certi_reg = QtGui.QVBoxLayout()
    self.label_num_certi_reg = QtGui.QLabel(self)
    self.label_fecha_certi_reg = QtGui.QLabel(self)
    self.text_num_certi_reg1 = CampoCad(self, u"Certificado Registro Presupuestal 1")
    self.date_fecha_certi_reg1 = QtGui.QDateEdit(self)
    self.text_num_certi_reg2 = CampoCad(self, u"Certificado Registro Presupuestal 2")
    self.date_fecha_certi_reg2 = QtGui.QDateEdit(self)
    self.text_num_certi_reg3 = CampoCad(self, u"Certificado Registro Presupuestal 3")
    self.date_fecha_certi_reg3 = QtGui.QDateEdit(self)
    
    self.conten_colum_certi_reg.addLayout(self.columna_num_certi_reg)
    self.conten_colum_certi_reg.addLayout(self.columna_fechas_certi_reg)
    
    self.columna_num_certi_reg.addWidget(self.label_num_certi_reg)
    self.columna_fechas_certi_reg.addWidget(self.label_fecha_certi_reg)
    self.columna_num_certi_reg.addWidget(self.text_num_certi_reg1)
    self.columna_fechas_certi_reg.addWidget(self.date_fecha_certi_reg1)
    self.columna_num_certi_reg.addWidget(self.text_num_certi_reg2)
    self.columna_fechas_certi_reg.addWidget(self.date_fecha_certi_reg2)
    self.columna_num_certi_reg.addWidget(self.text_num_certi_reg3)
    self.columna_fechas_certi_reg.addWidget(self.date_fecha_certi_reg3)
    
    self.setLayout(self.conten_colum_certi_reg)
    self.translate_view()
  
  init_data = initData
  translate_view = translateView
  update_data = updateData
  check_validacion = checkValidacion
  save = Save