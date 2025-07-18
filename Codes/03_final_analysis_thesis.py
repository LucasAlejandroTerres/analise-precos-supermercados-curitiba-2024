import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

#======================================================================
# --- 1. CONFIGURAÇÃO E CARREGAMENTO ---
#======================================================================
print("Iniciando Script de Análise Final e Detalhada para o TCC...")

# --- Caminho do Dataset Final ---
caminho_dataset_pronto = r'D:\CliqueEconomia_TCC_DATASET_PRONTO.csv'

# --- Define o caminho absoluto para salvar os resultados ---
pasta_resultados = r'D:\resultados_tcc'
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)
print(f"Todos os resultados serão salvos na pasta: '{pasta_resultados}'")

# --- Definições ---
CESTA_ESSENCIAL = [
    'MERCEARIA', 'HORTIFRUTI', 'CARNES', 
    'LATICINIOS_E_FRIOS', 'LIMPEZA_E_UTILIDADES'
]
# Lista de subcategorias chave para a nova análise detalhada
SUBCATEGORIAS_CHAVE = [
    'LEITE', 'ARROZ', 'FEIJAO', 'CARNE_BOVINA', 'AVES', 'PAES', 'OVOS', 'FRUTAS', 'LEGUMES_E_VERDURAS'
]

# --- Carregamento dos Dados ---
try:
    df = pd.read_csv(caminho_dataset_pronto, delimiter=';', encoding='utf-8-sig')
    df['data_pesquisa'] = pd.to_datetime(df['data_pesquisa'], errors='coerce')
    df.dropna(subset=['data_pesquisa'], inplace=True)
    print(f"Dataset com {len(df)} linhas carregado e datas validadas com sucesso.")
    
except FileNotFoundError:
    print(f"ERRO CRÍTICO: Arquivo '{caminho_dataset_pronto}' não encontrado.")
    sys.exit()

df_cesta = df[df['categoria_n1'].isin(CESTA_ESSENCIAL)].copy()

#======================================================================
# --- TEMAS 1, 2, 3 e 4: ANÁLISES MACRO (GERA ARQUIVOS 1-6) ---
#======================================================================
print("\nGerando Insights Macro (Temas 1 a 4)...")

# TEMA 1: Análise Geográfica por Bairro
print(" -> Gerando Análise Geográfica por Bairro...")
preco_mediano_bairro = df_cesta.groupby(['bairro', 'categoria_n1'])['preco_regular'].median().unstack()
custo_cesta_bairro = preco_mediano_bairro.sum(axis=1).sort_values(ascending=False)
tabela_ranking_bairros = custo_cesta_bairro.round(2).reset_index(name='indice_custo_cesta_R$')
tabela_ranking_bairros.to_csv(os.path.join(pasta_resultados, '1_tabela_ranking_bairros.csv'), index=False, sep=';', encoding='utf-8-sig')
top_10_caros = tabela_ranking_bairros.head(10).sort_values(by='indice_custo_cesta_R$')
top_10_baratos = tabela_ranking_bairros.tail(10).sort_values(by='indice_custo_cesta_R$')
bairros_plot = pd.concat([top_10_caros, top_10_baratos])
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 10))
colors = ['#d9534f']*10 + ['#5cb85c']*10
bars = ax.barh(bairros_plot['bairro'], bairros_plot['indice_custo_cesta_R$'], color=colors)
ax.set_title('Ranking de Bairros por Custo da Cesta Essencial', fontsize=16, pad=20)
ax.set_xlabel('Índice de Custo da Cesta (R$)', fontsize=12)
ax.set_ylabel('Bairro', fontsize=12)
ax.bar_label(bars, fmt='R$ %.2f', padding=3, fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, '1_grafico_ranking_bairros.png'), dpi=300)
plt.close()

# TEMA 2: Análise Competitiva entre Redes
print(" -> Gerando Análise Competitiva entre Redes...")
preco_mediano_rede = df_cesta.groupby(['rede', 'categoria_n1'])['preco_regular'].median().unstack()
custo_cesta_rede = preco_mediano_rede.sum(axis=1).sort_values(ascending=False)
tabela_ranking_redes = custo_cesta_rede.round(2).reset_index(name='indice_custo_cesta_R$')
tabela_ranking_redes.to_csv(os.path.join(pasta_resultados, '2_tabela_ranking_redes.csv'), index=False, sep=';', encoding='utf-8-sig')
matriz_competitividade = preco_mediano_rede.fillna(0).round(2)
matriz_competitividade.to_csv(os.path.join(pasta_resultados, '3_tabela_matriz_competitividade.csv'), sep=';', encoding='utf-8-sig')
fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(matriz_competitividade, annot=True, fmt=".2f", cmap="viridis_r", linewidths=.5, ax=ax)
ax.set_title('Matriz de Competitividade: Preço Mediano por Rede e Categoria', fontsize=16, pad=20)
ax.set_xlabel('Macro Categoria', fontsize=12)
ax.set_ylabel('Rede de Supermercado', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, '3_grafico_matriz_competitividade.png'), dpi=300)
plt.close()

# TEMA 3: Análise Temporal e de Volatilidade
print(" -> Gerando Análise Temporal e de Volatilidade...")
stats_preco_categoria = df.groupby('categoria_n2')['preco_regular'].agg(['mean', 'std']).dropna()
stats_preco_categoria['coef_variacao_%'] = (stats_preco_categoria['std'] / stats_preco_categoria['mean']) * 100
tabela_volatilidade = stats_preco_categoria.sort_values(by='coef_variacao_%', ascending=False)
tabela_volatilidade.round(2).to_csv(os.path.join(pasta_resultados, '4_tabela_ranking_volatilidade.csv'), sep=';', encoding='utf-8-sig')
top_20_volateis = tabela_volatilidade.head(20).sort_values(by='coef_variacao_%')
fig, ax = plt.subplots(figsize=(12, 10))
ax.barh(top_20_volateis.index, top_20_volateis['coef_variacao_%'], color='skyblue')
ax.set_title('Top 20 Categorias com Maior Volatilidade de Preços', fontsize=16, pad=20)
ax.set_xlabel('Coeficiente de Variação (%)', fontsize=12)
ax.set_ylabel('Subcategoria (Nível 2)', fontsize=12)
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, '4_grafico_volatilidade.png'), dpi=300)
plt.close()

# --- ALTERAÇÃO AQUI: Lógica para plotar a evolução de cada categoria ---
df['mes'] = df['data_pesquisa'].dt.to_period('M')
# Calcula o preço mediano de cada categoria para cada mês
preco_evolucao_categoria = df.groupby(['mes', 'categoria_n1'])['preco_regular'].median().unstack()

# Salva a tabela detalhada
tabela_evolucao_detalhada = preco_evolucao_categoria.round(2)
tabela_evolucao_detalhada.index = tabela_evolucao_detalhada.index.to_timestamp() # Converte o índice para um formato mais legível
tabela_evolucao_detalhada.to_csv(os.path.join(pasta_resultados, '5_tabela_evolucao_por_categoria.csv'), sep=';', encoding='utf-8-sig')
print(" -> Tabela '5_tabela_evolucao_por_categoria.csv' salva.")

# Gera o novo gráfico de linhas com uma linha para cada categoria
fig, ax = plt.subplots(figsize=(16, 9))
preco_evolucao_categoria.plot(ax=ax, marker='o', linestyle='-')

ax.set_title('Evolução do Preço Mediano por Categoria ao Longo de 2024', fontsize=18, pad=20)
ax.set_xlabel('Mês', fontsize=14)
ax.set_ylabel('Preço Mediano (R$)', fontsize=14)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend(title='Macro Categoria', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.savefig(os.path.join(pasta_resultados, '5_grafico_evolucao_categorias.png'), dpi=300)
print(" -> Gráfico '5_grafico_evolucao_categorias.png' (detalhado por categoria) salvo.")
plt.close()
# --- FIM DA ALTERAÇÃO ---


# TEMA 4: Síntese para o Consumidor
print(" -> Gerando Guia do Consumidor Inteligente...")
# A lógica para a tabela 6 permanece a mesma, pois ela se baseia na cesta essencial geral.
preco_mediano_bairro_rede_cat = df_cesta.groupby(['bairro', 'rede', 'categoria_n1'])['preco_regular'].median()
custo_por_cat = preco_mediano_bairro_rede_cat.unstack()
custo_cesta_bairro_rede = custo_por_cat.sum(axis=1, min_count=len(CESTA_ESSENCIAL) - 1)
custo_df = custo_cesta_bairro_rede.reset_index(name='custo_cesta')
idx_menor_custo = custo_df.loc[custo_df.groupby('bairro')['custo_cesta'].idxmin()]
tabela_guia_consumidor = idx_menor_custo.rename(columns={'rede': 'rede_mais_barata', 'custo_cesta': 'custo_minimo_cesta_R$'}).round(2)
tabela_guia_consumidor.to_csv(os.path.join(pasta_resultados, '6_tabela_guia_consumidor.csv'), index=False, sep=';', encoding='utf-8-sig')

print(" -> Insights Macro (1 a 6) gerados com sucesso.")

#======================================================================
# --- TEMA 5: ANÁLISE DETALHADA POR SUBCATEGORIA (HEATMAPS) ---
#======================================================================
print("\nGerando Insight 5: Heatmaps Detalhados por Subcategoria...")

# Identificar as redes, bairros e subcategorias mais relevantes para focar a análise
top_15_redes = df['rede'].value_counts().nlargest(15).index
top_15_bairros = df['bairro'].value_counts().nlargest(15).index
top_20_subcategorias = df['categoria_n2'].value_counts().nlargest(20).index

# Filtrar o DataFrame para conter apenas esses dados mais relevantes
df_filtrado = df[
    df['rede'].isin(top_15_redes) &
    df['bairro'].isin(top_15_bairros) &
    df['categoria_n2'].isin(top_20_subcategorias)
]
print(f" -> Foco da análise: {len(top_15_redes)} principais redes, {len(top_15_bairros)} principais bairros e {len(top_20_subcategorias)} principais subcategorias.")

# --- Heatmap: Rede vs. Subcategoria ---
matriz_rede_subcat = df_filtrado.pivot_table(index='rede', columns='categoria_n2', values='preco_regular', aggfunc='median')
matriz_rede_subcat.round(2).to_csv(os.path.join(pasta_resultados, '11_tabela_heatmap_rede_vs_subcategoria.csv'), sep=';', encoding='utf-8-sig')
print(" -> Tabela '11_tabela_heatmap_rede_vs_subcategoria.csv' salva.")

fig, ax = plt.subplots(figsize=(22, 14))
sns.heatmap(matriz_rede_subcat, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=.5, ax=ax)
ax.set_title('Heatmap de Preços: Top 15 Redes vs. Top 20 Subcategorias (Preço Mediano)', fontsize=18, pad=20)
ax.set_xlabel('Subcategoria de Produto (Nível 2)', fontsize=14)
ax.set_ylabel('Rede de Supermercado', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, '11_grafico_heatmap_rede_vs_subcategoria.png'), dpi=300)
print(" -> Gráfico '11_grafico_heatmap_rede_vs_subcategoria.png' salvo.")
plt.close()

# --- Heatmap: Bairro vs. Subcategoria ---
matriz_bairro_subcat = df_filtrado.pivot_table(index='bairro', columns='categoria_n2', values='preco_regular', aggfunc='median')
matriz_bairro_subcat.round(2).to_csv(os.path.join(pasta_resultados, '12_tabela_heatmap_bairro_vs_subcategoria.csv'), sep=';', encoding='utf-8-sig')
print(" -> Tabela '12_tabela_heatmap_bairro_vs_subcategoria.csv' salva.")

fig, ax = plt.subplots(figsize=(22, 14))
sns.heatmap(matriz_bairro_subcat, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=.5, ax=ax)
ax.set_title('Heatmap de Preços: Top 15 Bairros vs. Top 20 Subcategorias (Preço Mediano)', fontsize=18, pad=20)
ax.set_xlabel('Subcategoria de Produto (Nível 2)', fontsize=14)
ax.set_ylabel('Bairro', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(pasta_resultados, '12_grafico_heatmap_bairro_vs_subcategoria.png'), dpi=300)
print(" -> Gráfico '12_grafico_heatmap_bairro_vs_subcategoria.png' salvo.")
plt.close()


#======================================================================
# --- TEMA 6: RANKINGS DETALHADOS POR SUBCATEGORIA (TEXTO) ---
#======================================================================
print("\nGerando Insight 6: Rankings Detalhados por Subcategoria...")

# Prepara as tabelas de preço mediano por subcategoria (usando o df original completo)
preco_mediano_bairro_subcat_full = df.groupby(['bairro', 'categoria_n2'])['preco_regular'].median().unstack()
preco_mediano_rede_subcat_full = df.groupby(['rede', 'categoria_n2'])['preco_regular'].median().unstack()

# Salva as tabelas completas para consulta
preco_mediano_bairro_subcat_full.round(2).to_csv(os.path.join(pasta_resultados, '7_tabela_detalhada_bairros_por_subcategoria.csv'), sep=';', encoding='utf-8-sig')
print(" -> Tabela '7_tabela_detalhada_bairros_por_subcategoria.csv' salva.")
preco_mediano_rede_subcat_full.round(2).to_csv(os.path.join(pasta_resultados, '8_tabela_detalhada_redes_por_subcategoria.csv'), sep=';', encoding='utf-8-sig')
print(" -> Tabela '8_tabela_detalhada_redes_por_subcategoria.csv' salva.")


# Gera os rankings para as subcategorias chave e imprime no terminal
for subcategoria in SUBCATEGORIAS_CHAVE:
    print("\n" + "-"*70)
    print(f"--- RANKINGS DETALHADOS PARA A SUBCATEGORIA: {subcategoria} ---")
    print("-"*70)

    # Verifica se a subcategoria existe nos dados antes de tentar acessá-la
    if subcategoria in preco_mediano_bairro_subcat_full.columns and subcategoria in preco_mediano_rede_subcat_full.columns:
        # Ranking de Bairros
        ranking_bairro = preco_mediano_bairro_subcat_full[subcategoria].dropna().sort_values(ascending=False)
        print(f"\n[ Ranking de Bairros para '{subcategoria}' ]")
        print("\nTop 5 Bairros MAIS CAROS:")
        print(ranking_bairro.head(5).round(2).reset_index(name='preco_mediano_R$'))
        print("\nTop 5 Bairros MAIS BARATOS:")
        print(ranking_bairro.tail(5).sort_values().round(2).reset_index(name='preco_mediano_R$'))
        
        # Ranking de Redes
        ranking_rede = preco_mediano_rede_subcat_full[subcategoria].dropna().sort_values(ascending=False)
        print(f"\n[ Ranking de Redes para '{subcategoria}' ]")
        print("\nTop 5 Redes MAIS CARAS:")
        print(ranking_rede.head(5).round(2).reset_index(name='preco_mediano_R$'))
        print("\nTop 5 Redes MAIS BARATAS:")
        print(ranking_rede.tail(5).sort_values().round(2).reset_index(name='preco_mediano_R$'))
    else:
        print(f"AVISO: Não há dados suficientes para gerar rankings para a subcategoria '{subcategoria}'.")


print("\n----------------------------------------------------")
print("✅ ANÁLISE COMPLETA E DETALHADA CONCLUÍDA! ✅")
print(f"Todos os arquivos foram salvos na pasta '{pasta_resultados}'.")
print("----------------------------------------------------")
