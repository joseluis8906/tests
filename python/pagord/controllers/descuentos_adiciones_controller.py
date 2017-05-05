#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from models.discriminacion_model import DiscriminacionModel

def initData(self, query_orden):
    self.text_iva.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_ret_fuente.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_ret_iva.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.checkbox_imp_municipales.setChecked(False)
    self.checkbox_auto_retenedor.setChecked(False)
    self.text_otros_concepto.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_otros_valor.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Descuentos y adiciones', None, QtGui.QApplication.UnicodeUTF8))
    self.label_iva.setText(QtGui.QApplication.translate('Orden', 'Iva $', None, QtGui.QApplication.UnicodeUTF8))
    self.label_ret_iva.setText(QtGui.QApplication.translate('Orden', 'Reteiva %', None, QtGui.QApplication.UnicodeUTF8))
    self.label_auto_retenedor.setText(QtGui.QApplication.translate('Orden', 'Autorretenedor', None, QtGui.QApplication.UnicodeUTF8))
    self.label_imp_municipales.setText(QtGui.QApplication.translate('Orden', 'Impuestos municipales', None, QtGui.QApplication.UnicodeUTF8))
    self.label_ret_fuente.setText(QtGui.QApplication.translate('Orden', 'Retefuente % ', None, QtGui.QApplication.UnicodeUTF8))
    self.label_otros_concepto.setText(QtGui.QApplication.translate('Orden', 'Concepto otros (item1,item2,...) ', None, QtGui.QApplication.UnicodeUTF8))
    self.label_otros.setText(QtGui.QApplication.translate('Orden', 'Valor otros (item1+item2+...) ', None, QtGui.QApplication.UnicodeUTF8))
    
def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    else:
        discriminacion = query_orden[0].discriminacion[0]
        self.text_iva.setText(QtGui.QApplication.translate('Orden', u"%s"%(discriminacion.get_iva()), None, QtGui.QApplication.UnicodeUTF8))
        self.text_ret_fuente.setText(QtGui.QApplication.translate('Orden', u"%s"%(discriminacion.get_ret_fuente()), None, QtGui.QApplication.UnicodeUTF8))
        self.text_ret_iva.setText(QtGui.QApplication.translate('Orden', u"%s"%(discriminacion.get_ret_iva()), None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox_auto_retenedor.setChecked(bool(discriminacion.get_auto_retenedor()))
        self.checkbox_imp_municipales.setChecked(bool(discriminacion.get_imp_municipales()))
        self.text_otros_concepto.setText(QtGui.QApplication.translate('Orden', u"%s"%(discriminacion.get_otros_concepto()), None, QtGui.QApplication.UnicodeUTF8))
        self.text_otros_valor.setText(QtGui.QApplication.translate('Orden', u"%s"%(discriminacion.get_otros_valor()), None, QtGui.QApplication.UnicodeUTF8))
        
def checkValidacion(self):
    if self.text_iva.validacion():
        if self.text_ret_fuente.validacion():
            if self.text_ret_iva.validacion():
                if self.text_otros_concepto.validacion():
                    if self.text_otros_valor.validacion():
                        if len(self.parent().OrdenModel.get_discriminacion()) > 0:
                            self.parent().OrdenModel.discriminacion[0].set_iva(u"%s"%(self.text_iva.text()))
                            self.parent().OrdenModel.discriminacion[0].set_ret_fuente(u"%s"%(self.text_ret_fuente.text()))
                            self.parent().OrdenModel.discriminacion[0].set_ret_iva(u"%s"%(self.text_ret_iva.text()))
                            self.parent().OrdenModel.discriminacion[0].set_auto_retenedor(bool(self.checkbox_auto_retenedor.checkState()))
                            self.parent().OrdenModel.discriminacion[0].set_imp_municipales(bool(self.checkbox_imp_municipales.checkState()))
                            self.parent().OrdenModel.discriminacion[0].set_otros_concepto(u"%s"%(self.text_otros_concepto.text()))
                            self.parent().OrdenModel.discriminacion[0].set_otros_valor(u"%s"%(self.text_otros_valor.text()))
                        else:
                            self.parent().OrdenModel.discriminacion.append(DiscriminacionModel(u"%s"%(self.text_iva.text()), u"%s"%(self.text_ret_fuente.text()), u"%s"%(self.text_ret_iva.text()), bool(self.checkbox_auto_retenedor.checkState()), bool(self.checkbox_imp_municipales.checkState()), u"%s"%(self.text_otros_concepto.text()), u"%s"%(self.text_otros_valor.text())))
                        return True
    return False
    
def Save(self):
    if self.check_validacion():
        return True
    return False
