# -*- coding: utf-8 -*-

import codecs
from encodings import utf_8
from models import Base, Column, Date, Integer, ForeignKey, relationship, String
from beneficiario_model import BeneficiarioModel
from cerdisp_model import CerdispModel
from cerreg_model import CerregModel
from discriminacion_model import DiscriminacionModel
from opciones_model import OpcionesModel

class OrdenModel(Base):
    __tablename__='orden'
    
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fecha = Column(Date)
    bien_servicio = Column(Integer)
    rubro = Column(String(30))
    beneficiario_id = Column(Integer, ForeignKey('beneficiario.id'))
    #rubro = Column(String(50))
    #concepto = relationship('Concepto', backref='orden', cascade='all, delete-orphan')
    #comprobante = relationship('Comprobante', backref='orden', cascade='all, delete-orphan')
    #infocond = relationship('Infocond', backref='orden', cascade='all, delete-orphan')
    #beneficiario = relationship('BeneficiarioModel', backref='orden', cascade='all, delete-orphan')
    cerdisp = relationship('CerdispModel', backref='orden', cascade='all, delete-orphan')
    cerreg = relationship('CerregModel', backref='orden', cascade='all, delete-orphan')
    discriminacion = relationship('DiscriminacionModel', backref='orden', cascade='all, delete-orphan')
    opciones = relationship('OpcionesModel', backref='orden', cascade='all, delete-orphan')
    
    def __init__(self, numero, fecha, bien_servicio, rubro):
        self.numero = numero
        self.fecha = fecha
        self.bien_servicio = bien_servicio
        self.rubro = rubro
  
    def __repr__(self):
        return u"<Orden (%s)>"%(self.numero)
    
    def get_numero(self):
        return int(self.numero)
    
    def get_fecha(self):
        return self.fecha
    
    def get_bien_servicio(self):
        return u"%s"%(self.bien_servicio)
    
    def get_rubro(self):
        return self.rubro
    
    def get_concepto(self):
        try:
            file_concepto = codecs.open(u"concepto/%s.txt"%(self.get_numero()), mode='r', encoding='utf-8')
            concepto = file_concepto.read()
            file_concepto.close()
        except:
            concepto = u""
        return concepto
    
    def get_beneficiario(self):
        return self.beneficiario
    
    def get_cerdisp(self):
        return self.cerdisp
    
    def get_cerreg(self):
        return self.cerreg
    
    def get_discriminacion(self):
        return self.discriminacion
    
    def get_opciones(self):
        return self.opciones
    
    def set_fecha(self, fecha):
        self.fecha = fecha
        
    def set_bien_servicio(self, bien_servicio):
        self.bien_servicio = bien_servicio
        
    def set_rubro(self, rubro):
        self.rubro = rubro
    
    def set_beneficiario(self, beneficiario):
        self.beneficiario = beneficiario
