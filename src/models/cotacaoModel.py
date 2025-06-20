from pydantic import BaseModel


class Cotacao(BaseModel):
    codigoMoeda: int
    dataCotacao: str
    valorCotacao: float
