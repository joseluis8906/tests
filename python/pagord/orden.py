#! /usr/bin/python
#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
from PyQt4 import QtCore, QtGui
#from campos import CampoNum, CampoCad, CampoParrafo, CampoDec, CampoNumOrden, ConceptoOtros, ValorOtros
from models.models import session
from models.orden_model import OrdenModel
from views.barra_menu_view import BarraMenuView
from views.orden_view import OrdenView
from views.beneficiario_view import BeneficiarioView
from views.concepto_view import ConceptoView
from views.descuentos_adiciones_view import DescuentosAdicionesView
from views.opciones_view import OpcionesView
from views.dialogo_busqueda_view import DialogoBusquedaView

from informe import generar_pdf


### window principal
class OrdenUi(QtGui.QWidget):
  
  def __init__(self):
    super(OrdenUi, self).__init__()
    
    self.menubar = BarraMenuView(self)
   
    # ------------ orden ----------
    self.orden_view = OrdenView(self)
    
    # ---------- Beneficiario ------------
    self.beneficiario_view = BeneficiarioView(self)
    
    # ---------- Concepto -------------
    self.concepto_view = ConceptoView(self)
    
    # ---------- Descuentos y adiciones ------------
    self.descuentos_view = DescuentosAdicionesView(self)
     
    # ----------- Opciones ------------
    self.opciones_view = OpcionesView(self)
    
    # ---------- Contenedor -------------
    self.boton_generar = QtGui.QPushButton(self)
    
    self.container = QtGui.QVBoxLayout(self)
    self.container.addWidget(self.menubar)
    self.container.addWidget(self.orden_view)
    self.container.addWidget(self.beneficiario_view)
    self.container.addWidget(self.concepto_view)
    self.container.addWidget(self.descuentos_view)
    self.container.addWidget(self.opciones_view)
    self.container.addWidget(self.boton_generar)
    
    # --------- Funciones de inicialización del frame ------------
    self.translateUiAndLayout()
    self.initData()
    
    # --------- Manejador de eventos --------------
    self.boton_generar.clicked.connect(self.save)
    self.orden_view.text_numero.editingFinished.connect(self.updateData)
    self.setLayout(self.container)
    self.showMaximized()

  def translateUiAndLayout(self):
    """ Asignar valor a los label e inicializar correctamente  los campos date """
    self.setWindowTitle(QtGui.QApplication.translate('Orden', 'Pagord', None, QtGui.QApplication.UnicodeUTF8))
    self.setGeometry(50, 50, 300, 150)
    self.boton_generar.setText(QtGui.QApplication.translate('Orden', 'Generar', None, QtGui.QApplication.UnicodeUTF8))
    self.boton_generar.setMaximumWidth(80)
    
  def initData(self):
    query_orden = session.query(OrdenModel).all()
    self.orden_view.init_data(query_orden)
    self.beneficiario_view.init_data(query_orden)
    self.concepto_view.init_data(query_orden)
    self.descuentos_view.init_data(query_orden)
    self.opciones_view.init_data(query_orden)
    
  def updateData(self):
    query_orden = session.query(OrdenModel).filter(OrdenModel.numero==unicode(self.orden_view.text_numero.text())).all()
    self.orden_view.update_data(query_orden)
    self.beneficiario_view.update_data(query_orden)
    self.concepto_view.update_data(query_orden)
    self.descuentos_view.update_data(query_orden)
    self.opciones_view.update_data(query_orden)
  
  def save(self):
    if self.orden_view.save():
      if self.beneficiario_view.save():
        if self.concepto_view.save():
          if self.descuentos_view.save():
            if self.opciones_view.save():
              session.add(self.BeneficiarioModel)
              session.commit()
              self.initData()
              generar_pdf(self.OrdenModel)
              return True
    return False
    
  def alerta(self, info):
    self.mensaje = QtGui.QMessageBox.information(self, u"Error", u"%s"%(info), 1)
  
  def pregunta(self, info):
    self.respuesta = QtGui.QMessageBox.question(self, u"Cuidado", u"%s"%(info), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    return self.respuesta
  
  def dialogo_busqueda(self):
    self.busqueda = DialogoBusquedaView(self)
    self.busqueda.showMaximized()
    ret = self.busqueda.exec_()
  
def main():
  app = QtGui.QApplication(sys.argv)
  ex = OrdenUi()
  sys.exit(app.exec_())
  
if __name__ == '__main__':
  main()
