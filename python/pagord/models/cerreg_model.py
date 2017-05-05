# -*- coding: utf-8 -*-

from models import Base, Column, Date, Integer, ForeignKey, String

class CerregModel(Base):
    __tablename__='cerreg'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(30))
    fecha = Column(Date)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha

    def __repr__(self):
        return u"<Cerreg (%s, %s)>"%(self.numero, self.fecha)
     
    def get_numero(self):
        return int(self.numero)
    
    def get_fecha(self):
        return self.fecha
    
    def get_year(self):
        return self.fecha.year
    
    def get_month(self):
        return self.fecha.month
    
    def get_day(self):
        return self.fecha.day
    
    def set_numero(self, numero):
        self.numero = numero
        
    def set_fecha(self, fecha):
        self.fecha = fecha