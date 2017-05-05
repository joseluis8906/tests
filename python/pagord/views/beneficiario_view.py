#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from datos_personal_empresarial_view import DatosPersonalEmpresarialView
from certificado_disponibilidad_view import CertificadoDisponibilidadView
from certificado_registro_presupuestal_view import CertificadoRegistroPresupuestalView

from controllers.beneficiario_controller import initData, translateView, updateData, checkValidacion, Save

class BeneficiarioView(QtGui.QGroupBox):
    def __init__(self, parent=None):
      super(BeneficiarioView, self).__init__(parent)
    
      self.datos_personal_empresarial_view = DatosPersonalEmpresarialView(self)
      self.certificado_disponibilidad_view = CertificadoDisponibilidadView(self)
      self.certificado_registro_presupuestal_view = CertificadoRegistroPresupuestalView(self)
    
      self.contenedor_beneficiario = QtGui.QHBoxLayout()
      self.contenedor_beneficiario.addWidget(self.datos_personal_empresarial_view)
      self.contenedor_beneficiario.addWidget(self.certificado_disponibilidad_view)
      self.contenedor_beneficiario.addWidget(self.certificado_registro_presupuestal_view)
    
      self.setLayout(self.contenedor_beneficiario)
      self.translate_view()

    init_data = initData
    translate_view = translateView
    update_data = updateData
    check_validacion = checkValidacion
    save = Save