#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from models.opciones_model import OpcionesModel

def initData(self, query_orden):
    self.checkbox_pago_final.setChecked(False)
    self.text_monto.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_monto.setEnabled(False)
    self.checkbox_anulada.setChecked(False)
    self.text_orden_relacionada.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Opciones', None, QtGui.QApplication.UnicodeUTF8))
    self.checkbox_pago_final.setText(QtGui.QApplication.translate('Orden', 'Pago final ', None, QtGui.QApplication.UnicodeUTF8))
    self.label_pago_final.setText(QtGui.QApplication.translate('Orden', 'Monto $ ', None, QtGui.QApplication.UnicodeUTF8))
    self.text_monto.setEnabled(False)
    self.checkbox_anulada.setText(QtGui.QApplication.translate('Orden', 'Anulada ', None, QtGui.QApplication.UnicodeUTF8))
    self.label_orden_relacionada.setText(QtGui.QApplication.translate('Orden', 'Orden Relacionada', None, QtGui.QApplication.UnicodeUTF8))
    
def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    else:
        opciones = query_orden[0].opciones[0]
        self.checkbox_pago_final.setChecked(bool(opciones.get_pago_final()))
        self.habilitar_monto()
        self.text_monto.setText(QtGui.QApplication.translate('Orden', u"%s"%(opciones.get_monto()), None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_anulada.setChecked(bool(opciones.get_anulada()))
        self.text_orden_relacionada.setText(QtGui.QApplication.translate('Orden', u"%s"%(opciones.get_orden_relacionada()), None, QtGui.QApplication.UnicodeUTF8))
        
def habilitarMonto(self):
    if self.checkbox_pago_final.checkState():
        self.text_monto.setEnabled(True)
    else:
        self.text_monto.setEnabled(False)
        
def checkValidacion(self):
    if self.checkbox_pago_final.checkState():
        if self.text_monto.validacion(obligatorio=True):
            if self.text_orden_relacionada.validacion():
                return True
    else:    
        if self.text_monto.validacion():
            if self.text_orden_relacionada.validacion():
                return True
    return False
    
def Save(self):
    if self.check_validacion():
        if len(self.parent().OrdenModel.opciones) > 0:
            self.parent().OrdenModel.opciones[0].set_pago_final(bool(self.checkbox_pago_final.checkState()))
            self.parent().OrdenModel.opciones[0].set_monto(u"%s"%(self.text_monto.text()))
            self.parent().OrdenModel.opciones[0].set_anulada(bool(self.checkbox_anulada.checkState()))
            self.parent().OrdenModel.opciones[0].set_orden_relacionada(u"%s"%(self.text_orden_relacionada.text()))
        else:
            self.parent().OrdenModel.opciones.append(OpcionesModel(bool(self.checkbox_pago_final.checkState()), u"%s"%(self.text_monto.text()), bool(self.checkbox_anulada.checkState()), u"%s"%(self.text_orden_relacionada.text())))
        return True
    return False
