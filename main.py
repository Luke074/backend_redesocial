import uvicorn

# FastAPI
from fastapi import FastAPI, HTTPException

# Model
from model.response import returnStatus

# Interfaces
from interface.RequestLogin import RequestLogin
from interface.RequestRegister import RequestRegister

# Pydantic
from pydantic import ValidationError
from fastapi.exceptions import RequestValidationError
from model.validation_exception import validation_exception_handler

app = FastAPI()

app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/")
def read_root():
    return returnStatus(200, True, "Hello World")


@app.post("/login")
def login(request: RequestLogin):
    try:
        # Aqui você pode adicionar sua lógica de autenticação
        if request.nome == "testando" and request.senha == "testando":
            return returnStatus(200, True, "Login realizado com sucesso")
        else:
            return returnStatus(401, False, "Usuário ou senha inválidos")

    except ValidationError as e:
        return returnStatus(400, False, str(e))
    except Exception as e:
        return returnStatus(500, False, f"Erro interno do servidor: {str(e)}")


@app.post("/register")
def register(request: RequestRegister):
    try:
        print(f"Request: {request}")
        return returnStatus(200, True, "Registro realizado com sucesso")
    except ValidationError as e:
        return returnStatus(400, False, str(e))
    except Exception as e:
        return returnStatus(500, False, f"Erro interno do servidor: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
