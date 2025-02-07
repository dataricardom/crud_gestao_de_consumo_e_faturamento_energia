from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


# Tabela Cliente
class ClienteModel(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    email_cliente = Column(String)
    data_cadastro = Column(DateTime(timezone=True), default=func.now())

    # Relacionamento com Medidor
    medidores = relationship("MedidorModel", back_populates="cliente")
    
    # Relacionamento com Fatura
    faturas = relationship("FaturaModel", back_populates="cliente")

# Tabela Medidor
class MedidorModel(Base):
    __tablename__ = "medidor"
    
    id_medidor = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id_cliente'))
    numero_medidor = Column(Integer)
    tipo = Column(String)
    data_instalacao = Column(DateTime(timezone=True), default=func.now())

    # Relacionamento com Cliente (muitos para um)
    cliente = relationship("ClienteModel", back_populates="medidores")
    
    # Relacionamento com Leitura
    leituras = relationship("LeituraModel", back_populates="medidor")

# Tabela Leitura
class LeituraModel(Base):
    __tablename__ = "leitura"

    id_leitura = Column(Integer, primary_key=True)
    medidor_id = Column(Integer, ForeignKey('medidor.id_medidor'))
    data_leitura = Column(DateTime(timezone=True), default=func.now())
    leitura_kwh = Column(Float)

    # Relacionamento com Medidor (muitos para um)
    medidor = relationship("MedidorModel", back_populates="leituras")

# Tabela Fatura
class FaturaModel(Base):
    __tablename__ = "fatura"

    id_fatura = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id_cliente'))
    mes_referencia = Column(DateTime(timezone=True), default=func.now())
    valor = Column(Float)
    status_pagamento = Column(String)
    data_emissao = Column(DateTime(timezone=True), default=func.now())
    data_vencimento = Column(DateTime(timezone=True), default=func.now() + func.interval('15 day'))

    # Relacionamento com Cliente (muitos para um)
    cliente = relationship("ClienteModel", back_populates="faturas")
