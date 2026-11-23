import matplotlib.pyplot as plt
from database.incidentes_repo import dados_agrupados_por_categoria


def gerar_grafico_categorias():
    """Gera gráficos comparativos agrupados por categoria usando matplotlib."""
    dados = dados_agrupados_por_categoria()

    if not dados:
        print("\nNenhum dado cadastrado para gerar gráficos.")
        return

    categorias = [item["categoria"] for item in dados]
    totais_incidentes = [int(item["total_incidentes"]) for item in dados]
    prejuizos = [float(item["prejuizo_total"]) for item in dados]

    # Cria uma figura com 2 gráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("BlackBox TI - Análise de Incidentes Críticos por Categoria", fontsize=14, fontweight="bold")

    # Gráfico 1: Soma do Prejuízo Financeiro por Categoria
    barras1 = ax1.bar(categorias, prejuizos, color="#dc2626")
    ax1.set_title("Prejuízo Financeiro Total (US$ Milhões)")
    ax1.set_xlabel("Categoria")
    ax1.set_ylabel("Milhões de Dólares")
    ax1.bar_label(barras1, fmt="%.1f", padding=3)

    # Gráfico 2: Quantidade de Incidentes por Categoria
    barras2 = ax2.bar(categorias, totais_incidentes, color="#2563eb")
    ax2.set_title("Quantidade de Incidentes Registrados")
    ax2.set_xlabel("Categoria")
    ax2.set_ylabel("Nº de Incidentes")
    ax2.bar_label(barras2, padding=3)

    plt.tight_layout()
    caminho_imagem = "output/grafico_incidentes.png"
    plt.savefig(caminho_imagem, dpi=150)
    print(f"\nGráfico salvo em '{caminho_imagem}'! Fechando a janela do gráfico você volta ao menu.")
    plt.show()