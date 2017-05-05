# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date, Boolean, Float
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///models/hosapp.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
metadata = Base.metadata

"""class Concepto(Base):
    __tablename__='concepto'
    
    id = Column(Integer, primary_key=True)
    descripcion = Column(Text)
    orden_id = Column(Integer, ForeignKey('orden.id'))
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
        return u"<Concepto (%s)>"%(self.descripcion)
        
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
        return u"<Infocond (cheque: %s cuenta: %s)>"%(self.cheque, self.cuenta)"""


    
