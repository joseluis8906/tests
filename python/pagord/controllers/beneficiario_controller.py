#-*- coding: utf-8 -*-

from PyQt4 import QtGui

def initData(self, query_orden):
    self.datos_personal_empresarial_view.init_data(query_orden)
    self.certificado_disponibilidad_view.init_data(query_orden)
    self.certificado_registro_presupuestal_view.init_data(query_orden)

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Beneficiario', None, QtGui.QApplication.UnicodeUTF8))
    
def updateData(self, query_orden):
    self.datos_personal_empresarial_view.update_data(query_orden)
    self.certificado_disponibilidad_view.update_data(query_orden)
    self.certificado_registro_presupuestal_view.update_data(query_orden)

def checkValidacion(self):
    if self.datos_personal_empresarial_view.check_validacion():
        if self.certificado_disponibilidad_view.check_validacion():
            return True
    return False
    
def Save(self):
    if self.datos_personal_empresarial_view.save():
        if self.certificado_disponibilidad_view.save():
            if self.certificado_registro_presupuestal_view.save():
                return True
    return False
