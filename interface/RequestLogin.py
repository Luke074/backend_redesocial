from pydantic import BaseModel, Field


class RequestLogin(BaseModel):
    nome: str = Field(..., min_length=8, max_length=200)
    senha: str = Field(..., min_length=8, max_length=200)

    def __str__(self):
        return f"Nome: {self.nome}, Senha: {self.senha}"
