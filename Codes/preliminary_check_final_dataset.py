import pandas as pd
import sys

#======================================================================
# --- 1. CONFIGURAÇÃO ---
#======================================================================
# ▼▼▼ ATENÇÃO: COLOQUE O CAMINHO CORRETO DO SEU ARQUIVO FINAL AQUI ▼▼▼
caminho_do_seu_dataset_final = r'D:\CliqueEconomia_TCC_DATASET_PRONTO.csv' # Exemplo
# ▲▲▲ ATENÇÃO: COLOQUE O CAMINHO CORRETO DO SEU ARQUIVO FINAL AQUI ▲▲▲

#======================================================================
# --- EXECUÇÃO DA VALIDAÇÃO ---
#======================================================================
try:
    print("Iniciando Script Final de Validação de Qualidade...")
    # Usando utf-8-sig para ler corretamente arquivos salvos com essa codificação (padrão dos nossos scripts)
    df = pd.read_csv(caminho_do_seu_dataset_final, delimiter=';', encoding='utf-8-sig')
    print(f"Dataset com {len(df)} linhas carregado com sucesso.\n")
except FileNotFoundError:
    print(f"ERRO CRÍTICO: Arquivo não encontrado em '{caminho_do_seu_dataset_final}'")
    print("Por favor, verifique se o nome e o caminho do arquivo na variável 'caminho_do_seu_dataset_final' estão corretos.")
    sys.exit()
except Exception as e:
    print(f"ERRO ao carregar o arquivo: {e}")
    sys.exit()

# --- 1. VERIFICAÇÃO DE VALORES NULOS ---
print("\n" + "="*50)
print("--- 1. VERIFICAÇÃO DE VALORES NULOS ---")
print("="*50)
nulos_por_coluna = df.isnull().sum()
nulos_encontrados = nulos_por_coluna[nulos_por_coluna > 0]
if nulos_encontrados.empty:
    print("✅ STATUS: Ótimo! Nenhuma coluna possui valores nulos.")
else:
    print("⚠️ PONTO DE ATENÇÃO: Foram encontrados valores nulos nas seguintes colunas:")
    print(nulos_encontrados)

# --- 2. VERIFICAÇÃO DE DUPLICATAS ---
print("\n" + "="*50)
print("--- 2. VERIFICAÇÃO DE DUPLICATAS ---")
print("="*50)
duplicatas = df.duplicated().sum()
print(f"Número de linhas completamente duplicadas encontradas: {duplicatas}")
if duplicatas > 0:
    print("AVISO: Recomenda-se investigar se essas duplicatas são esperadas ou se devem ser removidas.")
else:
    print("✅ STATUS: Ótimo! Não há linhas 100% duplicadas no dataset.")


# --- 3. VERIFICAÇÃO DE ANOMALIAS DE PREÇO (OUTLIERS) ---
print("\n" + "="*50)
print("--- 3. VERIFICAÇÃO DE ANOMALIAS DE PREÇO ---")
print("="*50)
print("\n[3.1] Estatísticas Descritivas da coluna 'preco_regular':")
print(df['preco_regular'].describe().round(2))
print("\n[3.2] Top 10 preços mais altos no dataset para verificação manual:")
print(df.sort_values(by='preco_regular', ascending=False)[['descricao', 'rede', 'bairro', 'preco_regular']].head(10).reset_index(drop=True))
print("\nAnálise de Preços: Verifique se os preços mais altos são para produtos plausíveis (ex: carnes nobres, fórmulas infantis, vinhos) ou se indicam erros.")


# --- 4. VERIFICAÇÃO DA CONSISTÊNCIA DAS CATEGORIAS ---
print("\n" + "="*50)
print("--- 4. VERIFICAÇÃO DA CONSISTÊNCIA DAS CATEGORIAS ---")
print("="*50)
print("\n[4.1] Contagem de itens por Macro Categoria (Nível 1):")
print(df['categoria_n1'].value_counts())
outros_n2 = df[df['categoria_n2'] == 'OUTROS']
print(f"\n[4.2] Total de produtos que restaram na subcategoria 'OUTROS': {len(outros_n2)}")
if not outros_n2.empty:
    print("AVISO: Ainda existem produtos classificados como 'OUTROS'. Amostra:")
    print(outros_n2['descricao'].value_counts().head(10))
else:
    print("✅ STATUS: Perfeito! Nenhum produto foi classificado como 'OUTROS'.")

# --- 5. VERIFICAÇÃO DA INTEGRIDADE DOS ENDEREÇOS ---
print("\n" + "="*50)
print("--- 5. VERIFICAÇÃO DA INTEGRIDADE DOS ENDEREÇOS ---")
print("="*50)
enderecos_nulos = df['bairro'].isnull().sum()
print(f"Total de registros sem informação de bairro: {enderecos_nulos}")
if enderecos_nulos == 0:
    print("✅ STATUS: Perfeito! Todos os registros possuem endereços completos.")
else:
    print("⚠️ PONTO DE ATENÇÃO: Existem registros onde o endereço não foi preenchido.")

print("\n" + "="*50)
print("--- VALIDAÇÃO DE INCONSISTÊNCIAS CONCLUÍDA ---")
print("="*50)