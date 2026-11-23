# Bugs Históricos — Base de Análise de Incidentes Críticos (Post-Mortem)

Aplicação em Python integrada a um banco de dados **PostgreSQL** hospedado na nuvem (**Neon.tech**) utilizando `psycopg2`, desenvolvida para a disciplina de **Algoritmos e Estruturas de Dados I** (UniSenac Pelotas).

## Funcionalidades
- **CRUD Completo:** Cadastro, listagem, consulta por ID, atualização e exclusão de incidentes críticos.
- **Pesquisa Avançada:** Filtro combinado por categoria e ano mínimo de ocorrência.
- **Análise Gráfica:** Geração de gráficos comparativos (`matplotlib`) com agrupamento SQL (`GROUP BY`).
- **Relatório Web:** Geração dinâmica de catálogo visual em HTML/CSS (`output/index.html`) com imagens.
- **Backup:** Exportação completa da base de dados em formatos `.json` e `.csv`.
