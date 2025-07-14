import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =======================
# 1. CARREGAMENTO DO DATASET
# =======================
caminho_arquivo = r'D:\resultados_tcc\3_tabela_matriz_competitividade.csv'

# Carrega o arquivo
df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8-sig')

# =======================
# 2. ESTATÍSTICAS DESCRITIVAS
# =======================
print("=== ESTATÍSTICAS DESCRITIVAS DA VARIÁVEL 'preco_regular' ===")
estatisticas = df['preco_regular'].describe()
print(estatisticas)

# =======================
# 3. PLOTAGEM DO BOXPLOT
# =======================
plt.figure(figsize=(10, 1.5))
sns.boxplot(x=df['preco_regular'], color='skyblue')
plt.title('Boxplot dos Preços Regulares Observados')
plt.xlabel('Preço (R$)')
plt.grid(True, axis='x', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('boxplot_preco_regular.png', dpi=300)
plt.show()
