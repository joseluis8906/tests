#! /usr/bin/python
#-*- coding: utf-8 -*-

import re
from encodings import utf_8
from PyQt4 import QtCore, QtGui
from models.models import session
from models.orden_model import OrdenModel

class CampoNum(QtGui.QLineEdit):
    def __init__(self, parent=None, label=u""):
        super(CampoNum, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        
        if len(self.text()) > 0:
            try:
                int(self.text())
            except:
                self.alerta(u"El campo %s debe ser un número entero."%(self.get_label()))
                return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
    
class CampoCad(QtGui.QLineEdit):
    def __init__(self, parent=None, label=u""):
        super(CampoCad, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        
        if len(self.text()) > 0 and not re.match("^([a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ#°&-.,]+\s*[a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ#°&-.,]*)+$", str(unicode(self.text()).encode('utf-8')), re.UNICODE):
            self.alerta(u"El campo %s contiene caracteres no permitidos."%(self.get_label()))
            return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)

class CampoParrafo(QtGui.QTextEdit):
    def __init__(self, parent=None, label=u""):
        super(CampoParrafo, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        texto = self.toPlainText()
        if obligatorio and len(texto) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        
        if len(texto) > 0 and not re.match("^([a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ#°&-.,]+\s*[a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ#°&-.,]*)+$", str(unicode(texto).encode('utf-8')), re.UNICODE):
            self.alerta(u"El campo %s contiene caracteres no permitidos."%(self.get_label()))
            return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
    
class CampoDec(QtGui.QLineEdit):
    def __init__(self, parent=None, label=u""):
        super(CampoDec, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False, msg=u""):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        if len(self.text()) > 0 and not re.match("^[0-9]+[.]{0,1}[0-9]*$", str(unicode(self.text()).encode('utf-8')), re.UNICODE):
            self.alerta(u"El campo %s contiene caracteres no permitidos."%(self.get_label()))
            return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
        
class ConceptoOtros(CampoCad):
    def __init__(self, parent=None, label=u""):
        super(ConceptoOtros, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        elif len(self.text()) > 0 and not re.match("^([a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ,]+\s*[a-zñA-ZÑ0-9áéíóúÁÉÍÓÚ,]*)+$", str(unicode(self.text()).encode('utf-8')), re.UNICODE):
            self.alerta(u"El campo %s contiene caracteres no permitidos."%(self.get_label()))
            return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
    
class ValorOtros(CampoCad):
    def __init__(self, parent=None, label=u""):
        super(ValorOtros, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        elif len(self.text()) > 0 and not re.match("^([0-9]+\+*[0-9]*)+$", str(unicode(self.text()).encode('utf-8')), re.UNICODE):
            self.alerta(u"El campo %s contiene caracteres no permitidos."%(self.get_label()))
            return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)

class CampoOrdRel(QtGui.QLineEdit):
    def __init__(self, parent=None, label=u""):
        super(CampoOrdRel, self).__init__(parent)
        self.label = label
        
    def validacion(self, obligatorio=False):
        if obligatorio and len(self.text()) == 0:
            self.alerta(u"El campo %s es obligatorio."%(self.get_label()))
            return False
        
        if len(self.text()) > 0:
            try:
                int(self.text())
                if len(session.query(OrdenModel).filter(OrdenModel.numero==int(self.text())).all()) < 1:
                    self.alerta(u"Ninguna orden concuerda con el número de relación.")            
                    return False
            except:
                self.alerta(u"El campo %s debe ser un número entero."%(self.get_label()))
                return False
        return True
    
    def get_label(self):
        return self.label
    
    def alerta(self, info):
        self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
    