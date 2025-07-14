import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

#======================================================================
# --- 1. CONFIGURAÇÃO ---
#======================================================================
# Caminho para o arquivo CSV com o ranking das redes
caminho_tabela_redes = r'D:\resultados_tcc\2_tabela_ranking_redes.csv'

# Pasta para salvar o resultado
pasta_resultados = 'resultados_tcc'
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)
print(f"O gráfico será salvo na pasta: '{pasta_resultados}'")

# Lista das redes que serão desconsideradas na análise
redes_a_excluir = ['SUPER GS', 'SUPERMERCADO GALVÃO']

#======================================================================
# --- 2. CARREGAMENTO E PREPARAÇÃO DOS DADOS ---
#======================================================================
try:
    # Carrega o arquivo CSV
    df_ranking = pd.read_csv(caminho_tabela_redes, delimiter=';')
    print(f"Tabela de ranking com {len(df_ranking)} redes carregada com sucesso.")

    # --- Filtro para Excluir Redes Específicas ---
    print(f"Excluindo as seguintes redes da análise: {redes_a_excluir}")
    df_filtrado = df_ranking[~df_ranking['rede'].isin(redes_a_excluir)]
    print(f"Análise será feita com {len(df_filtrado)} redes.")

    # Ordena os dados do mais barato para o mais caro
    df_sorted = df_filtrado.sort_values(by='indice_custo_cesta_R$')

    # Extrai os 10 mais baratos e os 10 mais caros do conjunto de dados JÁ FILTRADO
    top_10_baratos = df_sorted.head(10)
    top_10_caros = df_sorted.tail(10)

    # Concatena os dois grupos em um único DataFrame para o gráfico
    df_plot = pd.concat([top_10_baratos, top_10_caros]).sort_values(by='indice_custo_cesta_R$', ascending=True)

except FileNotFoundError:
    print(f"ERRO CRÍTICO: Arquivo '{caminho_tabela_redes}' não encontrado.")
    sys.exit()
except Exception as e:
    print(f"Ocorreu um erro ao processar os dados: {e}")
    sys.exit()

#======================================================================
# --- 3. GERAÇÃO DO GRÁFICO ---
#======================================================================
print("Gerando o gráfico de ranking duplo...")

# Define o estilo do gráfico
plt.style.use('seaborn-v0_8-whitegrid')
# Cria a figura e os eixos com um tamanho adequado
fig, ax = plt.subplots(figsize=(14, 12))

# Define as cores: verde para os 10 mais baratos, vermelho para os 10 mais caros
colors = ['#5cb85c'] * 10 + ['#d9534f'] * 10

# Cria as barras horizontais
bars = ax.barh(df_plot['rede'], df_plot['indice_custo_cesta_R$'], color=colors)

# Adiciona os valores (rótulos) em cada barra, formatados como moeda
ax.bar_label(bars, fmt='R$ %.2f', padding=5, fontsize=11, color='black')

# Configura os títulos e os eixos exatamente como solicitado
ax.set_title(
    'Ranking Duplo das Redes de Supermercado por Custo da Cesta Essencial (Top 10 mais baratos e mais caros)',
    fontsize=18,
    pad=20,
    fontweight='bold'
)
ax.set_xlabel('Índice de Custo da Cesta (R$)', fontsize=14)
ax.set_ylabel('Rede de Supermercado', fontsize=14)

# Ajusta as margens para garantir que tudo fique visível
plt.tight_layout()

#======================================================================
# --- 4. EXPORTAÇÃO E EXIBIÇÃO ---
#======================================================================
# Salva o gráfico em formato PNG com alta resolução
caminho_saida = os.path.join(pasta_resultados, 'grafico_ranking_duplo_redes_filtrado.png')
plt.savefig(caminho_saida, dpi=300)
print(f"Gráfico salvo com sucesso em: '{caminho_saida}'")

# Exibe o gráfico
plt.show()