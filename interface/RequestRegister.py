from pydantic import BaseModel, Field
from datetime import datetime


class RequestRegister(BaseModel):
    nome: str = Field(..., min_length=8, max_length=200, example="João da Silva")
    senha: str = Field(..., min_length=8, max_length=200, examples="teste1234")
    email: str = Field(..., min_length=8, max_length=200, example="email@email.com")
    data_nascimento: datetime = Field(..., format="%d/%m/%Y", description="Data de nascimento no formato dd/mm/yyyy", example="21/05/2025")

    def __str__(self):
        return f"Nome: {self.nome}, Senha: {self.senha}, Email: {self.email}"
