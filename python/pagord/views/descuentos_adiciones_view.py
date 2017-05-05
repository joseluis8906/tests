#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoNum, CampoCad, CampoDec, ConceptoOtros, ValorOtros
from controllers.descuentos_adiciones_controller import initData, translateView, updateData, checkValidacion, Save

class DescuentosAdicionesView(QtGui.QGroupBox):
    def __init__(self, parent=None):
        super(DescuentosAdicionesView, self).__init__(parent)
        self.contenedor_descuentos = QtGui.QHBoxLayout()
        self.columna1 = QtGui.QVBoxLayout()
        self.columna2 = QtGui.QVBoxLayout()
        self.columna3 = QtGui.QVBoxLayout()
        
        self.columna_auto_retenedor = QtGui.QVBoxLayout()
        self.columna_imp_municipales = QtGui.QVBoxLayout()
        self.fila_columnas_checkbox = QtGui.QHBoxLayout()

        self.label_iva = QtGui.QLabel(self)
        self.text_iva = CampoNum(self, u"Iva")
        self.label_ret_iva = QtGui.QLabel(self)
        self.text_ret_iva = CampoDec(self, u"Reteiva")
        self.label_imp_municipales = QtGui.QLabel(self)
        self.checkbox_imp_municipales = QtGui.QCheckBox(self)
        self.label_auto_retenedor = QtGui.QLabel(self)
        self.checkbox_auto_retenedor = QtGui.QCheckBox(self)
        self.label_ret_fuente = QtGui.QLabel(self)
        self.text_ret_fuente = CampoDec(self, u"Retefuente")
        self.label_otros_concepto = QtGui.QLabel(self)
        self.text_otros_concepto = ConceptoOtros(self, u"Concepto Otros")
        self.label_otros = QtGui.QLabel(self)
        self.text_otros_valor = ValorOtros(self, u"Valor Otros")

        self.contenedor_descuentos.addLayout(self.columna1)
        self.contenedor_descuentos.addLayout(self.columna2)
        self.contenedor_descuentos.addLayout(self.columna3)

        self.columna1.addWidget(self.label_iva)
        self.columna1.addWidget(self.text_iva)
        self.columna1.addWidget(self.label_ret_iva)
        self.columna1.addWidget(self.text_ret_iva)

        self.columna2.addWidget(self.label_ret_fuente)
        self.columna2.addWidget(self.text_ret_fuente)
        self.columna2.addLayout(self.fila_columnas_checkbox)

        self.fila_columnas_checkbox.addLayout(self.columna_auto_retenedor)
        self.fila_columnas_checkbox.addLayout(self.columna_imp_municipales)

        self.columna_auto_retenedor.addWidget(self.label_auto_retenedor)
        self.columna_auto_retenedor.addWidget(self.checkbox_auto_retenedor)

        self.columna_imp_municipales.addWidget(self.label_imp_municipales)
        self.columna_imp_municipales.addWidget(self.checkbox_imp_municipales)

        self.columna3.addWidget(self.label_otros_concepto)
        self.columna3.addWidget(self.text_otros_concepto)
        self.columna3.addWidget(self.label_otros)
        self.columna3.addWidget(self.text_otros_valor)        

        self.setLayout(self.contenedor_descuentos)
        self.translate_view()
    
    init_data = initData
    translate_view = translateView
    update_data = updateData
    check_validacion = checkValidacion
    save = Save