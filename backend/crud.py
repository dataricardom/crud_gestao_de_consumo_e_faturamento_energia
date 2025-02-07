from sqlalchemy.orm import Session
from schemas import ClienteUpdate, ClienteCreate
from schemas import FaturaCreate , FaturaUpdate
from schemas import MedidorUpdate, MedidorCreate
from schemas import LeituraUpdate, LeituraCreate
from models import ClienteModel, FaturaModel, MedidorModel, LeituraModel

# Crud Tabela Cliente

def get_clientes(db:Session):
    
    return db.query(ClienteModel).all()

def get_cliente(db:Session, cliente_id: int):
   
    return db.query(ClienteModel).filter(ClienteModel.id_cliente == cliente_id).first()

def create_cliente(db: Session, cliente: ClienteCreate):
    
    db_cliente = ClienteModel(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def delete_cliente(db: Session, cliente_id: int):
    
    db_cliente = db.query(ClienteModel).filter(ClienteModel.id_cliente == cliente_id).first()
    db.delete(db_cliente)
    db.commit()
    return db_cliente

def update_cliente(db:Session, cliente_id: int, cliente: ClienteUpdate):
    
    db_cliente = db.query(ClienteModel).filter(ClienteModel.id_cliente == cliente_id).first()
    if db_cliente is None:
        return None
    if cliente.endereco is not None:
        db_cliente.nome = cliente.endereco
    if cliente.telefone is not None:
        db_cliente.telefone = cliente.telefone
    if cliente.email_cliente is not None:
        db_cliente.email_cliente = cliente.email_cliente
    
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Crud Tabela Medidor

def get_medidores(db:Session):
    
    return db.query(MedidorModel).all()

def get_medidor(db:Session, cliente_id: int):
   
    return db.query(MedidorModel).filter(MedidorModel.id_medidor == cliente_id).first()

def create_medidor(db: Session, medidor: MedidorCreate):
    
    db_medidor = MedidorModel(**medidor.model_dump())
    db.add(db_medidor)
    db.commit()
    db.refresh(db_medidor)
    return db_medidor


def delete_medidor(db: Session, medidor_id: int):
    
    db_medidor = db.query(MedidorModel).filter(MedidorModel.id_medidor == medidor_id).first()
    db.delete(db_medidor)
    db.commit()
    return db_medidor

def update_medidor(db:Session, medidor_id: int, medidor: MedidorUpdate):
    
    db_medidor = db.query(MedidorModel).filter(MedidorModel.id_medidor == medidor_id).first()
    if db_medidor is None:
        return None
    if medidor.numero_medidor is not None:
        db_medidor.numero_medidor = medidor.numero_medidor
    if medidor.tipo is not None:
        db_medidor.tipo = medidor.tipo
    db.commit()
    db.refresh(db_medidor)
    return db_medidor
   

# Crud Tabela Leitura

def get_leituras(db:Session):
    
    return db.query(LeituraModel).all()

def get_leitura(db:Session, leitura_id: int):
    
    return db.query(LeituraModel).filter(LeituraModel.id_leitura == leitura_id).first()

def create_leitura(db:Session, leitura_id: int):
    
    db_leitura = db.query(LeituraModel).filter(LeituraModel.id_leitura == leitura_id)
    db.delete(db_leitura)
    db.commit()
    return db_leitura

def update_medidor(db:Session, leitura_id: int, leitura: LeituraUpdate):
    
    db_leitura = db.query(LeituraModel).filter(LeituraModel.id_leitura == leitura_id).first()
    if db_leitura is None:
        return None
    if leitura.leitura_kwh is not None:
        db_leitura.leitura_kwh = leitura.leitura_kwh
    db.commit()
    db.refresh(db_leitura)
    return db_leitura




# Crud Tabela Fatura



def get_faturas(db:Session):
   
    return db.query(FaturaModel).all()

def get_fatura(db:Session, fatura_id: int):
    
    return db.query(FaturaModel).filter(FaturaModel.id_fatura == fatura_id).first()

def create_fatura(db:Session, fatura_id: int):
    
    db_fatura = db.query(FaturaModel).filter(FaturaModel.id_fatura == fatura_id)
    db.delete(db_fatura)
    db.commit()
    return db_fatura

def update_fatura(db:Session, fatura_id: int, fatura: FaturaUpdate):
    
    db_fatura = db.query(FaturaModel).filter(FaturaModel.id_fatura == fatura_id).first()
    
    if db_fatura is None:
        return None
    if fatura.valor is not None:
        db_fatura.valor = fatura.valor
    if fatura.status_pagamento is not None:
        db_fatura.status_pagamento = fatura.status_pagamento
    db.commit()
    db.refresh(db_fatura)
    return db_fatura
