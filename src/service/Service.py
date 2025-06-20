from starlette.responses import JSONResponse

from src.database.db import Databases
from src.models.indicadoresModel import Indicadores


class Service:
    @classmethod
    def listar(cls, filtro_indicadores: Indicadores):  # Recebe um objeto Indicadores completo
        # Sua query SQL COM o INNER JOIN e o filtro WHERE pelo CodigoMoeda
        query = """
            SELECT c.dataCotacao, c.valorCotacao
            FROM indicadores i 
            INNER JOIN cotacao c ON i.CodigoMoeda = c.CodigoMoeda
            WHERE i.CodigoMoeda = ?; -- O filtro é aplicado na coluna CodigoMoeda que participa do JOIN
            """

        # O parâmetro para a query é uma tupla com o codigoMoeda do objeto Indicadores
        params = (filtro_indicadores.codigoMoeda,)  # Tupla de um elemento, sempre!

        lista = Databases.fetch_all(query, params)

        listar_dict = [dict(row) for row in lista] if lista else []
        return JSONResponse(status_code=200, content=listar_dict)
