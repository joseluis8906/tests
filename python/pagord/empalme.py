from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date, Boolean
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engineAntiguo = create_engine('sqlite:///dbAntigua/hosappAntigua.db', echo=False)
SessionAntigua = sessionmaker(bind=engineAntiguo)
sessionAntigua = SessionAntigua()
BaseAntigua = declarative_base()
metadataAntigua = BaseAntigua.metadata

engineNuevo = create_engine('sqlite:///hosapp.db', echo=False)
SessionNueva = sessionmaker(bind=engineNuevo)
sessionNueva = SessionNueva()
BaseNueva = declarative_base()
metadataNueva = BaseNueva.metadata

class Beneficiario_A(BaseAntigua):
    __tablename__='beneficiario'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(Text)
    nit = Column(String(30))
    orden_id = Column(Integer, ForeignKey('orden.id'))

    #cerdisp = relationship('Cerdisp', backref='beneficiario', cascade='all, delete-orphan')
    #cerreg = relationship('Cerreg', backref='beneficiario', cascade='all, delete-orphan')
    
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def __repr__(self):
        return "<Beneficiario (%s, %s)>"%(self.nombre, self.nit)
        
        
class Beneficiario_N(BaseNueva):
    __tablename__='beneficiario'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(Text)
    nit = Column(String(30))
    
    #orden = relationship('Orden', backref='beneficiario', cascade='all, delete-orphan')
    
    
    def __init__(self, nombre, nit):
        self.nombre = nombre
        self.nit = nit

    def __repr__(self):
        return u"<Beneficiario (%s, %s)>"%(self.nombre, self.nit)
        
if __name__ == '__main__':
    beneficiarioA = sessionAntigua.query(Beneficiario_A).first()
    beneficiarioN = Beneficiario_N(beneficiarioA.nombre, beneficiarioA.nit)
    sessionNueva.add(beneficiarioN)
    sessionNueva.commit()
    print beneficiarioN