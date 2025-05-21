from pydantic import BaseModel, Field
from datetime import datetime


class RequestRegister(BaseModel):
    nome: str = Field(..., min_length=8, max_length=200, example="João da Silva")
    senha: str = Field(..., min_length=8, max_length=200, examples="teste1234")
    email: str = Field(
        ...,
        min_length=8,
        max_length=200,
        example="email@email.com",
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    )
    celular: str = Field(..., le=15, example="(11) 99999-9999")
    data_nascimento: datetime = Field(
        ...,
        format="%d/%m/%Y",
        description="Data de nascimento no formato dd/mm/yyyy",
        example="01/01/1990",
        ge=datetime(1900, 1, 1),
    )

    def __str__(self):
        return f"Nome: {self.nome}, Senha: {self.senha}, Email: {self.email}, Data de nascimento: {self.data_nascimento}, Celular: {self.celular}"
