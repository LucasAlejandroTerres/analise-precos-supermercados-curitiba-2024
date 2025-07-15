<a id="portuguese"></a>

# 🗺️🛒💰Onde é Mais Barato Comprar em Curitiba: Análise dos Preços no Varejo por Bairro com Dados Públicos

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**Versão em Inglês 🇬🇧**](#english)

## 📖 Descrição do Projeto
Este projeto consiste em uma análise exploratória de dados sobre a dispersão de preços no setor de varejo alimentício da cidade de Curitiba, utilizando dados públicos do programa "Clique Economia" referentes ao ano de 2024. O objetivo principal é transformar mais de 700.000 registros de preços brutos em insights acionáveis que possam empoderar o consumidor em suas decisões de compra.

O trabalho explora a dinâmica de preços através de três eixos principais: **geográfico** (comparando bairros), **competitivo** (comparando redes de supermercado) e **temporal** (analisando a evolução dos preços ao longo dos meses).

---

## 🎯 Objetivos
* Mapear a variação de custos de uma cesta de consumo representativa entre os diferentes bairros.  
* Comparar o posicionamento de preço das principais redes de supermercado.  
* Identificar as categorias de produtos com maior volatilidade de preços.  
* Sintetizar os achados em um guia prático para o consumidor curitibano.  

---

## 🛠️ Metodologia e Pipeline de Dados
1. **Extração:** Automação da coleta de centenas de arquivos CSV diários do portal de dados abertos.  
2. **Limpeza de Dados:** Tratamento de valores nulos, correção de tipos de dados e remoção de duplicatas.  
3. **Enriquecimento e Normalização:**  
   * **Normalização Geográfica:** Padronização dos bairros de Curitiba.  
   * **Padronização de Redes:** Unificação de nomes variantes de uma mesma rede.  
   * **Sistema de Categorização:** Classificação hierárquica em dois níveis (`categoria_n1`, `categoria_n2`) para mais de 700 mil descrições de produtos.  

---

## 📈 Amostra dos Resultados
#### 🏘️ Ranking de Bairros por Custo da Cesta Essencial  
Mostra os 10 bairros mais caros e os 10 mais baratos para uma cesta padrão.  
![Ranking de Bairros](Results/Graphs/1_grafico_ranking_bairros.png)

#### 🏬 Matriz de Competitividade por Rede e Categoria  
Aponta quais redes são mais competitivas em cada categoria.  
![Matriz de Competitividade](Results/Graphs/3_grafico_matriz_competitividade_redes_macrocategoria.png)

#### 📈 Evolução Temporal das Subcategorias  
Acompanha a trajetória de preços das subcategorias ao longo do ano.  
![Evolução das Subcategorias](Results/Graphs/painel_evolucao_subcategorias.png)

#### 📊 Guia do Consumidor por Bairro  
Indica, bairro a bairro, qual rede tem os menores preços médios.  
![Guia por Bairro](Results/Graphs/Ranking_RedesMaisBaratas_Bairro.png)

---

### 📂 Quer ver todos os gráficos e planilhas?
[**Pasta completa de gráficos e planilhas**](Results/) — tá tudo lá!

---

## 🚀 Como Executar o Projeto
1. Clone este repositório.  
2. Crie um ambiente virtual: `python -m venv .venv` e ative-o.  
3. Instale as dependências: `pip install -r requirements.txt`.  
4. Coloque os CSV brutos em `/dados`.  
5. Execute os scripts `01_...`, `02_...`, `03_...`.  
6. Resultados serão salvos em `/resultados`.  

---

## 👨‍💻 Autor
**Lucas Alejandro Terres**  
[LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/) • lucasalejandroterres@gmail.com  

&nbsp;  
&nbsp;

---

<a id="english"></a>

# 🗺️🛒💰Where to Shop Cheaper in Curitiba: Neighborhood Grocery Price Analysis Based on Public Data

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**Portuguese Version 🇧🇷**](#portuguese)

## 📖 About the Project
Exploratory analysis of **700 k+ grocery-price records** from Curitiba’s *Clique Economia* dataset (2024) to help shoppers find the best deals.

Price dynamics were studied along three axes:

* **Geographic** — neighborhood differences  
* **Competitive** — supermarket chain comparison  
* **Temporal** — month-by-month trends  

---

## 🎯 Key Objectives
* Map basket cost variation across neighborhoods.  
* Compare chain pricing strategies.  
* Detect highly volatile categories.  
* Provide a clear shopping guide.  

---

## 🛠️ Methodology & Pipeline
1. **Extraction** – automated CSV download.  
2. **Cleaning** – handle nulls, fix types, remove duplicates.  
3. **Enrichment** – normalize neighborhoods/chains, two-level product classification.  
4. **EDA & visualization**.  

---

## 📈 Results Showcase
* **[Neighborhood Ranking](Results/Graphs/1_grafico_ranking_bairros.png)** – Cheapest vs. priciest areas.  
* **[Competitiveness Matrix](Results/Graphs/3_grafico_matriz_competitividade_redes_macrocategoria.png)** – Chain strength by category.  
* **[Price Evolution Dashboard](Results/Graphs/painel_evolucao_subcategorias.png)** – Monthly trends.  
* **[Cheapest Chain by Neighborhood](Results/Graphs/Ranking_RedesMaisBaratas_Bairro.png)** – Best option per area.

Want everything in detail? Check the 👉 [**charts & tables folder**](Results/) — it’s all there!

---

## 🚀 How to Run
1. Clone this repo.  
2. `python -m venv .venv` and activate it.  
3. `pip install -r requirements.txt`  
4. Put raw CSVs in `/dados`.  
5. Run scripts in order.  
6. Outputs in `/resultados`.  

---

## 👨‍💻 Author
**Lucas Alejandro Terres**  
[LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/) • lucasalejandroterres@gmail.com
