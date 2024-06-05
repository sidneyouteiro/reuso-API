from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from modules.database import Base

class Requisito(Base):
    __tablename__ = "Requisitos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String, index=True)
    inputs = relationship("Input", secondary="RequisitosInputs")
    outputs = relationship("Output", secondary="RequisitosOutputs")
    excecoes = relationship("Excecao", secondary="RequisitosExcecoes")

class Input(Base):
    __tablename__ = "Inputs"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String, index=True)

class Output(Base):
    __tablename__ = "Outputs"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String, index=True)

class Excecao(Base):
    __tablename__ = "Excecoes"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, index=True)

requisito_input = Table(
    'RequisitosInputs',
    Base.metadata,
    Column('requisito_id', Integer, ForeignKey('Requisitos.id'), primary_key=True),
    Column('input_id', Integer, ForeignKey('Inputs.id'), primary_key=True)
)

requisito_output = Table(
    'RequisitosOutputs',
    Base.metadata,
    Column('requisito_id', Integer, ForeignKey('Requisitos.id'), primary_key=True),
    Column('output_id', Integer, ForeignKey('Outputs.id'), primary_key=True)
)

requisito_excecao = Table(
    'RequisitosExcecoes',
    Base.metadata,
    Column('requisito_id', Integer, ForeignKey('Requisitos.id'), primary_key=True),
    Column('excecao_id', Integer, ForeignKey('Excecoes.id'), primary_key=True)
)