from starlette.responses import JSONResponse

from src.database.db import Databases
from src.models.indicadoresModel import Indicadores


class IndicadoresService:
    @classmethod
    def criar_indicadores(cls, indicador_data: Indicadores):
        params = (
            indicador_data.codigoMoeda,
            indicador_data.dataInicio,
            indicador_data.dataFim
        )
        last_id = Databases.execute_query(
            """INSERT INTO indicadores (CodigoMoeda, DataInicio, DataFim) VALUES (?,?,?)""", params)
        return JSONResponse(status_code=201, content={"message": "Indicador criado com sucesso!", "id": last_id})

    @classmethod
    def listar_indicadores(cls):
        lista = Databases.fetch_all("""SELECT * FROM indicadores""")
        indicadores_dict = [dict(row) for row in lista] if lista else []
        return JSONResponse(status_code=200, content=indicadores_dict)

    @classmethod
    def atualizar_indicadores(cls, indicador_id: int, indicador_data: Indicadores):
        query = """
            UPDATE indicadores
            SET CodigoMoeda = ?, DataInicio = ?, DataFim = ?
            WHERE Id = ?;
            """
        params = (
            indicador_data.codigoMoeda,
            indicador_data.dataInicio,
            indicador_data.dataFim,
            indicador_id  # O ID do registro a ser atualizado
        )
        Databases.execute_query(query, params)
        return {"message": f"Indicador com ID {indicador_id} atualizado com sucesso!"}

    @classmethod
    def deletar_indicadores(cls, ids):
        if isinstance(ids, (int, str)):
            ids = [ids]
        if not ids:
            raise ValueError("Nenhum ID fornecido para exclusão.")
        placeholders = ", ".join(["?" for _ in ids])
        Databases.execute_query(f"DELETE FROM indicadores WHERE Id IN ({placeholders})", tuple(ids))
        return {"message": "Registros deletados com sucesso!"}
