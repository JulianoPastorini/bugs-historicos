import os
import webbrowser
from database.incidentes_repo import listar_incidentes


def gerar_pagina_web():
    """Gera dinamicamente o arquivo output/index.html exibindo os cards dos incidentes."""
    incidentes = listar_incidentes()

    if not incidentes:
        print("\nNenhum incidente cadastrado para gerar a página Web.")
        return

    cards_html = ""
    for inc in incidentes:
        cards_html += f"""
        <div class="card">
            <img src="{inc['foto_url']}" alt="{inc['titulo']}" onerror="this.src='https://placehold.co/600x400/1e293b/94a3b8?text=Imagem+Indisponivel'">
            <div class="card-body">
                <span class="badge">{inc['categoria']} • {inc['ano']}</span>
                <h2>#{inc['id']} - {inc['titulo']}</h2>
                <p><strong>Organização Afetada:</strong> {inc['organizacao_afetada']}</p>
                <p class="prejuizo">Impacto Estimado: US$ {float(inc['impacto_financeiro_milhoes']):,.2f} milhões</p>
            </div>
        </div>
        """

    html_completo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BlackBox TI - Post-Mortem de Incidentes Críticos</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 32px;
        }}
        header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        header h1 {{
            color: #38bdf8;
            margin-bottom: 8px;
        }}
        header p {{
            color: #94a3b8;
            margin: 0;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .card {{
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        }}
        .card img {{
            width: 100%;
            height: 200px;
            object-fit: cover;
            background-color: #020617;
        }}
        .card-body {{
            padding: 20px;
        }}
        .badge {{
            display: inline-block;
            background-color: #0284c7;
            color: #fff;
            font-size: 12px;
            font-weight: bold;
            padding: 4px 10px;
            border-radius: 999px;
            margin-bottom: 10px;
        }}
        .card h2 {{
            font-size: 18px;
            margin: 0 0 12px 0;
            color: #f1f5f9;
        }}
        .card p {{
            margin: 6px 0;
            font-size: 14px;
            color: #cbd5e1;
        }}
        .prejuizo {{
            color: #f87171 !important;
            font-weight: bold;
            margin-top: 12px !important;
        }}
    </style>
</head>
<body>
    <header>
        <h1>BlackBox TI — Base de Incidentes Críticos</h1>
        <p>Relatório Visual de Post-Mortem e Impacto em Engenharia de Sistemas</p>
    </header>
    <main class="grid">
        {cards_html}
    </main>
</body>
</html>
"""

    caminho_html = os.path.abspath("output/index.html")
    with open(caminho_html, "w", encoding="utf-8") as arquivo:
        arquivo.write(html_completo)

    print(f"\nPágina Web gerada com sucesso em: {caminho_html}")
    webbrowser.open(f"file://{caminho_html}")