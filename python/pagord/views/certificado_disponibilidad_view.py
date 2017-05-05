#-*- coding: utf-8 -*-

from PyQt4 import QtGui
from campos import CampoCad
from controllers.certificado_disponibilidad_controller import initData, translateView, updateData, checkValidacion, Save

class CertificadoDisponibilidadView(QtGui.QGroupBox):
    def __init__(self, parent=None):
        super(CertificadoDisponibilidadView, self).__init__(parent)
    
        self.conten_colum_certi_disp = QtGui.QHBoxLayout()
        self.columna_num_certi_disp = QtGui.QVBoxLayout()
        self.columna_fechas_certi_disp = QtGui.QVBoxLayout()
        self.label_num_certi_disp = QtGui.QLabel(self)
        self.label_fecha_certi_disp = QtGui.QLabel(self)
        self.text_num_certi_disp1 = CampoCad(self, u"Certificado Disponibilidad 1")
        self.date_fecha_certi_disp1 = QtGui.QDateEdit(self)
        self.text_num_certi_disp2 = CampoCad(self, u"Certificado Disponibilidad 2")
        self.date_fecha_certi_disp2 = QtGui.QDateEdit(self)
        self.text_num_certi_disp3 = CampoCad(self, u"Certificado Disponibilidad 3")
        self.date_fecha_certi_disp3 = QtGui.QDateEdit(self)
    
        self.conten_colum_certi_disp.addLayout(self.columna_num_certi_disp)
        self.conten_colum_certi_disp.addLayout(self.columna_fechas_certi_disp)
    
        self.columna_num_certi_disp.addWidget(self.label_num_certi_disp)
        self.columna_fechas_certi_disp.addWidget(self.label_fecha_certi_disp)
        self.columna_num_certi_disp.addWidget(self.text_num_certi_disp1)
        self.columna_fechas_certi_disp.addWidget(self.date_fecha_certi_disp1)
        self.columna_num_certi_disp.addWidget(self.text_num_certi_disp2)
        self.columna_fechas_certi_disp.addWidget(self.date_fecha_certi_disp2)
        self.columna_num_certi_disp.addWidget(self.text_num_certi_disp3)
        self.columna_fechas_certi_disp.addWidget(self.date_fecha_certi_disp3)
    
        self.setLayout(self.conten_colum_certi_disp)
        self.translate_view()
    
    init_data = initData
    translate_view = translateView
    update_data = updateData
    check_validacion = checkValidacion
    save = Save