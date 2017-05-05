from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date, Boolean
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db/hosapp.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = Base.metadata


class Orden(Base):
    __tablename__='orden'
    
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fecha = Column(Date)
    compromiso = Column(Integer)
    rubro = Column(String(50))
    
    beneficiario = relationship("Beneficiario", backref='orden', cascade='all, delete-orphan')
    concepto = relationship('Concepto', backref='orden', cascade='all, delete-orphan')
    comprobante = relationship('Comprobante', backref='orden', cascade='all, delete-orphan')
    infocond = relationship('Infocond', backref='orden', cascade='all, delete-orphan')
    discriminacion = relationship('Discriminacion', backref='orden', cascade='all, delete-orphan')
    
    def __init__(self, numero, fecha, compromiso, rubro):
        self.numero = numero
        self.fecha = fecha
        self.compromiso = compromiso
        self.rubro = rubro
  
    def __repr__(self):
        return "<Orden (%s)>"%(self.numero)
        
class Beneficiario(Base):
    __tablename__='beneficiario'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(Text)
    nit = Column(String(30))
    orden_id = Column(Integer, ForeignKey('orden.id'))

    cerdisp = relationship('Cerdisp', backref='beneficiario', cascade='all, delete-orphan')
    cerreg = relationship('Cerreg', backref='beneficiario', cascade='all, delete-orphan')
    
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def __repr__(self):
        return "<Beneficiario (%s, %s)>"%(self.nombre, self.nit)
        

        
class Cerdisp(Base):
    __tablename__='cerdisp'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(30))
    fecha = Column(String(30))
    beneficiario_id = Column(Integer, ForeignKey('beneficiario.id'))
    
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha

    def __repr__(self):
        return "<Cerdisp (%s, %s)>"%(self.numero, self.fecha)
        
class Cerreg(Base):
    __tablename__='cerreg'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(30))
    fecha = Column(String(30))
    beneficiario_id = Column(Integer, ForeignKey('beneficiario.id'))
    
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha

    def __repr__(self):
        return "<Cerreg (%s, %s)>"%(self.numero, self.fecha)
        

class Concepto(Base):
    __tablename__='concepto'
    
    id = Column(Integer, primary_key=True)
    descripcion = Column(Text)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
        return "<Concepto (%s)>"%(self.descripcion)
        
class Comprobante(Base):
    __tablename__='comprobante'
    
    id = Column(Integer, primary_key=True)
    numero = Column(String(30))
    fecha = Column(Date)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, numero, fecha):
        self.numero = numero
        self.fecha = fecha
        
    def __repr__(self):
        return "<Comprobante (%s)>"%(self.numero)

class Infocond(Base):
    __tablename__='infocond'
    
    id = Column(Integer, primary_key=True)
    cheque = Column(String(50))
    cuenta = Column(String(50))
    codigo = Column(String(30))
    valor = Column(Integer)
    fecha = Column(String(15))
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, cheque, cuenta, codigo, valor, fecha):
        self.cheque = cheque
        self.cuenta = cuenta
        self.codigo = codigo
        self.valor = valor
        self.fecha = fecha

    def __repr__(self):
        return "<Infocond (cheque: %s cuenta: %s)>"%(self.cheque, self.cuenta)

class Discriminacion(Base):
    __tablename__='discriminacion'
    
    id = Column(Integer, primary_key=True)
    iva = Column(Integer)
    ret_fuente = Column(String(5))
    ret_iva = Column(Boolean)
    imp_municipales = Column(Boolean)
    #est_pdf = Column(Boolean)
    #com_recaudo = Column(Boolean)
    otros_concepto = Column(String(120))
    otros = Column(String(120))
    monto = Column(Integer)
    bien_servicio = Column(Integer)
    pago_final = Column(Boolean)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, iva, ret_fuente, ret_iva, imp_municipales, otros_concepto, otros, monto, bien_servicio, pago_final ):
        self.iva = iva
        self.ret_fuente = ret_fuente
        self.ret_iva = ret_iva
        self.imp_municipales = imp_municipales
        #self.est_pdf = est_pdf
        #self.com_recaudo = com_recaudo
        self.otros_concepto = otros_concepto
        self.otros = otros
        self.monto = monto
        self.bien_servicio = bien_servicio
        self.pago_final = pago_final

    def __repr__(self):
        return "<Discriminacion (realizado)>"
