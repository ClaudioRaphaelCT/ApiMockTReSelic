from starlette.responses import JSONResponse

from src.database.db import Databases


class Service:
    @classmethod
    def listar(cls):
        lista = Databases.fetch_all("""SELECT c.dataCotacao, c.valorCotacao FROM indicadores i INNER JOIN cotacao c 
        on i.CodigoMoeda = c.CodigoMoeda""")
        listar_dict = [dict(row) for row in lista] if lista else []
        return JSONResponse(status_code=200, content=listar_dict)
