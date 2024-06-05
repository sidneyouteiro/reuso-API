from pydantic import BaseModel
from typing import List, Optional

class InputBase(BaseModel):
    nome: str
    tipo: str

class InputCreate(InputBase):
    pass

class Input(InputBase):
    id: int

    class Config:
        orm_mode = True

class OutputBase(BaseModel):
    nome: str
    tipo: str

class OutputCreate(OutputBase):
    pass

class Output(OutputBase):
    id: int

    class Config:
        orm_mode = True

class ExcecaoBase(BaseModel):
    tipo: str

class ExcecaoCreate(ExcecaoBase):
    pass

class Excecao(ExcecaoBase):
    id: int

    class Config:
        orm_mode = True

class RequisitoBase(BaseModel):
    titulo: str
    descricao: str

class RequisitoCreate(RequisitoBase):
    inputs: List[InputCreate] = []
    outputs: List[OutputCreate] = []
    excecoes: List[ExcecaoCreate] = []

class RequisitoUpdate(RequisitoBase):
    inputs: List[InputCreate] = []
    outputs: List[OutputCreate] = []
    excecoes: List[ExcecaoCreate] = []

class Requisito(RequisitoBase):
    id: int
    inputs: List[Input] = []
    outputs: List[Output] = []
    excecoes: List[Excecao] = []

    class Config:
        orm_mode = True