from pydantic import BaseModel, PositiveFloat, EmailStr, validator
from enum import Enum
from datetime import datetime
from typing import Optional

#Schemas Tabela Cliente:

class ClienteBase(BaseModel):
    nome:str
    endereco:str
    telefone:str
    email_cliente: EmailStr

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id_cliente: int
    data_cadastro: datetime

    class Config:
        from_attributes = True

class ClienteUpdate(BaseModel):
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    email_cliente: Optional[EmailStr] = None

#Schemas Tabela Medidor

class MedidorBase(BaseModel):
    client_id: int
    numero_medidor: int
    tipo:str

class MedidorCreate(MedidorBase):
    pass

class MedidorResponse(MedidorBase):
    medidor_id: int
    data_instalacao:datetime
    
    class Config:
        from_attributes= True

class MedidorUpdate (BaseModel):
    client_id: int
    numero_medidor: Optional [int] = None
    tipo:Optional[str] = None


#Schemas Tabela Leitura

class LeituraBase(BaseModel):
    medidor_id: int
    leitura_kwh: PositiveFloat

class LeituraCreate(LeituraBase):
    pass 

class LeituraResponse(LeituraBase):
    id_leitura:int
    data_leitura:datetime

    class Config:
        from_attributes = True

class LeituraUpdate(BaseModel):
    
    leitura_kwh:Optional[PositiveFloat] = None

# Schemas Tabela Fatura

class FaturaBase(BaseModel):
    valor: PositiveFloat
    status_pagamento: str
class FaturaCreate(FaturaBase):
    pass 

class FaturaResponse(FaturaBase):
    id_fatura:int
    mes_referencia:datetime
    data_emissao:datetime
    data_vencimento:datetime

    class Config:
        from_attributes = True

class FaturaUpdate(BaseModel):
    valor: Optional[PositiveFloat] = None
    status_pagamento: Optional[str] = None