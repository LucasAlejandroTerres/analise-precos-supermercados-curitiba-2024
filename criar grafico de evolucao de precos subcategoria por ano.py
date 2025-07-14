import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import os
import sys

#======================================================================
# --- 1. CONFIGURAÇÃO ---
#======================================================================
print("Iniciando a geração do painel de gráficos de evolução temporal...")

# --- Caminho do Dataset Final ---
caminho_dataset_pronto = r'D:\CliqueEconomia_TCC_DATASET_PRONTO.csv'

# --- Pasta para salvar os resultados ---
pasta_resultados = r'D:\resultados_tcc'
if not os.path.exists(pasta_resultados):
    os.makedirs(pasta_resultados)
print(f"O gráfico será salvo na pasta: '{pasta_resultados}'")

# --- Definições ---
# Selecionando as 12 subcategorias mais relevantes para um painel 4x3
SUBCATEGORIAS_PAINEL = [
    'LEITE', 'ARROZ', 'FEIJAO', 'CARNE_BOVINA', 'AVES', 'PAES', 'OVOS', 
    'FRUTAS', 'LEGUMES_E_VERDURAS', 'QUEIJO', 'EMBUTIDOS', 'CAFE_E_CHA'
]

#======================================================================
# --- 2. CARREGAMENTO E PREPARAÇÃO DOS DADOS ---
#======================================================================
try:
    df = pd.read_csv(caminho_dataset_pronto, delimiter=';', encoding='utf-8-sig')
    df['data_pesquisa'] = pd.to_datetime(df['data_pesquisa'], errors='coerce')
    df.dropna(subset=['data_pesquisa'], inplace=True)
    print(f"Dataset com {len(df)} linhas carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO CRÍTICO: Arquivo '{caminho_dataset_pronto}' não encontrado.")
    sys.exit()

#======================================================================
# --- 3. ANÁLISE E GERAÇÃO DE DADOS PARA O GRÁFICO ---
#======================================================================
print("Calculando o preço mediano mensal para as subcategorias selecionadas...")
df_filtrado = df[df['categoria_n2'].isin(SUBCATEGORIAS_PAINEL)].copy()
df_filtrado['mes'] = df_filtrado['data_pesquisa'].dt.to_period('M')
preco_evolucao = df_filtrado.groupby(['mes', 'categoria_n2'])['preco_regular'].median().unstack()

# Garante que a ordem das colunas no plot seja a mesma da nossa lista
preco_evolucao = preco_evolucao[SUBCATEGORIAS_PAINEL]

#======================================================================
# --- 4. GERAÇÃO DO PAINEL DE GRÁFICOS (VISUALIZAÇÃO "CAPRICHADA") ---
#======================================================================
print("Gerando o painel de gráficos...")

plt.style.use('seaborn-v0_8-ticks')
# Cria uma grade de 4 linhas e 3 colunas para os 12 gráficos
fig, axes = plt.subplots(4, 3, figsize=(18, 22), sharex=False) # sharex=False para melhor controle

# Adiciona um título principal para toda a figura
fig.suptitle('Evolução do Preço Mediano das Principais Subcategorias (Curitiba - 2024)', fontsize=24, fontweight='bold', y=0.97)

# O `axes.flat` transforma a grade 4x3 em uma lista única para facilitar o loop
for ax, subcategoria in zip(axes.flat, SUBCATEGORIAS_PAINEL):
    if subcategoria in preco_evolucao.columns:
        # Pega os dados da subcategoria atual
        dados_plot = preco_evolucao[subcategoria].dropna()
        # Converte o índice do tipo Período para Timestamp para o plot
        eixo_x_datas = dados_plot.index.to_timestamp()
        
        # Plota os dados
        ax.plot(eixo_x_datas, dados_plot.values, marker='o', markersize=5, linestyle='-')
        
        # --- Estilização de cada mini-gráfico ---
        ax.set_title(subcategoria.replace('_', ' ').title(), fontsize=16, fontweight='bold')
        ax.set_ylabel('Preço Mediano (R$)', fontsize=12)
        ax.grid(True, which='both', linestyle=':', linewidth=0.7)
        
        # Formata o eixo Y como moeda (R$)
        ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('R$ {x:,.2f}'))
        
        # Formata o eixo X com os nomes dos meses
        ax.set_xticks(eixo_x_datas)
        ax.set_xticklabels([d.strftime('%b') for d in eixo_x_datas], rotation=45, ha='right')

# Remove os eixos dos subplots que não foram usados (se houver menos de 12)
for ax in axes.flat[len(SUBCATEGORIAS_PAINEL):]:
    ax.set_visible(False)

# Ajusta o layout para evitar sobreposição
plt.tight_layout(rect=[0, 0, 1, 0.95])

#======================================================================
# --- 5. EXPORTAÇÃO ---
#======================================================================
caminho_saida = os.path.join(pasta_resultados, 'painel_evolucao_subcategorias.png')
plt.savefig(caminho_saida, dpi=300)
print(f" -> Painel de gráficos salvo com sucesso em: '{os.path.basename(caminho_saida)}'")
plt.close()

print("\n----------------------------------------------------")
print("✅ Processo concluído! ✅")
print("----------------------------------------------------")