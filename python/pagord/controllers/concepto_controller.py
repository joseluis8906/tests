#-*- coding: utf-8 -*-

import codecs
from encodings import utf_8
from PyQt4 import QtGui

def initData(self, query_orden):
    self.text_concepto.setPlainText(u"")

def translateView(self):
    self.setTitle(QtGui.QApplication.translate('Orden', 'Concepto', None, QtGui.QApplication.UnicodeUTF8))
    
def updateData(self, query_orden):
    if(len(query_orden)==0):
        self.init_data(query_orden)
    try:
        file_concepto = codecs.open(u"concepto/%s.txt"%(self.parent().orden_view.text_numero.text()), mode='r', encoding='utf-8')
        concepto = file_concepto.read()
        file_concepto.close()
        self.text_concepto.setPlainText(u"%s"%(concepto))
    except:
        pass

def checkValidacion(self):
    if self.text_concepto.validacion(obligatorio=True):
        return True
    return False
    
def Save(self):
    if self.check_validacion():
        if len(self.text_concepto.toPlainText()) > 0:
            file_concepto = codecs.open(u"concepto/%s.txt"%(self.parent().orden_view.text_numero.text()), mode='w', encoding='utf-8')
            file_concepto.write(u"%s"%(self.text_concepto.toPlainText()))
            file_concepto.close()        
        return True
    return False
