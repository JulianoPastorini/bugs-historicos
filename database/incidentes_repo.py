from psycopg2.extras import RealDictCursor
from database.conexao import conectar


def inserir_incidente(titulo, categoria, ano, organizacao_afetada, impacto_financeiro_milhoes, foto_url):
    """C - Create: Insere um novo incidente crítico no banco."""
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO incidentes_criticos
        (titulo, categoria, ano, organizacao_afetada, impacto_financeiro_milhoes, foto_url)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (titulo, categoria, ano, organizacao_afetada, impacto_financeiro_milhoes, foto_url))
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_incidentes():
    """R - Read: Retorna todos os incidentes cadastrados como lista de dicionários."""
    conexao = conectar()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM incidentes_criticos ORDER BY id")
    incidentes = cursor.fetchall()

    cursor.close()
    conexao.close()
    return incidentes


def buscar_por_id(id_incidente):
    """R - Read: Busca um incidente específico pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM incidentes_criticos WHERE id = %s", (id_incidente,))
    incidente = cursor.fetchone()

    cursor.close()
    conexao.close()
    return incidente


def atualizar_incidente(id_incidente, titulo, categoria, ano, organizacao_afetada, impacto_financeiro_milhoes, foto_url):
    """U - Update: Atualiza os dados de um incidente existente."""
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE incidentes_criticos
    SET titulo = %s,
        categoria = %s,
        ano = %s,
        organizacao_afetada = %s,
        impacto_financeiro_milhoes = %s,
        foto_url = %s
    WHERE id = %s
    """
    cursor.execute(
        sql,
        (titulo, categoria, ano, organizacao_afetada, impacto_financeiro_milhoes, foto_url, id_incidente)
    )
    linhas_afetadas = cursor.rowcount
    conexao.commit()

    cursor.close()
    conexao.close()
    return linhas_afetadas


def excluir_incidente(id_incidente):
    """D - Delete: Remove um incidente pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM incidentes_criticos WHERE id = %s", (id_incidente,))
    linhas_afetadas = cursor.rowcount
    conexao.commit()

    cursor.close()
    conexao.close()
    return linhas_afetadas


def pesquisa_avancada(categoria, ano_minimo):
    """Requisito 2: Pesquisa avançada filtrando por 2 atributos (Categoria + Ano mínimo)."""
    conexao = conectar()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    sql = """
    SELECT * FROM incidentes_criticos
    WHERE LOWER(categoria) = LOWER(%s) AND ano >= %s
    ORDER BY ano DESC
    """
    cursor.execute(sql, (categoria, ano_minimo))
    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return resultados


def dados_agrupados_por_categoria():
    """Requisito 3: Agrupa quantidade e prejuízo total por categoria para os gráficos."""
    conexao = conectar()
    cursor = conexao.cursor(cursor_factory=RealDictCursor)

    sql = """
    SELECT
        categoria,
        COUNT(*) AS total_incidentes,
        SUM(impacto_financeiro_milhoes) AS prejuizo_total
    FROM incidentes_criticos
    GROUP BY categoria
    ORDER BY prejuizo_total DESC
    """
    cursor.execute(sql)
    dados = cursor.fetchall()

    cursor.close()
    conexao.close()
    return dados