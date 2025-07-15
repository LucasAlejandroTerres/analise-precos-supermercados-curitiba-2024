import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

# --- 1. CONFIGURAÇÕES ---
# URL do repositório de dados abertos
URL_DADOS = 'https://dadosabertos.c3sl.ufpr.br/curitiba/CliqueEconomia/'

# Pasta local para salvar os arquivos baixados e o resultado final
PASTA_SAIDA = 'dados_clique_economia'

# Nome do arquivo CSV consolidado que será gerado
ARQUIVO_FINAL = 'CliqueEconomia_Consolidado_2024.csv'

# --- 2. FUNÇÃO PARA LISTAR ARQUIVOS NO REPOSITÓRIO ---
def listar_arquivos_csv(url):
    """
    Acessa a URL do repositório e extrai todos os links de arquivos CSV.
    """
    print(f"Acessando o repositório em: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para status ruins (ex: 404)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encontra todas as tags 'a' (links) cujo href termina com '.csv'
        links_csv = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.csv')]
        print(f"Encontrados {len(links_csv)} arquivos CSV no total.")
        return links_csv
    except requests.exceptions.RequestException as e:
        print(f"ERRO: Falha ao acessar a URL. Verifique sua conexão. Detalhe: {e}")
        sys.exit()

# --- 3. EXECUÇÃO DO PROCESSO DE EXTRAÇÃO ---
if __name__ == "__main__":
    # Garante que a pasta de saída exista
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)
        print(f"Pasta '{PASTA_SAIDA}' criada.")

    # Etapa de Extração
    todos_os_arquivos = listar_arquivos_csv(URL_DADOS)

    # Filtra apenas os arquivos relevantes (ano 2024 e de 'Base_de_Dados')
    print("\nFiltrando arquivos para o ano de 2024...")
    arquivos_para_baixar = [
        f for f in todos_os_arquivos 
        if "2024" in f and "Base_de_Dados" in f
    ]
    print(f"Selecioandos {len(arquivos_para_baixar)} arquivos para download.")

    # Loop para baixar cada arquivo CSV filtrado
    print("\nIniciando download dos arquivos...")
    for nome_arquivo in arquivos_para_baixar:
        caminho_local = os.path.join(PASTA_SAIDA, nome_arquivo)
        # Verifica se o arquivo já existe para não baixar novamente
        if not os.path.exists(caminho_local):
            url_arquivo = URL_DADOS + nome_arquivo
            print(f"  Baixando '{nome_arquivo}'...")
            try:
                r = requests.get(url_arquivo, stream=True)
                r.raise_for_status()
                with open(caminho_local, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            except requests.exceptions.RequestException as e:
                print(f"    -> Falha ao baixar {nome_arquivo}. Erro: {e}")
        else:
            print(f"  -> Arquivo '{nome_arquivo}' já existe. Pulando.")
    print("Download concluído.")    

    # Etapa de Consolidação (Concatenação)
    print("\nIniciando consolidação dos arquivos em um único CSV...")
    lista_dfs = []
    arquivos_baixados = [f for f in os.listdir(PASTA_SAIDA) if f.endswith('.csv') and "2024" in f and "Base_de_Dados" in f]

    for nome_arquivo in arquivos_baixados:
        caminho_completo = os.path.join(PASTA_SAIDA, nome_arquivo)
        try:
            # Lê cada CSV. O encoding 'latin-1' é robusto para dados governamentais brasileiros.
            df_temp = pd.read_csv(caminho_completo, delimiter=';', encoding='latin-1', low_memory=False)
            lista_dfs.append(df_temp)
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")

    if lista_dfs:
        # Concatena todos os DataFrames da lista em um único
        df_consolidado = pd.concat(lista_dfs, ignore_index=True)
        print(f"Total de {len(df_consolidado)} registros consolidados.")

        # Salva o resultado final
        caminho_final = os.path.join(PASTA_SAIDA, ARQUIVO_FINAL)
        df_consolidado.to_csv(caminho_final, index=False, sep=';', encoding='utf-8-sig')
        print(f"\n✅ Processo concluído! Arquivo consolidado salvo em: '{caminho_final}'")
    else:
        print("\nNenhum dado para consolidar. Processo encerrado.")