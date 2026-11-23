import csv
import json
from decimal import Decimal
from database.incidentes_repo import listar_incidentes


def exportar_backup():
    """Exporta todos os registros do banco para output/backup.json e output/backup.csv."""
    incidentes = listar_incidentes()

    if not incidentes:
        print("\nNenhum registro encontrado para realizar backup.")
        return

    # Converte valores Decimal do PostgreSQL para float antes de salvar
    dados_limpos = []
    for item in incidentes:
        registro = dict(item)
        if isinstance(registro.get("impacto_financeiro_milhoes"), Decimal):
            registro["impacto_financeiro_milhoes"] = float(registro["impacto_financeiro_milhoes"])
        dados_limpos.append(registro)

    # 1. Backup em JSON
    caminho_json = "output/backup.json"
    with open(caminho_json, "w", encoding="utf-8") as f_json:
        json.dump(dados_limpos, f_json, ensure_ascii=False, indent=4)

    # 2. Backup em CSV
    caminho_csv = "output/backup.csv"
    colunas = dados_limpos[0].keys()
    with open(caminho_csv, "w", newline="", encoding="utf-8") as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(dados_limpos)

    print(f"\nBackups gerados com sucesso!\n -> {caminho_json}\n -> {caminho_csv}")