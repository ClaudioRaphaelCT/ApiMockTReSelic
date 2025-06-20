from starlette.responses import JSONResponse

from src.database.db import Databases
from src.models.indicadoresModel import Indicadores


class Service:
    @classmethod
    def listar(cls, filtro_indicadores: Indicadores):
        query = """
           SELECT c.dataCotacao, c.valorCotacao
           FROM cotacao c
           WHERE c.CodigoMoeda = ?;
           """
        params = (filtro_indicadores.codigoMoeda,)

        lista = Databases.fetch_all(query, params)

        listar_dict = [dict(row) for row in lista] if lista else []
        return JSONResponse(status_code=200, content=listar_dict)
