import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def conectar():
    """Abre e retorna uma conexão ativa com o PostgreSQL no Neon.tech."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432"),
        sslmode="require"
    )


def criar_tabela():
    """Cria a tabela incidentes_criticos no banco caso ela ainda não exista."""
    conexao = conectar()
    cursor = conexao.cursor()

    sql_tabela = """
    CREATE TABLE IF NOT EXISTS incidentes_criticos (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        ano INTEGER NOT NULL,
        organizacao_afetada VARCHAR(100) NOT NULL,
        impacto_financeiro_milhoes NUMERIC(10, 2) NOT NULL,
        foto_url TEXT NOT NULL
    )
    """

    cursor.execute(sql_tabela)
    conexao.commit()

    cursor.close()
    conexao.close()
    print("Conexão verificada e tabela 'incidentes_criticos' pronta!")