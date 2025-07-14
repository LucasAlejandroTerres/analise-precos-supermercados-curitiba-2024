import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

#======================================================================
# --- 1. CONFIGURAÇÃO E CARREGAMENTO ---
#======================================================================
print("Iniciando a geração do Heatmap de Competitividade por Macro Categoria...")

# --- Caminho do Dataset Final ---
caminho_dataset_pronto = r'D:\CliqueEconomia_TCC_DATASET_PRONTO.csv'

# --- Pasta para salvar os resultados ---
pasta_resultados = r'D:\resultados_tcc'
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)
print(f"O resultado será salvo na pasta: '{pasta_resultados}'")

# --- Definição da Cesta de Categorias Essenciais ---
CESTA_ESSENCIAL = [
    'MERCEARIA', 'HORTIFRUTI', 'CARNES', 
    'LATICINIOS_E_FRIOS', 'LIMPEZA_E_UTILIDADES'
]

# --- Carregamento dos Dados ---
try:
    df = pd.read_csv(caminho_dataset_pronto, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset com {len(df)} linhas carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO CRÍTICO: Arquivo '{caminho_dataset_pronto}' não encontrado.")
    sys.exit()

# Filtra o DataFrame para conter apenas os itens da cesta essencial
df_cesta = df[df['categoria_n1'].isin(CESTA_ESSENCIAL)].copy()

#======================================================================
# --- 2. CRIAÇÃO DA MATRIZ E GERAÇÃO DO GRÁFICO ---
#======================================================================
print("Preparando a matriz de competitividade...")

# Cria a tabela pivot com o preço mediano por rede e MACRO categoria
matriz_competitividade = df_cesta.pivot_table(
    index='rede', 
    columns='categoria_n1', 
    values='preco_regular', 
    aggfunc='median'
)

# Salva a tabela de dados para sua referência
caminho_tabela = os.path.join(pasta_resultados, '3_tabela_matriz_competitividade.csv')
matriz_competitividade.round(2).to_csv(caminho_tabela, sep=';', encoding='utf-8-sig')
print(f" -> Tabela de dados salva em: '{os.path.basename(caminho_tabela)}'")

# Gera o gráfico de heatmap
print("Gerando o gráfico de heatmap...")
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 10)) # Ajuste no tamanho para melhor visualização

sns.heatmap(
    matriz_competitividade.fillna(0), # Preenche valores nulos com 0 para o gráfico
    annot=True, 
    fmt=".2f", 
    cmap="viridis_r", # Paleta de cores (Verde/Azul para mais barato)
    linewidths=.5, 
    ax=ax
)

ax.set_title(
    'Matriz de Competitividade: Preço Mediano por Rede e Macro Categoria',
    fontsize=16, 
    pad=20, 
    fontweight='bold'
)
ax.set_xlabel('Macro Categoria', fontsize=12)
ax.set_ylabel('Rede de Supermercado', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()

#======================================================================
# --- 3. EXPORTAÇÃO ---
#======================================================================
caminho_saida = os.path.join(pasta_resultados, '3_grafico_matriz_competitividade.png')
plt.savefig(caminho_saida, dpi=300)
print(f" -> Gráfico de heatmap salvo com sucesso em: '{os.path.basename(caminho_saida)}'")
plt.close()

print("\n----------------------------------------------------")
print("✅ Processo concluído! ✅")
print("----------------------------------------------------")