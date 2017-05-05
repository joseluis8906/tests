# -*- coding: utf-8 -*-

from models import Base, Column, ForeignKey, Integer, String, Float, Boolean

class DiscriminacionModel(Base):
    __tablename__='discriminacion'
    
    id = Column(Integer, primary_key=True)
    iva = Column(Integer)
    ret_fuente = Column(Float)
    ret_iva = Column(Float)
    auto_retenedor = Column(Boolean)
    imp_municipales = Column(Boolean)
    otros_concepto = Column(String(120))
    otros_valor = Column(String(120))
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, iva, ret_fuente, ret_iva, auto_retenedor, imp_municipales, otros_concepto, otros_valor):
        self.iva = 0 if (iva == u"" or iva == None) else int(iva)
        self.ret_fuente = 0.0 if (ret_fuente == u"" or ret_fuente == None) else float(ret_fuente)
        self.ret_iva = 0.0 if (ret_iva == u"" or ret_iva == None) else float(ret_iva)
        self.auto_retenedor = auto_retenedor
        self.imp_municipales = imp_municipales
        self.otros_concepto = otros_concepto
        self.otros_valor = otros_valor
        
    def __repr__(self):
        return u"<Discriminación>"
    
    def get_iva(self):
        return self.iva
    
    def get_ret_fuente(self):
        return self.ret_fuente
    
    def get_ret_iva(self):
        return self.ret_iva
    
    def get_auto_retenedor(self):
        return self.auto_retenedor
    
    def get_imp_municipales(self):
        return self.imp_municipales
    
    def get_otros_concepto(self):
        return self.otros_concepto
    
    def get_otros_valor(self):
        return self.otros_valor
    
    def set_iva(self, iva):
        self.iva = 0 if (iva == u"" or iva == None) else int(iva)
        
    def set_ret_fuente(self, ret_fuente):
        self.ret_fuente = 0.0 if (ret_fuente == u"" or ret_fuente == None) else float(ret_fuente)
        
    def set_ret_iva(self, ret_iva):
        self.ret_iva = 0.0 if (ret_iva == u"" or ret_iva == None) else float(ret_iva)
        
    def set_auto_retenedor(self, auto_retenedor):
        self.auto_retenedor = auto_retenedor

    def set_imp_municipales(self, imp_municipales):
        self.imp_municipales = imp_municipales
        
    def set_otros_concepto(self, otros_concepto):
        self.otros_concepto = otros_concepto
        
    def set_otros_valor(self, otros_valor):
        self.otros_valor = otros_valor