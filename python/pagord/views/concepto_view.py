#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoParrafo
from controllers.concepto_controller import initData, translateView, updateData, checkValidacion, Save

class ConceptoView(QtGui.QGroupBox):
    def __init__(self, parent=None):
        super(ConceptoView, self).__init__(parent)

        self.fila_concepto = QtGui.QVBoxLayout()
        self.text_concepto = CampoParrafo(self, u"Concepto")

        self.fila_concepto.addWidget(self.text_concepto)
        
        self.setLayout(self.fila_concepto)
        self.translate_view()

    init_data = initData
    translate_view = translateView
    update_data = updateData
    check_validacion = checkValidacion
    save = Save