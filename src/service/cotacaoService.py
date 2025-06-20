from starlette.responses import JSONResponse

from src.database.db import Databases
from src.models.cotacaoModel import Cotacao


class CotacaoService:
    @classmethod
    def criar_cotacao(cls, cotacao_data: Cotacao):
        params = (
            cotacao_data.codigoMoeda,
            cotacao_data.dataCotacao,
            cotacao_data.valorCotacao
        )
        last_id = Databases.execute_query(
            """INSERT INTO cotacao (CodigoMoeda, DataCotacao, ValorCotacao) VALUES (?,?,?)""", params)
        return JSONResponse(status_code=201, content={"message": "Cotação criada com sucesso!", "id": last_id})

    @classmethod
    def listar_cotacoes(cls):
        lista = Databases.fetch_all("""SELECT * FROM cotacao""")
        cotacao_dict = [dict(row) for row in lista] if lista else []
        return JSONResponse(status_code=200, content=cotacao_dict)

    @classmethod
    def deletar_cotacao(cls, ids):
        if isinstance(ids, (int, str)):
            ids = [ids]
        if not ids:
            raise ValueError("Nenhum ID fornecido para exclusão.")
        placeholders = ", ".join(["?" for _ in ids])
        Databases.execute_query(f"DELETE FROM cotacao WHERE Id IN ({placeholders})", tuple(ids))
        return {"message": "Registros deletados com sucesso!"}

    @classmethod
    def atualizar_cotacao(cls, cotacao_id: int, cotacao_data: Cotacao):
        query = """
                UPDATE indicadores
                SET CodigoMoeda = ?, DataCotacao = ?, ValorCotacao = ?
                WHERE Id = ?;
                """
        params = (
            cotacao_data.codigoMoeda,
            cotacao_data.dataInicio,
            cotacao_data.dataFim,
            cotacao_id  # O ID do registro a ser atualizado
        )
        Databases.execute_query(query, params)
        return {"message": f"Indicador com ID {cotacao_id} atualizado com sucesso!"}
