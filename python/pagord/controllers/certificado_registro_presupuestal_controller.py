#-*- coding: utf-8 -*-

import datetime
from PyQt4 import QtGui
from models.models import session
from models.cerreg_model import CerregModel

def initData(self, query_orden):
    self.text_num_certi_reg1.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_num_certi_reg2.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_num_certi_reg3.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.date_fecha_certi_reg1.setDate(datetime.date.today())
    self.date_fecha_certi_reg2.setDate(datetime.date.today())
    self.date_fecha_certi_reg3.setDate(datetime.date.today())

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Certificados de regsitro presupuestal', None, QtGui.QApplication.UnicodeUTF8))
    self.label_num_certi_reg.setText(QtGui.QApplication.translate('Orden', 'Número', None, QtGui.QApplication.UnicodeUTF8))
    self.label_fecha_certi_reg.setText(QtGui.QApplication.translate('Orden', 'Fecha', None, QtGui.QApplication.UnicodeUTF8))
    self.date_fecha_certi_reg1.setCalendarPopup(True)    
    self.date_fecha_certi_reg2.setCalendarPopup(True)
    self.date_fecha_certi_reg3.setCalendarPopup(True)
    self.text_num_certi_reg1.setMinimumWidth(120)
    self.text_num_certi_reg2.setMinimumWidth(120)
    self.text_num_certi_reg3.setMinimumWidth(120)

def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    else:
        orden = query_orden[0]
        try:
            self.text_num_certi_reg1.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerreg[0].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_reg1.setDate(datetime.date(orden.cerreg[0].get_year(), orden.cerreg[0].get_month(), orden.cerreg[0].get_day()))
            self.text_num_certi_reg2.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerreg[1].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_reg2.setDate(datetime.date(orden.cerreg[1].get_year(), orden.cerreg[1].get_month(), orden.cerreg[1].get_day()))
            self.text_num_certi_reg3.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerreg[2].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_reg3.setDate(datetime.date(orden.cerreg[2].get_year(), orden.cerreg[2].get_month(), orden.cerreg[2].get_day()))
        except:
            pass
        
def checkValidacion(self):
    if self.text_num_certi_reg1.validacion():
        if self.text_num_certi_reg2.validacion():
            if self.text_num_certi_reg3.validacion():
                fechas_app_cerreg = [self.date_fecha_certi_reg1, self.date_fecha_certi_reg2, self.date_fecha_certi_reg3]
                for index, cerreg in enumerate([self.text_num_certi_reg1, self.text_num_certi_reg2, self.text_num_certi_reg3]):
                    if len(cerreg.text()) > 0:
                        fecha_app_cerreg = datetime.date(fechas_app_cerreg[index].date().year(), fechas_app_cerreg[index].date().month(), fechas_app_cerreg[index].date().day())
                        if len(self.parent().parent().OrdenModel.get_cerreg()) > index:
                            fecha_query = self.parent().parent().OrdenModel.cerreg[index].get_fecha()
                            if self.parent().parent().OrdenModel.cerreg[index].get_numero() != u"%s"%(cerreg.text()) or fecha_query != fecha_app_cerreg:
                                self.parent().parent().OrdenModel.cerreg[index].set_numero(u"%s"%(cerreg.text()))
                                self.parent().parent().OrdenModel.cerreg[index].set_fecha(fecha_app_cerreg)
                        else:
                            self.parent().parent().OrdenModel.cerreg.append(CerregModel(u"%s"%(cerreg.text()), fecha_app_cerreg))
                    else:
                        if len(self.parent().parent().OrdenModel.get_cerreg()) > index:
                            session.delete(self.parent().parent().OrdenModel.cerreg[index])
                return True                
    return False

def Save(self):
    if self.check_validacion():
        return True
    return False
