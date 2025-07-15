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

* **[Ranking de Bairros por Custo da Cesta Essencial](Results/Graphs/1_grafico_ranking_bairros.png)** – Os 10 bairros mais caros e mais baratos.
* **[Matriz de Competitividade: Preço por Rede e Categoria](Results/Graphs/3_grafico_matriz_competitividade_redes_macrocategoria.png)** – Competitividade entre redes em cada categoria.
* **[Evolução Temporal das Subcategorias](Results/Graphs/painel_evolucao_subcategorias.png)** – Como os preços variaram ao longo de 2024.
* **[Guia do Consumidor por Bairro](Results/Graphs/Ranking_RedesMaisBaratas_Bairro.png)** – Qual rede tem o menor preço médio em cada bairro.

---

### 📂 Quer ver todos os gráficos e planilhas de resultados?

Quer conferir todos os resultados? Dá uma olhada 👉 [**na pasta completa de gráficos e planilhas**](Results/Graphs) — tá tudo lá!

---

## 🚀 Como Executar o Projeto

1. Clone este repositório.
2. Crie um ambiente virtual (`python -m venv .venv`) e ative-o.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Coloque os arquivos de dados brutos na pasta `/dados`.
5. Execute os scripts na ordem: `01_...`, `02_...`, `03_...`.
6. Os resultados serão salvos em `/resultados`.

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

[**Portuguese Version 🇧🇷**](#️🛒💰onde-é-mais-barato-comprar-em-curitiba-análise-dos-preços-no-varejo-por-bairro-com-dados-públicos)

## 📖 About The Project

This project consists of an exploratory data analysis of price dispersion in the food retail sector of Curitiba, Brazil, using public data from the "Clique Economia" program for the year 2024. The main goal is to transform over 700,000 raw price records into actionable intelligence that can empower consumers in their purchasing decisions.

The work explores price dynamics across three main axes: **geographical**, **competitive**, and **temporal**.

---

## 🎯 Key Objectives

* Map the price variation of a consumer basket across city neighborhoods.
* Compare pricing strategies of supermarket chains.
* Identify the most volatile product categories.
* Provide a practical shopping guide for consumers.

---

## 🛠️ Methodology & Data Pipeline

1. **Extraction:** Automated download of daily CSV files.
2. **Cleaning:** Nulls, types, duplicates.
3. **Enrichment:**
   * Neighborhood normalization
   * Retail chain harmonization
   * Two-level product classification

---

## 📈 Results Showcase

* **[Neighborhood Ranking](Results/Graphs/1_grafico_ranking_bairros.png)** – Most and least expensive areas.
* **[Competitiveness Matrix](Results/Graphs/3_grafico_matriz_competitividade_redes_macrocategoria.png)** – Chain positioning by category.
* **[Price Evolution Dashboard](Results/Graphs/painel_evolucao_subcategorias.png)** – Monthly price trends.
* **[Cheapest Chain by Neighborhood](Results/Graphs/Ranking_RedesMaisBaratas_Bairro.png)** – Final consumer guide.

---

Want to check out all results?  
Browse the full set of [**charts and spreadsheets here**](Results/Graphs) — everything is ready to explore!

---

## 🚀 How to Run

1. Clone this repo.
2. Create a virtual env: `python -m venv .venv`
3. Activate and install deps: `pip install -r requirements.txt`
4. Add raw data to `/dados`
5. Run scripts in order.
6. Outputs go to `/resultados`.

---

## 👨‍💻 Author

**Lucas Alejandro Terres**  
🔗 [LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/)  
📧 lucasalejandroterres@gmail.com
