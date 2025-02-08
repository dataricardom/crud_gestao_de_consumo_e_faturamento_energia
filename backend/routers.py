from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ClienteResponse, ClienteUpdate, ClienteCreate
from schemas import LeituraResponse, LeituraUpdate, LeituraCreate
from schemas import MedidorResponse, MedidorUpdate, MedidorCreate
from schemas import FaturaResponse, FaturaUpdate, FaturaCreate
from typing import List
from crud import (get_clientes,
                  get_cliente,
                  create_cliente,
                  delete_cliente,
                  update_cliente,
                  get_medidores,
                  get_medidor,
                  create_medidor,
                  delete_medidor,
                  update_medidor,
                  get_leituras,
                  get_leitura,
                  create_leitura,
                  delete_leitura,
                  update_leitura,
                  get_faturas,
                  get_fatura,
                  create_fatura,
                  delete_fatura,
                  update_fatura
                  )

routers = APIRouter()


@routers.post("/cliente/", response_model= ClienteResponse)
def create_cliente_route(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db=db, cliente=cliente)

@routers.get("/cliente/", response_model=List[ClienteResponse])
def read_all_clientes_route(db: Session = Depends(get_db)):
    clientes = get_clientes(db)
    return clientes

@routers.get("/cliente/{cliente_id}", response_model=ClienteResponse)
def read_one_clientes_route(cliente_id:int , db: Session = Depends(get_db)):
    db_cliente = get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail= "Você esta procurando um Cliente que não existe")
    return db_cliente


@routers.delete("/cliente/{cliente_id}", response_model=ClienteResponse)
def delete_product_route(cliente_id: int, db: Session = Depends(get_db)):
    cliente_db = delete_cliente(cliente_id=cliente_id, db=db)
    
    if cliente_db is None:

        raise HTTPException(status_code=404, detail= "Você esta tentando deletar um Cliente que não existe")
    return cliente_db


@routers.put("/cliente/{cliente_id}", response_model=ClienteResponse)
def update_product_route(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    cliente_db = update_cliente(db=db, cliente_id=cliente_id, cliente=cliente)
    
    if cliente_db is None:

        raise HTTPException(status_code=404, detail= "Você esta tentando atualizar dados de um Cliente que não existe")
    return cliente_db


# Rota Medidor


@routers.post("/medidor/", response_model=MedidorResponse)
def create_medidor_route(medidor: MedidorCreate, db: Session = Depends(get_db)):
    return create_medidor(db=db, medidor=medidor)


@routers.get("/medidor/", response_model=List[MedidorResponse])
def read_all_medidores_route(db: Session = Depends(get_db)):
    medidores = get_medidores(db)
    return medidores

@routers.get("/medidor/{medidor_id}", response_model=MedidorResponse)
def read_one_medidor_route(medidor_id: int, db: Session = Depends(get_db)):
    db_medidor = get_medidor(db, medidor_id=medidor_id)
    if db_medidor is None:
        raise HTTPException(status_code=404, detail="Medidor não encontrado")
    return db_medidor

@routers.delete("/medidor/{medidor_id}", response_model=MedidorResponse)
def delete_medidor_route(medidor_id: int, db: Session = Depends(get_db)):
    db_medidor = delete_medidor(db=db, medidor_id=medidor_id)
    if db_medidor is None:
        raise HTTPException(status_code=404, detail="Medidor não encontrado")
    return db_medidor

@routers.put("/medidor/{medidor_id}", response_model=MedidorResponse)
def update_medidor_route(medidor_id: int, medidor: MedidorUpdate, db: Session = Depends(get_db)):
    db_medidor = update_medidor(db=db, medidor_id=medidor_id, medidor=medidor)
    if db_medidor is None:
        raise HTTPException(status_code=404, detail="Medidor não encontrado")
    return db_medidor

# Rota Leituras 

@routers.post("/leitura/", response_model=LeituraResponse)
def create_leitura_route(leitura: LeituraCreate, db: Session = Depends(get_db)):
    return create_leitura(db=db, leitura=leitura)

@routers.get("/leitura/", response_model=List[LeituraResponse])
def read_all_leituras_route(db: Session = Depends(get_db)):
    leituras = get_leituras(db)
    return leituras

@routers.get("/leitura/{leitura_id}", response_model=LeituraResponse)
def read_one_leitura_route(leitura_id: int, db: Session = Depends(get_db)):
    db_leitura = get_leitura(db, leitura_id=leitura_id)
    if db_leitura is None:
        raise HTTPException(status_code=404, detail="Leitura não encontrada")
    return db_leitura

@routers.delete("/leitura/{leitura_id}", response_model=LeituraResponse)
def delete_leitura_route(leitura_id: int, db: Session = Depends(get_db)):
    db_leitura = delete_leitura(db=db, leitura_id=leitura_id)
    if db_leitura is None:
        raise HTTPException(status_code=404, detail="Leitura não encontrada")
    return db_leitura

@routers.put("/leitura/{leitura_id}", response_model=LeituraResponse)
def update_leitura_route(leitura_id: int, leitura: LeituraUpdate, db: Session = Depends(get_db)):
    db_leitura = update_leitura(db=db, leitura_id=leitura_id, leitura=leitura)
    if db_leitura is None:
        raise HTTPException(status_code=404, detail="Leitura não encontrada")
    return db_leitura

#Rota Fatura

@routers.post("/fatura/", response_model=FaturaResponse)
def create_fatura_route(fatura: FaturaCreate, db: Session = Depends(get_db)):
    return create_fatura(db=db, fatura=fatura)

@routers.get("/fatura/", response_model=List[FaturaResponse])
def read_all_faturas_route(db: Session = Depends(get_db)):
    faturas = get_faturas(db)
    return faturas

@routers.get("/fatura/{fatura_id}", response_model=FaturaResponse)
def read_one_fatura_route(fatura_id: int, db: Session = Depends(get_db)):
    db_fatura = get_fatura(db, fatura_id=fatura_id)
    if db_fatura is None:
        raise HTTPException(status_code=404, detail="Fatura não encontrada")
    return db_fatura

@routers.delete("/fatura/{fatura_id}", response_model=FaturaResponse)
def delete_fatura_route(fatura_id: int, db: Session = Depends(get_db)):
    db_fatura = delete_fatura(db=db, fatura_id=fatura_id)
    if db_fatura is None:
        raise HTTPException(status_code=404, detail="Fatura não encontrada")
    return db_fatura

@routers.put("/fatura/{fatura_id}", response_model=FaturaResponse)
def update_fatura_route(fatura_id: int, fatura: FaturaUpdate, db: Session = Depends(get_db)):
    db_fatura = update_fatura(db=db, fatura_id=fatura_id, fatura=fatura)
    if db_fatura is None:
        raise HTTPException(status_code=404, detail="Fatura não encontrada")
    return db_fatura
