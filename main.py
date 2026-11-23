from database.conexao import criar_tabela
from database.incidentes_repo import (
    inserir_incidente,
    listar_incidentes,
    buscar_por_id,
    atualizar_incidente,
    excluir_incidente,
    pesquisa_avancada,
)
from services.graficos import gerar_grafico_categorias
from services.web_generator import gerar_pagina_web
from services.backup import exportar_backup


def exibir_incidente(inc):
    """Formata e imprime os dados de um dicionário de incidente."""
    print(f"\nID: {inc['id']} | Título: {inc['titulo']}")
    print(f"Categoria: {inc['categoria']} | Ano: {inc['ano']}")
    print(f"Organização Afetada: {inc['organizacao_afetada']}")
    print(f"Impacto Financeiro: US$ {float(inc['impacto_financeiro_milhoes']):,.2f} milhões")
    print(f"Foto URL: {inc['foto_url']}")


def menu_inserir():
    print("\n---< CADASTRAR INCIDENTE CRÍTICO >---")
    titulo = input("Título do incidente: ")
    categoria = input("Categoria (Software / Hardware / Segurança / Infraestrutura): ")
    ano = int(input("Ano de ocorrência: "))
    organizacao = input("Organização afetada: ")
    impacto = float(input("Impacto financeiro (em milhões de US$): ").replace(",", "."))
    foto_url = input("URL da foto ilustrativa: ")

    inserir_incidente(titulo, categoria, ano, organizacao, impacto, foto_url)
    print("\nIncidente cadastrado com sucesso!")


def menu_listar():
    print("\n---< LISTAGEM DE INCIDENTES CRÍTICOS >---")
    incidentes = listar_incidentes()
    if not incidentes:
        print("Nenhum incidente cadastrado.")
        return

    for inc in incidentes:
        exibir_incidente(inc)


def menu_consultar():
    print("\n---< CONSULTAR INCIDENTE POR ID >---")
    id_inc = int(input("Informe o ID do incidente: "))
    inc = buscar_por_id(id_inc)

    if inc is None:
        print("\nIncidente não encontrado!")
    else:
        exibir_incidente(inc)


def menu_atualizar():
    print("\n---< ATUALIZAR INCIDENTE >---")
    id_inc = int(input("Informe o ID do incidente: "))
    inc = buscar_por_id(id_inc)

    if inc is None:
        print("\nIncidente não encontrado!")
        return

    print(f"\nEditando: {inc['titulo']}")
    titulo = input("Novo título: ")
    categoria = input("Nova categoria (Software / Hardware / Segurança / Infraestrutura): ")
    ano = int(input("Novo ano: "))
    organizacao = input("Nova organização afetada: ")
    impacto = float(input("Novo impacto financeiro (em milhões de US$): ").replace(",", "."))
    foto_url = input("Nova URL da foto: ")

    atualizar_incidente(id_inc, titulo, categoria, ano, organizacao, impacto, foto_url)
    print("\nIncidente atualizado com sucesso!")


def menu_excluir():
    print("\n---< EXCLUIR INCIDENTE >---")
    id_inc = int(input("Informe o ID do incidente: "))
    inc = buscar_por_id(id_inc)

    if inc is None:
        print("\nIncidente não encontrado!")
        return

    print(f"\nIncidente selecionado: {inc['titulo']}")
    confirma = input("Deseja realmente excluir? (S/N): ")

    if confirma.strip().upper() == "S":
        excluir_incidente(id_inc)
        print("\nIncidente excluído com sucesso!")
    else:
        print("\nExclusão cancelada.")


def menu_pesquisa_avancada():
    print("\n---< PESQUISA AVANÇADA (2 FILTROS) >---")
    categoria = input("Filtrar por Categoria (Software / Hardware / Segurança / Infraestrutura): ")
    ano_minimo = int(input("A partir de qual ano (ex: 1995): "))

    resultados = pesquisa_avancada(categoria, ano_minimo)
    if not resultados:
        print("\nNenhum incidente encontrado com esses critérios.")
    else:
        print(f"\n{len(resultados)} incidente(s) encontrado(s):")
        for inc in resultados:
            exibir_incidente(inc)


def main():
    criar_tabela()

    while True:
        print("\n==========< BLACKBOX TI - POST-MORTEM >==========")
        print("1. Cadastrar incidente (Create)")
        print("2. Listar todos os incidentes (Read)")
        print("3. Consultar incidente por ID (Read)")
        print("4. Atualizar incidente (Update)")
        print("5. Excluir incidente (Delete)")
        print("6. Pesquisa avançada (Categoria + Ano mínimo)")
        print("7. Gerar gráfico comparativo por categoria")
        print("8. Gerar página Web (HTML)")
        print("9. Gerar backup dos dados (JSON e CSV)")
        print("0. Sair")
        print("=================================================")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nPor favor, digite apenas números.")
            continue

        if opcao == 1:
            menu_inserir()
        elif opcao == 2:
            menu_listar()
        elif opcao == 3:
            menu_consultar()
        elif opcao == 4:
            menu_atualizar()
        elif opcao == 5:
            menu_excluir()
        elif opcao == 6:
            menu_pesquisa_avancada()
        elif opcao == 7:
            gerar_grafico_categorias()
        elif opcao == 8:
            gerar_pagina_web()
        elif opcao == 9:
            exportar_backup()
        elif opcao == 0:
            print("\nEncerrando BlackBox TI...")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()