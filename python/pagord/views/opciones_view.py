#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoNum, CampoOrdRel
from controllers.opciones_controller import initData, translateView, updateData, habilitarMonto, checkValidacion, Save

class OpcionesView(QtGui.QGroupBox):
    def __init__(self, parent):
        super(OpcionesView, self).__init__(parent)
        
        self.checkbox_pago_final = QtGui.QCheckBox(self)
        self.label_pago_final = QtGui.QLabel(self)
        self.text_monto= CampoNum(self, u"Monto")
        self.checkbox_anulada = QtGui.QCheckBox(self)
        self.label_orden_relacionada = QtGui.QLabel(self)
        self.text_orden_relacionada = CampoOrdRel(self, u"Orden Relacionada")
        
        self.fila_pago_final = QtGui.QHBoxLayout()
        self.contenedor_opciones = QtGui.QVBoxLayout()
        
        self.fila_pago_final.addWidget(self.checkbox_pago_final)
        self.fila_pago_final.addWidget(self.label_pago_final)
        self.fila_pago_final.addWidget(self.text_monto)
        self.fila_pago_final.addWidget(self.label_orden_relacionada)
        self.fila_pago_final.addWidget(self.text_orden_relacionada)
        
        self.contenedor_opciones.addLayout(self.fila_pago_final)
        self.contenedor_opciones.addWidget(self.checkbox_anulada)
        
        self.setLayout(self.contenedor_opciones)
        
        self.checkbox_pago_final.clicked.connect(self.habilitar_monto)
        self.translate_view()
    
    init_data = initData 
    translate_view = translateView
    update_data = updateData
    habilitar_monto = habilitarMonto
    check_validacion = checkValidacion
    save = Save