#-*- coding: utf-8 -*-

import datetime
from PyQt4 import QtGui
from models.models import session
from models.cerdisp_model import CerdispModel

def initData(self, query_orden):
    self.text_num_certi_disp1.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_num_certi_disp2.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.text_num_certi_disp3.setText(QtGui.QApplication.translate('Orden', u"", None, QtGui.QApplication.UnicodeUTF8))
    self.date_fecha_certi_disp1.setDate(datetime.date.today())
    self.date_fecha_certi_disp2.setDate(datetime.date.today())
    self.date_fecha_certi_disp3.setDate(datetime.date.today())

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Certificados de disponibilidad', None, QtGui.QApplication.UnicodeUTF8))
    self.label_num_certi_disp.setText(QtGui.QApplication.translate('Orden', 'Número', None, QtGui.QApplication.UnicodeUTF8))
    self.label_fecha_certi_disp.setText(QtGui.QApplication.translate('Orden', 'Fecha', None, QtGui.QApplication.UnicodeUTF8))
    self.text_num_certi_disp1.setMinimumWidth(120)
    self.text_num_certi_disp2.setMinimumWidth(120)
    self.text_num_certi_disp3.setMinimumWidth(120)
    self.date_fecha_certi_disp1.setCalendarPopup(True)
    self.date_fecha_certi_disp2.setCalendarPopup(True)
    self.date_fecha_certi_disp3.setCalendarPopup(True)

def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    else:
        orden = query_orden[0]
        try:
            self.text_num_certi_disp1.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerdisp[0].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_disp1.setDate(datetime.date(orden.cerdisp[0].get_year(), orden.cerdisp[0].get_month(), orden.cerdisp[0].get_day()))
            self.text_num_certi_disp2.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerdisp[1].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_disp2.setDate(datetime.date(orden.cerdisp[1].get_year(), orden.cerdisp[1].get_month(), orden.cerdisp[1].get_day()))
            self.text_num_certi_disp3.setText(QtGui.QApplication.translate('Orden', u"%s"%(orden.cerdisp[2].get_numero()), None, QtGui.QApplication.UnicodeUTF8))
            self.date_fecha_certi_disp3.setDate(datetime.date(orden.cerdisp[2].get_year(), orden.cerdisp[2].get_month(), orden.cerdisp[2].get_day()))
        except:
            pass

def checkValidacion(self):
    if self.text_num_certi_disp1.validacion():
        if self.text_num_certi_disp2.validacion():
            if self.text_num_certi_disp3.validacion():
                fechas_app_cerdisp = [self.date_fecha_certi_disp1, self.date_fecha_certi_disp2, self.date_fecha_certi_disp3]
                for index, cerdisp in enumerate([self.text_num_certi_disp1, self.text_num_certi_disp2, self.text_num_certi_disp3]):
                    if len(cerdisp.text()) > 0:
                        fecha_app_cerdisp = datetime.date(fechas_app_cerdisp[index].date().year(), fechas_app_cerdisp[index].date().month(), fechas_app_cerdisp[index].date().day())
                        if len(self.parent().parent().OrdenModel.get_cerdisp()) > index:
                            fecha_query = self.parent().parent().OrdenModel.cerdisp[index].get_fecha()
                            if self.parent().parent().OrdenModel.cerdisp[index].get_numero() != u"%s"%(cerdisp.text()) or fecha_query != fecha_app_cerdisp:
                                self.parent().parent().OrdenModel.cerdisp[index].set_numero(u"%s"%(cerdisp.text()))
                                self.parent().parent().OrdenModel.cerdisp[index].set_fecha(fecha_app_cerdisp)
                        else:
                            self.parent().parent().OrdenModel.cerdisp.append(CerdispModel(u"%s"%(cerdisp.text()), fecha_app_cerdisp))
                    else:
                        if len(self.parent().parent().OrdenModel.get_cerdisp()) > index:
                            session.delete(self.parent().parent().OrdenModel.cerdisp[index])
                return True
    return False

def Save(self):
    if self.check_validacion():
        return True
    return False
