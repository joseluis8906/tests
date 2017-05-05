# -*- coding: utf-8 -*-


from models import Base, Column, Integer, relationship, Text, String

class BeneficiarioModel(Base):
    __tablename__='beneficiario'
    
    id = Column(Integer, primary_key=True)
    nit = Column(String(30))
    nombre = Column(Text)
    
    orden = relationship('OrdenModel', backref='beneficiario', cascade='all, delete-orphan')
    
    
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit
    
    def __repr__(self):
        return u"<Beneficiario (%s, %s)>"%(self.nit, self.nombre)
    
    def get_nit(self):
        return u"%s"%(self.nit)
    
    def get_nombre(self):
        return u"%s"%(self.nombre)
    
    def set_nit(self, nit):
        self.nit = nit
        
    def set_nombre(self, nombre):
        self.nombre = nombre