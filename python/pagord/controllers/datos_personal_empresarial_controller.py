#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from models.beneficiario_model import BeneficiarioModel
from models.models import session

def initData(self, query_orden):
    self.text_nit.setText(QtGui.QApplication.translate('Orden',  u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_nombre.setText(QtGui.QApplication.translate('Orden',  u"", None, QtGui.QApplication.UnicodeUTF8))

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Datos Personal/Empresarial', None, QtGui.QApplication.UnicodeUTF8))
    self.label_nit.setText(QtGui.QApplication.translate('Orden', 'Nit o C.C ', None, QtGui.QApplication.UnicodeUTF8))
    self.text_nit.setMinimumWidth(250)
    self.label_nombre.setText(QtGui.QApplication.translate('Orden', 'Nombre ', None, QtGui.QApplication.UnicodeUTF8))
    self.text_nombre.setMinimumWidth(250)
    
def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    else:
        beneficiario = query_orden[0].beneficiario
        self.text_nit.setText(QtGui.QApplication.translate('Orden',  u"%s"%(beneficiario.get_nit()), None, QtGui.QApplication.UnicodeUTF8))
        self.text_nombre.setText(QtGui.QApplication.translate('Orden',  u"%s"%(beneficiario.get_nombre()), None, QtGui.QApplication.UnicodeUTF8))

def autoCompleteNombre(self):
    if self.text_nit.validacion(obligatorio=True):
        beneficiario = session.query(BeneficiarioModel).filter(BeneficiarioModel.nit == u"%s"%(self.text_nit.text())).all()
        if len(beneficiario) > 0:
            self.text_nombre.setText(QtGui.QApplication.translate('Orden', u"%s"%(beneficiario[0].get_nombre()), None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.text_nombre.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))

def checkValidacion(self):
    if self.text_nit.validacion(obligatorio=True):
        if self.text_nombre.validacion(obligatorio=True):
            return True
    return False
    
def Save(self):
    if self.check_validacion():
        beneficiario_query = session.query(BeneficiarioModel).filter(BeneficiarioModel.nit == u"%s"%(self.text_nit.text())).all()
        if len(beneficiario_query) > 0:
            beneficiario = beneficiario_query[0]
            if self.parent().parent().OrdenModel.get_beneficiario():
                if self.parent().parent().OrdenModel.get_beneficiario() != beneficiario:
                    self.parent().parent().OrdenModel.set_beneficiario(beneficiario)
            else:
                beneficiario.orden.append(self.parent().parent().OrdenModel)
            if beneficiario.get_nombre() != u"%s"%(self.text_nombre.text()):
                opcion = self.pregunta(u"El nit del beneficiario ya está registrado, pero el nombre \nno coincide con el nit. \n\n¿Sobre escribir el nombre del beneficiario?")
                if opcion == QtGui.QMessageBox.Yes:
                    beneficiario.set_nombre(u"%s"%(self.text_nombre.text()))
        else:
            beneficiario = BeneficiarioModel(u"%s"%(self.text_nombre.text()), u"%s"%(self.text_nit.text()))
            beneficiario.orden.append(self.parent().parent().OrdenModel)
        self.parent().parent().BeneficiarioModel = beneficiario
        return True
    return False

def Pregunta(self, info):
    self.respuesta = QtGui.QMessageBox.question(self, u"Cuidado", u"%s"%(info), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    return self.respuesta