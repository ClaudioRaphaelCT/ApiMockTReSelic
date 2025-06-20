from fastapi import FastAPI

from src.models.cotacaoModel import Cotacao
from src.models.indicadoresModel import Indicadores
from src.service.Service import Service
from src.service.cotacaoService import CotacaoService
from src.service.indicadoresService import IndicadoresService

app = FastAPI(title="Mock TR e SELIC", version="0.0.1")


# Check Healt
@app.get("/health", tags=["Health app check."], summary="Check app on.")
def health_check():
    return {"status": "ok", "swagger_url": "/docs#/"}


# INDICADORES
@app.post("/indicadores/v1", tags=["Indicadores"], summary="Criar indicador")
def criar_indicador(indicador: Indicadores):
    return IndicadoresService.criar_indicadores(indicador)


@app.get("/indicadores/v1", tags=["Indicadores"], summary="Visualizar todos indicadores criados.")
def listar_indicadores():
    return IndicadoresService.listar_indicadores()


@app.delete("/indicadores/v1/{indicador_id}", tags=["Indicadores"], summary="Deletar indicador por id unico.")
def deletar_indicadores(indicador_id: int):
    return IndicadoresService.deletar_indicadores(indicador_id)


@app.put("/indicadores/v1/{indicador_id}", tags=["Indicadores"], summary="Atualizar indicador por ID")
def atualizar_indicador(indicador_id: int, indicador_data: Indicadores):
    return IndicadoresService.atualizar_indicadores(indicador_id, indicador_data)


# COTACAO
@app.post("/cotacao/v1", tags=["Cotação"], summary="Criar cotação")
def criar_cotacao(cotacao: Cotacao):
    return CotacaoService.criar_cotacao(cotacao)


@app.get("/cotacao/v1", tags=["Cotação"], summary="Visualizar Todas cotações")
def listar_cotacoes():
    return CotacaoService.listar_cotacoes()


@app.delete("/cotacao/v1/{cotacao_id}", tags=["Cotação"], summary="Deletar cotação por id")
def deletar_cotacao(cotacao_id: int):
    return CotacaoService.deletar_cotacao(cotacao_id)


@app.put("/cotacao/v1/{cotacao_id}")
def atualizar_cotacao(cotacao_id: int, cotacao_data: Cotacao):
    return CotacaoService.atualizar_cotacao(cotacao_id, cotacao_data)


# SERVIÇO PRINCIPAL
@app.post("/indicadores/cotacao", tags=["Serviço Principal"], summary="Serviço que será realizado para o mock.")
def listar():
    return Service.listar()
