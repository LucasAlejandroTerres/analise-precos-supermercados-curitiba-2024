# 🗺️🛒💰Onde é Mais Barato Comprar em Curitiba: Análise dos Preços no Varejo por Bairro com Dados Públicos

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**English Version 🇬🇧**](#english-version)

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

O projeto foi desenvolvido em Python e seguiu um robusto pipeline de ETL (Extração, Transformação e Carga) para garantir a qualidade e a consistência dos dados. As principais etapas foram:
1. **Extração:** Automação da coleta de centenas de arquivos CSV diários do portal de dados abertos.
2. **Limpeza de Dados:** Tratamento de valores nulos, correção de tipos de dados e remoção de duplicatas.
3. **Enriquecimento e Normalização:**
   * **Normalização Geográfica:** Extração e padronização dos bairros de Curitiba.
   * **Padronização de Redes:** Unificação de nomes variantes de uma mesma rede de supermercado.
   * **Sistema de Categorização:** Desenvolvimento de um classificador hierárquico (`categoria_n1`, `categoria_n2`) baseado em um sistema de regras de dupla camada para classificar mais de 700.000 descrições de produtos.

---

## 📈 Amostra dos Resultados

* **[Ranking de Bairros por Custo da Cesta Essencial](./results/1_grafico_ranking_bairros.png)**  
  Comparação entre os 10 bairros mais caros e mais baratos para uma cesta padrão.

* **[Matriz de Competitividade: Preço por Rede e Categoria](./results/3_grafico_matriz_competitividade_redes_macrocategoria.png)**  
  Heatmap que revela o posicionamento de cada rede de supermercado.

* **[Evolução Temporal das Principais Subcategorias](./results/painel_evolucao_subcategorias.png)**  
  Visualização da jornada de preços das 12 subcategorias mais relevantes ao longo de 2024.

* **[Guia Prático: A Rede Mais Barata por Bairro](./results/Ranking_RedesMaisBaratas_Bairro.png)**  
  Tabela final indicando a rede com menor custo médio por bairro.

---

### 📂 Quer ver todos os gráficos e planilhas de resultados?

Quer conferir todos os resultados? Dá uma olhada 👉 [**Clique aqui para acessar a pasta `/results`**](./results) — tem tudo lá: gráficos, tabelas e planilhas do projeto.

---

## 🚀 Como Executar o Projeto

1. Clone este repositório.
2. Crie um ambiente virtual (`python -m venv .venv`) e ative-o.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Coloque os arquivos de dados brutos na pasta `/dados`.
5. Execute os scripts na ordem: `01_...`, `02_...`, `03_...`.
6. Os resultados serão gerados na pasta `/resultados`.

---

## 👨‍💻 Autor

**Lucas Alejandro Terres**  
🔗 [LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/)  
📧 lucasalejandroterres@gmail.com

&nbsp;  
&nbsp;  

---

<a name="english-version"></a>

# 🗺️🛒💰Where to Shop Cheaper in Curitiba: Neighborhood Grocery Price Analysis Based on Public Data

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**Portuguese Version 🇧🇷**](#️-onde-é-mais-barato-comprar-em-curitiba-análise-dos-preços-no-varejo-por-bairro-com-dados-públicos)

## 📖 About The Project

This project consists of an exploratory data analysis of price dispersion in the food retail sector of Curitiba, Brazil, using public data from the "Clique Economia" program for the year 2024. The main goal is to transform over 700,000 raw price records into actionable intelligence that can empower consumers in their purchasing decisions.

The work explores price dynamics across three main axes: **geographical** (comparing neighborhoods), **competitive** (comparing supermarket chains), and **temporal** (analyzing price evolution over the months).

---

## 🎯 Key Objectives

* Map the cost variation of a representative consumer basket across different city neighborhoods.
* Compare the price positioning of the main supermarket chains.
* Identify the product categories with the highest price volatility.
* Deliver a practical guide for consumers in Curitiba.

---

## 🛠️ Methodology & Data Pipeline

1. **Extraction:** Automated download of daily CSV files from the open data portal.
2. **Cleaning:** Null handling, type fixing, and deduplication.
3. **Enrichment:**
   * **Neighborhood Normalization**
   * **Retail Chain Harmonization**
   * **Hierarchical Product Classification**

---

## 📈 Results Showcase

* **[Neighborhood Ranking](./results/1_grafico_ranking_bairros.png)** – 10 most and least expensive neighborhoods.
* **[Competitiveness Matrix](./results/3_grafico_matriz_competitividade_redes_macrocategoria.png)** – Heatmap showing pricing strength by chain.
* **[Price Evolution Dashboard](./results/painel_evolucao_subcategorias.png)** – Price behavior over time.
* **[Cheapest Chain by Neighborhood](./results/Ranking_RedesMaisBaratas_Bairro.png)** – Final table with consumer guide.

---

Want to check out all the results?  
Take a look 👉 [**Full results folder here**](./results) — it's all there: plots, tables, and CSVs.

---

## 🚀 How to Run

1. Clone this repository.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it and run: `pip install -r requirements.txt`
4. Add your data to the `/dados` folder.
5. Run the scripts in order.
6. Outputs will be saved in `/resultados`.

---

## 👨‍💻 Author

**Lucas Alejandro Terres**  
🔗 [LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/)  
📧 lucasalejandroterres@gmail.com
