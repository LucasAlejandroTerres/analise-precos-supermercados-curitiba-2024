import pandas as pd
import re
import sys

# ======================================================================
# --- 1. CONFIGURAÇÃO E DICIONÁRIOS FINAIS (vFinal) ---
# ======================================================================
print("Iniciando a operação final de preparação de dados...")

# --- Caminhos dos Arquivos de Entrada e Saída ---
# Altere os caminhos se os arquivos estiverem em locais diferentes
caminho_principal = r'S:\CliqueEconomia_dataset_variaveisnormalizadas_V2.csv'
caminho_enderecos_com_id = r'S:\endereco_normalizado_COM_ID.csv'
caminho_gabarito_ouro = 'Classificao_Refinada_de_Produtos.csv'
caminho_saida_definitivo = r'S:\CliqueEconomia_DATASET_PRONTO_PARA_TCC.csv'

# --- Dicionários para Classificação ---

# CAMADA 1: GABARITO DE OURO (Exceções e correções manuais com prioridade máxima)
# Este dicionário contém as regras mais específicas para corrigir erros de contexto.
gabarito_ouro_map = {
    'leite condensado': 'DOCES_E_SOBREMESAS',
    'doce de leite': 'DOCES_E_SOBREMESAS',
    'creme de leite': 'CREME_E_MANTEIGA',
    'leite de coco': 'DOCES_E_SOBREMESAS',
    'composto lacteo': 'PRODUTOS_INFANTIS',
    'leite fermentado': 'IOGURTE',
    'bebida lactea': 'IOGURTE',
    'batata doce': 'LEGUMES_E_VERDURAS',
    'batata palha': 'BISCOITOS_E_SNACKS',
    'batata frita': 'BISCOITOS_E_SNACKS',
    'couve manteiga': 'LEGUMES_E_VERDURAS',
    'cebola para conserva': 'LEGUMES_E_VERDURAS',
    'milho verde': 'LEGUMES_E_VERDURAS',
    'farinha de arroz': 'FARINACEOS',
    'pao fatiado': 'PAES',
    'pao bisnaguinha': 'PAES',
    'pao frances': 'PAES',
    'caldo de galinha': 'MOLHOS_E_CONDIMENTOS',
    'atum ralado': 'ENLATADOS_E_CONSERVAS',
    'sardinha molho': 'ENLATADOS_E_CONSERVAS',
    'sabao em po': 'LIMPEZA_ROUPA',
    'sabao em barras': 'LIMPEZA_ROUPA',
    'suco integral': 'SUCO_E_NECTAR',
    'po p/ refresco': 'SUCO_E_NECTAR',
    'po p/ bebida': 'SUCO_E_NECTAR',
    'filtro de papel': 'UTILIDADES_DOMESTICAS',
    'filtro p/cafe': 'UTILIDADES_DOMESTICAS',
    'limpa vidros': 'LIMPEZA_CASA',
    'geleia de morango': 'DOCES_E_SOBREMESAS',
    'geleia de frutas': 'DOCES_E_SOBREMESAS',
    'margarina cremosa': 'CREME_E_MANTEIGA',
    'manteiga primeira qualidade': 'CREME_E_MANTEIGA',
    'formula infantil': 'PRODUTOS_INFANTIS',
    'nestogeno': 'PRODUTOS_INFANTIS',
    'cafe vacuo': 'CAFE_E_CHA',
    'salsichao': 'EMBUTIDOS',
    'charque': 'CARNES',
    'farofa': 'FARINACEOS',
    'bolinho recheado': 'BISCOITOS_E_SNACKS',
    'tempero completo': 'MOLHOS_E_CONDIMENTOS',
    'tempero alho': 'MOLHOS_E_CONDIMENTOS',
    'nata': 'CREME_E_MANTEIGA',
    'cereal alimentacao infantil': 'PRODUTOS_INFANTIS',
    'creme de hidratacao': 'CUIDADOS_PESSOAIS',
    'cachaca': 'BEBIDAS_ALCOOLICAS',
    'salsa': 'LEGUMES_E_VERDURAS',
    'cheiro verde': 'LEGUMES_E_VERDURAS',
    'hortalica': 'LEGUMES_E_VERDURAS',
    'saponaceo cremoso': 'LIMPEZA_CASA',
    'pipoca para microondas': 'BISCOITOS_E_SNACKS',
    'aveia em flocos': 'CEREAIS_E_GRANOLAS',
    'barra de nuts': 'CEREAIS_E_GRANOLAS',
    'barra de cereais': 'CEREAIS_E_GRANOLAS',
    'champignon': 'ENLATADOS_E_CONSERVAS',
    'grao de bico': 'FEIJAO',
    'maria mole': 'DOCES_E_SOBREMESAS'
}

# CAMADA 2: DICIONÁRIO PRINCIPAL (Regras gerais para o restante)
keyword_map_principal = {
    'QUEIJO': ['queijo', 'mussarela', 'prato', 'ricota', 'requeijao', 'parmesao', 'minas', 'ralado', 'cream cheese'],
    'IOGURTE': ['iogurte', 'yakult', 'petit suisse'],
    'EMBUTIDOS': ['presunto', 'mortadela', 'salame', 'linguica', 'calabresa', 'bacon', 'salsicha', 'fatiado', 'embutido', 'morcela'],
    'CONGELADOS': ['hamburguer', 'congelada', 'congelado'],
    'AVES': ['frango', 'coxa', 'sobrecoxa', 'peito', 'asa', 'ave', 'galinha', 'sambiquira'],
    'CARNE_BOVINA': ['bovina', 'alcatra', 'patinho', 'coxao', 'picanha', 'moida', 'costela', 'osso', 'vacuo', 'pedaco', 'file'],
    'CARNE_SUINA': ['suina', 'pernil', 'lombo', 'bisteca', 'panceta', 'banha'],
    'ARROZ': ['arroz', 'polido', 'parboilizado'],
    'FEIJAO': ['feijao', 'preto', 'carioca', 'grao'],
    'ACUCAR_E_ADOCANTE': ['acucar', 'adocante', 'doce'],
    'CAFE_E_CHA': ['cafe', 'cha', 'cappuccino', 'erva', 'mate'],
    'OLEO_E_AZEITE': ['oleo', 'soja', 'azeite'],
    'FARINACEOS': ['farinha', 'fuba', 'trigo', 'polenta', 'polvilho', 'tapioca'],
    'MASSAS': ['macarrao', 'nhoque', 'lasanha', 'massa', 'pastel', 'sopao'],
    'MOLHOS_E_CONDIMENTOS': ['molho', 'extrato', 'maionese', 'ketchup', 'mostarda', 'sal', 'especiarias', 'vinagre', 'catchup', 'caldo', 'tempero', 'vinagrete'],
    'BISCOITOS_E_SNACKS': ['biscoito', 'bolacha', 'torrada', 'salgadinho', 'waffer', 'cookie', 'cookies', 'pipoca'],
    'ENLATADOS_E_CONSERVAS': ['milho', 'ervilha', 'seleta', 'atum', 'sardinha', 'palmito', 'azeitona', 'conserva', 'pessegos'],
    'DOCES_E_SOBREMESAS': ['chocolate', 'achocolatado', 'bombom', 'bala', 'goiabada', 'gelatina', 'pudim', 'mel', 'barra'],
    'FERMENTO_E_MISTURAS': ['fermento', 'biologico', 'mistura', 'bolo', 'po'],
    'CEREAIS_E_GRANOLAS': ['granola', 'castanha', 'nozes', 'amendoim', 'lentilha', 'sagu', 'quirerinha', 'aveia', 'nuts'],
    'PAES': ['pao', 'bisnaga'],
    'FRUTAS': ['banana', 'maca', 'laranja', 'mamao', 'uva', 'limao', 'frutas', 'manga', 'morango', 'maracuja', 'melao', 'abacaxi', 'goiaba', 'abacate', 'pera', 'pessego', 'kiwi', 'ponkan', 'ameixa', 'caqui', 'melancia', 'mimosa', 'jabuticaba', 'figo'],
    'LEGUMES_E_VERDURAS': ['batata', 'cebola', 'alho', 'tomate', 'cenoura', 'alface', 'couve', 'brocolis', 'abobora', 'pepino', 'pimentao', 'repolho', 'chuchu', 'beterraba', 'berinjela', 'abobrinha', 'kabotia', 'moranga', 'agriao', 'rucula', 'acelga', 'aipim', 'cebolinha', 'gengibre', 'inhame', 'rabanete', 'quiabo', 'vagem', 'pinhao'],
    'OVOS': ['ovos', 'ovo'],
    'BEBIDAS_ALCOOLICAS': ['cerveja', 'vinho', 'conhaque', 'energetico', 'vodka', 'whisky'],
    'SUCO_E_NECTAR': ['suco', 'nectar', 'del valle', 'tang'],
    'REFRIGERANTE': ['refrigerante', 'coca-cola', 'guarana', 'pepsi', 'soda', 'pet'],
    'AGUA': ['agua mineral'],
    'LIMPEZA_ROUPA': ['sabao', 'amaciante', 'lava roupas', 'tira manchas'],
    'LIMPEZA_CASA': ['agua sanitaria', 'desinfetante', 'multiuso', 'limpador', 'detergente', 'cera', 'alcool', 'saponaceo'],
    'UTILIDADES_DOMESTICAS': ['filtro', 'esponja', 'aco', 'saco', 'lixo', 'plastico', 'fosforo', 'papel toalha', 'guardanapo', 'rolo', 'folha', 'vela', 'vassoura', 'toalha', 'rodo', 'lampada'],
    'HIGIENE_BUCAL': ['creme dental', 'pasta de dente', 'escova dental', 'fio dental', 'enxaguante'],
    'CUIDADOS_PESSOAIS': ['sabonete', 'shampoo', 'condicionador', 'absorvente', 'desodorante', 'locao', 'gel'],
    'PAPEL_HIGIENICO': ['papel higienico'],
    'PRODUTOS_INFANTIS': ['fralda', 'lenco umedecido'],
    'LEITE': ['leite'],
    'CREME_E_MANTEIGA': ['manteiga', 'margarina'],
    'COCO': ['coco'],
}

# MAPA FINAL E COMPLETO (Nível 2 -> Nível 1)
macro_map = {
    'LEITE': 'LATICINIOS_E_FRIOS', 'QUEIJO': 'LATICINIOS_E_FRIOS', 'IOGURTE': 'LATICINIOS_E_FRIOS', 'CREME_E_MANTEIGA': 'LATICINIOS_E_FRIOS', 'EMBUTIDOS': 'LATICINIOS_E_FRIOS',
    'CONGELADOS': 'CONGELADOS_E_FRIOS', 'CARNE_BOVINA': 'CARNES', 'AVES': 'CARNES', 'CARNE_SUINA': 'CARNES', 'CARNES': 'CARNES',
    'ARROZ': 'MERCEARIA', 'FEIJAO': 'MERCEARIA', 'ACUCAR_E_ADOCANTE': 'MERCEARIA', 'CAFE_E_CHA': 'MERCEARIA', 'OLEO_E_AZEITE': 'MERCEARIA', 'FARINACEOS': 'MERCEARIA', 'MASSAS': 'MERCEARIA', 'MOLHOS_E_CONDIMENTOS': 'MERCEARIA', 'BISCOITOS_E_SNACKS': 'MERCEARIA', 'ENLATADOS_E_CONSERVAS': 'MERCEARIA', 'DOCES_E_SOBREMESAS': 'MERCEARIA', 'FERMENTO_E_MISTURAS': 'MERCEARIA', 'CEREAIS_E_GRANOLAS': 'MERCEARIA',
    'PAES': 'PADARIA',
    'LEGUMES_E_VERDURAS': 'HORTIFRUTI', 'FRUTAS': 'HORTIFRUTI', 'OVOS': 'HORTIFRUTI', 'COCO': 'HORTIFRUTI',
    'REFRIGERANTE': 'BEBIDAS', 'SUCO_E_NECTAR': 'BEBIDAS', 'AGUA': 'BEBIDAS', 'BEBIDAS_ALCOOLICAS': 'BEBIDAS',
    'LIMPEZA_ROUPA': 'LIMPEZA_E_UTILIDADES', 'LIMPEZA_CASA': 'LIMPEZA_E_UTILIDADES', 'UTILIDADES_DOMESTICAS': 'LIMPEZA_E_UTILIDADES',
    'HIGIENE_BUCAL': 'HIGIENE_PESSOAL', 'CUIDADOS_PESSOAIS': 'HIGIENE_PESSOAL', 'PAPEL_HIGIENICO': 'HIGIENE_PESSOAL',
    'PRODUTOS_INFANTIS': 'INFANTIL', 'OUTROS': 'OUTROS'
}

# ======================================================================
# --- FUNÇÕES DE LÓGICA ---
# ======================================================================
def normalizar_texto(texto):
    """Converte para minúsculas e remove acentos."""
    texto = str(texto).lower()
    mapa_acentos = {'á':'a','à':'a','â':'a','ã':'a','é':'e','ê':'e','í':'i','î':'i','ó':'o','ô':'o','õ':'o','ç':'c','ú':'u','û':'u'}
    for acento, sem_acento in mapa_acentos.items():
        texto = texto.replace(acento, sem_acento)
    return texto

def categorizar_produto_final(descricao_norm):
    """Classifica um produto usando a lógica de duas camadas."""
    # Camada 1: Gabarito de Ouro (Exceções e correções manuais)
    for keyword, categoria in gabarito_ouro_map.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', descricao_norm):
            return categoria
    
    # Camada 2: Dicionário Principal (Regras gerais)
    for categoria, keywords in keyword_map_principal.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', descricao_norm):
                return categoria
    return 'OUTROS'  # Fallback final

def padronizar_rede(nome_rede):
    """Padroniza nomes de redes de supermercados."""
    nome_rede_norm = str(nome_rede).upper()
    if 'CONDOR' in nome_rede_norm: return 'CONDOR'
    if 'MUFFATO' in nome_rede_norm: return 'SUPER MUFFATO'
    if 'NOGUEIRA' in nome_rede_norm: return 'SUPERMERCADO NOGUEIRA'
    if 'MASTER' in nome_rede_norm: return 'REDE MASTER'
    if 'CURITIBA' in nome_rede_norm: return 'SUPERMERCADO CURITIBA'
    return nome_rede_norm

# ======================================================================
# --- EXECUÇÃO DO SCRIPT FINAL ---
# ======================================================================
try:
    # --- ETAPA 1: CARREGAR E PREPARAR DADOS ---
    print("Carregando arquivos de entrada...")
    df = pd.read_csv(caminho_principal, delimiter=';', encoding='utf-8-sig')
    df_enderecos = pd.read_csv(caminho_enderecos_com_id, delimiter=';', encoding='utf-8-sig')
    
    # Adicionado try-except para o gabarito, caso ele não exista
    try:
        df_gabarito_ouro = pd.read_csv(caminho_gabarito_ouro, delimiter=';', encoding='latin-1')
        print("Arquivo de gabarito carregado.")
        # Prepara o mapa do gabarito
        df_gabarito_ouro.columns = df_gabarito_ouro.columns.str.strip()
        df_gabarito_ouro.dropna(subset=['descricao', 'categoria_correta'], inplace=True)
        df_gabarito_ouro['descricao_norm'] = df_gabarito_ouro['descricao'].apply(normalizar_texto)
        df_gabarito_ouro['categoria_correta_norm'] = df_gabarito_ouro['categoria_correta'].str.upper().str.replace(' ', '_')
        gabarito_map = df_gabarito_ouro.set_index('descricao_norm')['categoria_correta_norm'].to_dict()
    except FileNotFoundError:
        print("AVISO: Arquivo 'Classificao_Refinada_de_Produtos.csv' não encontrado. A classificação será feita sem o gabarito manual.")
        gabarito_map = {} # Usa um dicionário vazio se o arquivo não existir
    
    # --- ETAPA 2: LIMPEZA E TRANSFORMAÇÃO ---
    print("Realizando limpeza e padronização dos dados...")
    df.dropna(subset=['preco_regular', 'descricao'], inplace=True)
    df['preco_regular'] = pd.to_numeric(df['preco_regular'].astype(str).str.replace(',', '.'), errors='coerce')
    df = df[df['preco_regular'] > 0]
    df['id_empresa'] = df['id_empresa'].astype(str)
    df_enderecos['id_empresa'] = df_enderecos['id_empresa'].astype(str)
    df['rede'] = df['rede'].apply(padronizar_rede)
    
    # --- ETAPA 3: JUNÇÃO DE ENDEREÇOS ---
    print("Juntando informações de endereço...")
    df_final = pd.merge(df, df_enderecos, on='id_empresa', how='left')

    # --- ETAPA 4: CLASSIFICAÇÃO ---
    print("Classificando todos os produtos...")
    df_final['descricao_norm'] = df_final['descricao'].apply(normalizar_texto)
    df_final['categoria_n2'] = df_final['descricao_norm'].apply(lambda x: categorizar_produto_final(x, gabarito_ouro_map))
    df_final['categoria_n1'] = df_final['categoria_n2'].map(macro_map)
    df_final['categoria_n1'].fillna('OUTROS', inplace=True) # Garante que não haja nulos na categoria n1

    # --- ETAPA 5: LIMPEZA FINAL E EXPORTAÇÃO ---
    print("Realizando limpeza final (duplicatas e organização)...")
    df_final.drop_duplicates(inplace=True)
    
    ordem_colunas = [
        'data_pesquisa', 'id_empresa', 'rede', 'bairro', 'id_produto', 'descricao', 
        'categoria_n1', 'categoria_n2', 'preco_regular', 'logradouro_tipo', 
        'logradouro_nome', 'numero', 'cidade', 'estado'
    ]
    df_final = df_final.drop(columns=['descricao_norm', 'endereco_completo'], errors='ignore')
    df_final = df_final[[col for col in ordem_colunas if col in df_final.columns]]
    
    df_final.to_csv(caminho_saida_definitivo, index=False, sep=';', encoding='utf-8-sig')

    # Verificação Final de 'OUTROS'
    outros_final = df_final[df_final['categoria_n2'] == 'OUTROS']
    
    print("\n----------------------------------------------------")
    print("🏆 PROCESSO CONCLUÍDO! 🏆")
    print(f"Dataset definitivo salvo em: {caminho_saida_definitivo}")
    print(f"Total de linhas no arquivo final: {len(df_final)}")
    print(f"Total de linhas que restaram como 'OUTROS': {len(outros_final)}")
    if not outros_final.empty:
        print("\nAmostra dos itens que restaram como 'OUTROS':")
        print(outros_final['descricao'].value_counts().head(10))
    print("----------------------------------------------------")

except Exception as e:
    print(f"\nOcorreu um erro inesperado durante o processo: {e}")
    sys.exit()

