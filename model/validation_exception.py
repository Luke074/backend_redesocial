from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        if error["type"] == "missing":
            field = error["loc"][-1]
            errors.append(f"O campo '{field}' é obrigatório")
        elif error["type"] == "string_too_short":
            field = error["loc"][-1]
            min_length = error["ctx"]["min_length"]
            errors.append(
                f"O campo '{field}' deve ter no mínimo {min_length} caracteres"
            )
        elif error["type"] == "string_too_long":
            field = error["loc"][-1]
            max_length = error["ctx"]["max_length"]
            errors.append(
                f"O campo '{field}' deve ter no máximo {max_length} caracteres"
            )
        elif error["type"] == "string_pattern_mismatch":
            field = error["loc"][-1]
            if field == "email":
                errors.append(
                    "Email inválido. Use um formato válido como: exemplo@email.com"
                )
            else:
                errors.append(error["msg"])
        elif error["type"] == "value_error.date.format":
            field = error["loc"][-1]
            errors.append(f"O campo '{field}' deve estar no formato dd/mm/yyyy")
        elif error["type"] == "value_error.email":
            field = error["loc"][-1]
            errors.append(f"O campo '{field}' deve ser um email válido")
        else:
            errors.append(error["msg"])

    raise HTTPException(status_code=400, detail=errors)
