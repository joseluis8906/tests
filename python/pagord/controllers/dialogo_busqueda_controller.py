#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from models.models import session
from models.orden_model import OrdenModel

def initData(self):
    self.text_busqueda.setText(u"")
    
def translateView(self):
    self.label_busqueda.setText(QtGui.QApplication.translate('Orden', u"Número de orden", None, QtGui.QApplication.UnicodeUTF8))
    self.boton_buscar.setText(QtGui.QApplication.translate('Orden', u"Buscar", None, QtGui.QApplication.UnicodeUTF8))
    
    self.setGeometry(50, 50, 600, 400)
    self.boton_buscar.setMaximumWidth(80)
    self.text_busqueda.setMaximumWidth(250)

    self.tabla.setColumnCount(7)
    
    self.tabla.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem(u"Número"))
    self.tabla.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem(u"Fecha"))
    self.tabla.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem(u"Bien/servicio"))
    self.tabla.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem(u"Concepto"))
    self.tabla.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem(u"Beneficiario"))
    self.tabla.setHorizontalHeaderItem(5, QtGui.QTableWidgetItem(u"Pago Final"))
    self.tabla.setHorizontalHeaderItem(5, QtGui.QTableWidgetItem(u"Anulada"))
    
def rastrearOrdenes(orden, lista_de_ordenes):
    lista_de_ordenes.append(orden)
    try:
        if orden.opciones[0].get_orden_relacionada() != u"" or orden.opciones[0].get_orden_relacionada() != None:
            nueva_orden = session.query(OrdenModel).filter(OrdenModel.numero==orden.opciones[0].ord_rel).all()
            rastrearOrdenes(nueva_orden[0], lista_de_ordenes)
    except:
        pass

def Buscar(self):
    if(len(self.text_busqueda.text()) > 0):
        orden_query = session.query(OrdenModel).filter(OrdenModel.numero==int(self.text_busqueda.text())).all()
        if len(orden_query)>0:
            lista_de_ordenes = []
            rastrearOrdenes(orden_query[0], lista_de_ordenes)
            self.tabla.setRowCount(len(lista_de_ordenes))
            for index, orden in enumerate(lista_de_ordenes):
                self.tabla.setItem(index,0, QtGui.QTableWidgetItem(u"%s"%orden.get_numero()))
                self.tabla.setItem(index,1, QtGui.QTableWidgetItem(u"%s"%orden.get_fecha()))
                self.tabla.setItem(index,2, QtGui.QTableWidgetItem(u"%s"%((int(orden.get_bien_servicio())+int(orden.discriminacion[0].get_iva())))))
                self.tabla.setItem(index,3, QtGui.QTableWidgetItem(u"%s"%orden.get_concepto()))
                self.tabla.setItem(index,4, QtGui.QTableWidgetItem(u"%s"%orden.get_beneficiario().get_nit()))
                self.tabla.setItem(index,5, QtGui.QTableWidgetItem(u"%s"%("Si" if (orden.get_opciones()[0].get_pago_final()) else u"No")))
                self.tabla.setItem(index,6, QtGui.QTableWidgetItem(u"%s"%("Si" if (orden.get_opciones()[0].get_anulada()) else u"No")))