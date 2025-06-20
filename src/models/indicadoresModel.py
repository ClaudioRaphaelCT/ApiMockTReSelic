from pydantic import BaseModel


class Indicadores(BaseModel):
    codigoMoeda: int
    dataInicio: str
    dataFim: str
