# -*- coding: utf-8 -*-

from models import Base, Column, Integer, ForeignKey, Boolean

class OpcionesModel(Base):
    __tablename__='opciones'
    
    id = Column(Integer, primary_key=True)
    pago_final = Column(Boolean)
    monto = Column(Integer)
    anulada = Column(Boolean)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    ord_rel = Column(Integer)
    
    def __init__(self, pago_final, monto, anulada, ord_rel):
        self.pago_final = pago_final
        self.monto = monto
        self.anulada = anulada
        self.ord_rel = u"" if (ord_rel == None) else ord_rel
        
    def __repr__(self):
        return u"<Opciones>"
    
    def get_pago_final(self):
        return self.pago_final
    
    def get_monto(self):
        return self.monto
    
    def get_anulada(self):
        return self.anulada
    
    def get_orden_relacionada(self):
        return self.ord_rel
    
    def set_pago_final(self, pago_final):
        self.pago_final = pago_final
        
    def set_monto(self, monto):
        self.monto = 0 if (monto == u"" or monto == None) else int(monto)
    
    def set_anulada(self, anulada):
        self.anulada = anulada
        
    def set_orden_relacionada(self, ord_rel):
        self.ord_rel = u"" if (ord_rel == u"" or ord_rel == None) else int(ord_rel)