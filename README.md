# 🗺️🛒💰Onde é Mais Barato Comprar em Curitiba: Análise dos Preços no Varejo por Bairro com Dados Públicos

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**English Version 🇬🇧**](#where-to-shop-cheaper-in-curitiba-neighborhood-grocery-price-analysis-based-on-public-data)

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
1.  **Extração:** Automação da coleta de centenas de arquivos CSV diários do portal de dados abertos.
2.  **Limpeza de Dados:** Tratamento de valores nulos, correção de tipos de dados e remoção de duplicatas.
3.  **Enriquecimento e Normalização:**
    * **Normalização Geográfica:** Extração e padronização dos bairros de Curitiba.
    * **Padronização de Redes:** Unificação de nomes variantes de uma mesma rede de supermercado.
    * **Sistema de Categorização:** Classificação hierárquica em dois níveis (`categoria_n1`, `categoria_n2`) para mais de 700 mil descrições de produtos.

---

## 📈 Amostra dos Resultados

#### 🏘️ Ranking de Bairros por Custo da Cesta Essencial
*Mostra os 10 bairros mais caros e os 10 mais baratos para uma cesta padrão de produtos.*
![Ranking de Bairros](resultados/graficos/1_grafico_ranking_bairros.png)

#### 🏬 Matriz de Competitividade por Rede e Categoria
*Aponta quais redes de supermercado são mais competitivas em cada categoria de produto.*
![Matriz de Competitividade](resultados/graficos/3_grafico_matriz_competitividade.png)

#### 📊 Guia do Consumidor por Bairro
*Indica, bairro a bairro, qual rede apresenta os menores preços médios para a cesta essencial.*
![Guia por Bairro](resultados/graficos/Ranking_RedesMaisBaratas_Bairro.png)

---

### 📂 Quer ver todos os gráficos e planilhas de resultados?

Quer conferir todos os resultados? Dá uma olhada 👉 [**na pasta completa de gráficos e planilhas**](resultados/) — tá tudo lá!

---

## 🚀 Como Executar o Projeto

1.  Clone este repositório.
2.  Crie um ambiente virtual (`python -m venv .venv`) e ative-o.
3.  Instale as dependências: `pip install -r requirements.txt`.
4.  Coloque os arquivos de dados brutos na pasta `/dados`.
5.  Execute os scripts na ordem: `01_...`, `02_...`, `03_...`.
6.  Os resultados serão salvos em `/resultados`.

---

## 👨‍💻 Autor

**Lucas Alejandro Terres**
🔗 [LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/)
📧 lucasalejandroterres@gmail.com

&nbsp;
&nbsp;

---
---

&nbsp;
&nbsp;

# 🗺️🛒💰Where to Shop Cheaper in Curitiba: Neighborhood Grocery Price Analysis Based on Public Data

[<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />](https://www.python.org/)
[<img src="https://img.shields.io/badge/Pandas-1.5-150458?style=for-the-badge&logo=pandas&logoColor=white" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Matplotlib-3.7-891845?style=for-the-badge&logo=matplotlib&logoColor=white" />](https://matplotlib.org/)
[<img src="https://img.shields.io/badge/Seaborn-0.12-09435b?style=for-the-badge&logo=seaborn&logoColor=white" />](https://seaborn.pydata.org/)

[**Portuguese Version 🇧🇷**](#-onde-é-mais-barato-comprar-em-curitiba-análise-dos-preços-no-varejo-por-bairro-com-dados-públicos)

## 📖 About The Project

This project is an exploratory data analysis of food retail price dispersion in Curitiba, Brazil, using public data from the "Clique Economia" program (2024). The goal is to turn over 700,000 raw price entries into actionable insights to help consumers shop smarter.

We explored pricing dynamics along three main axes: **geographic**, **competitive**, and **temporal**.

---

## 🎯 Key Objectives

* Map cost differences for a representative basket across neighborhoods.
* Compare pricing strategies between major supermarket chains.
* Detect the most volatile product categories.
* Deliver a clear and practical shopping guide for consumers.

---

## 🛠️ Methodology & Pipeline

1.  **Extraction:** Automated CSV download from public datasets.
2.  **Cleaning:** Handle missing values, fix types, remove duplicates.
3.  **Enrichment:**
    * Normalize neighborhood names
    * Unify brand variants
    * Classify products by category (two-tier system)

---

## 📈 Results Showcase

* **[Neighborhood Ranking](resultados/graficos/1_grafico_ranking_bairros.png)** – Highlights the 10 cheapest and most expensive areas.
* **[Competitiveness Matrix](resultados/graficos/3_grafico_matriz_competitividade.png)** – Shows which chains are more competitive in each category.
* **[Cheapest Chain by Neighborhood](resultados/graficos/Ranking_RedesMaisBaratas_Bairro.png)** – Points to the most affordable supermarket per neighborhood.

Want to check out all the results? Take a look 👉 [**charts and tables folder**](resultados/) — it’s all there!

---

## 🚀 How to Run

1.  Clone this repository.
2.  Create a virtual environment: `python -m venv .venv`
3.  Activate it and install dependencies: `pip install -r requirements.txt`
4.  Add raw data to the `/dados` folder.
5.  Run the scripts in order.
6.  Outputs (tables and charts) will be saved in `/resultados`.

---

## 👨‍💻 Author

**Lucas Alejandro Terres**
🔗 [LinkedIn](https://www.linkedin.com/in/lucasalejandroterres/)
📧 lucasalejandroterres@gmail.com
