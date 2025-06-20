import os
import sqlite3


class Databases:
    @classmethod
    def get_db_connection(cls):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "cartao.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def create_tables(cls):
        conn = cls.get_db_connection()
        try:
            # Executar a primeira tabela
            conn.execute("""
             CREATE TABLE IF NOT EXISTS indicadores(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                CodigoMoeda INTEGER NOT NULL,
                DataInicio TEXT NOT NULL,
                DataFim TEXT NOT NULL
             )
            """)  # Removido o ponto e vírgula final, não é estritamente necessário aqui

            # Executar a segunda tabela
            conn.execute("""
             CREATE TABLE IF NOT EXISTS cotacao(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                CodigoMoeda INTEGER NOT NULL,
                DataCotacao TEXT NOT NULL,
                ValorCotacao REAL NOT NULL
             )
            """)  # Removido o ponto e vírgula final

            conn.commit()
        finally:
            conn.close()

    @classmethod
    def execute_query(cls, sql_text, params=None):
        """Para queries que modificam o banco (INSERT, UPDATE, DELETE)."""
        conn = cls.get_db_connection()
        try:
            cursor = conn.execute(sql_text, params or ())
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    @classmethod
    def fetch_all(cls, sql_text, params=None):
        """Para queries que leem dados (SELECT)."""
        conn = cls.get_db_connection()
        results = None
        try:
            cursor = conn.execute(sql_text, params or ())
            results = cursor.fetchall()
        finally:
            conn.close()
        return results

    @classmethod
    def fetch_one(cls, sql_text, params=None):
        """Para queries que esperam um único resultado."""
        conn = cls.get_db_connection()
        result = None
        try:
            cursor = conn.execute(sql_text, params or ())
            result = cursor.fetchone()
        finally:
            conn.close()
        return result


Databases.create_tables()
