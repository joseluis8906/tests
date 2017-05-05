#-*- coding: utf-8 -*-

import datetime
from PyQt4 import QtGui
from models.models import session
from models.orden_model import OrdenModel

def initData(self, query_orden):
    if(len(query_orden)==0):
        self.text_numero.setText(QtGui.QApplication.translate('Orden', '1', None, QtGui.QApplication.UnicodeUTF8))    
    else:
        self.text_numero.setText(QtGui.QApplication.translate('Orden', u"%s"%(query_orden[-1].get_numero()+1), None, QtGui.QApplication.UnicodeUTF8))
     
    self.date_fecha.setDate(datetime.date.today())
    self.text_bien_servicio.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_rubro.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Datos de la orden', None, QtGui.QApplication.UnicodeUTF8))
    self.label_numero.setText(QtGui.QApplication.translate('Orden', 'Número ', None, QtGui.QApplication.UnicodeUTF8))
    self.label_fecha.setText(QtGui.QApplication.translate('Orden', 'Fecha ', None, QtGui.QApplication.UnicodeUTF8))
    self.date_fecha.setCalendarPopup(True)
    self.label_bien_servicio.setText(QtGui.QApplication.translate('Orden', 'bien o servicio $', None, QtGui.QApplication.UnicodeUTF8))
    self.label_rubro.setText(QtGui.QApplication.translate('Orden', 'Rubro', None, QtGui.QApplication.UnicodeUTF8))

def updateData(self, query_orden):
    if(len(query_orden)==0):
        query_orden = session.query(OrdenModel).all()
        self.init_data(query_orden)
    else:
        orden = query_orden[0]
        self.text_numero.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.get_numero()), None, QtGui.QApplication.UnicodeUTF8))
        fecha_query = datetime.date(orden.get_fecha().year, orden.get_fecha().month, orden.get_fecha().day)
        self.date_fecha.setDate(fecha_query)
        self.text_bien_servicio.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.get_bien_servicio()), None, QtGui.QApplication.UnicodeUTF8))
        self.text_rubro.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.get_rubro()), None, QtGui.QApplication.UnicodeUTF8))
        
def checkValidacion(self):
    if self.text_numero.validacion(obligatorio=True):
        if self.text_bien_servicio.validacion(obligatorio=True):
            if self.text_rubro.validacion():
                return True
    return False
    
def Save(self):
    if self.check_validacion():
        orden_query = session.query(OrdenModel).filter(OrdenModel.numero == int(self.text_numero.text())).all()
        if len(orden_query) > 0:
            orden = orden_query[0]
            if orden.get_fecha() != self.date_fecha.date():
                orden.set_fecha(datetime.date(self.date_fecha.date().year(), self.date_fecha.date().month(), self.date_fecha.date().day()))
            if orden.get_bien_servicio() != u"%s"%(self.text_bien_servicio.text()):
                orden.set_bien_servicio(u"%s"%(self.text_bien_servicio.text()))
            if orden.get_rubro() != u"%s"%(self.text_rubro.text()):
                orden.set_rubro(u"%s"%(self.text_rubro.text()))
        else:
            orden = OrdenModel(u"%s"%(self.text_numero.text()),datetime.date(self.date_fecha.date().year(), self.date_fecha.date().month(), self.date_fecha.date().day()), u"%s"%(self.text_bien_servicio.text()), u"%s"%(self.text_rubro.text()))
            
        self.parent().OrdenModel = orden
        return True
    
    return False
