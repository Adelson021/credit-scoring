# Probabilidade de Inadimplência

O modelo de Regressão Logística aplicado aos dados do credit_scoring.csv está estimando a probabilidade de inadimplência de um cliente com base em suas características financeiras e demográficas.

## Descrição do projeto

### 1. Introdução

Este projeto tem como objetivo desenvolver um modelo preditivo para credit scoring, utilizando Regressão Logística para estimar a probabilidade de inadimplência de clientes. O modelo será treinado com um conjunto de dados contendo informações financeiras e demográficas de diversos clientes, permitindo classificar se um indivíduo é inadimplente ou não inadimplente.

### 2. Objetivo

O objetivo principal do modelo é auxiliar instituições financeiras na avaliação de risco de crédito, reduzindo perdas financeiras e otimizando a concessão de empréstimos.

### 3. Metodologia

### 3.1. Coleta e Processamento dos Dados

Os dados utilizados foram extraídos do arquivo credit_scoring.csv, que contém variáveis relacionadas ao perfil financeiro e social dos clientes. O processamento dos dados envolveu as seguintes etapas:

Carregamento dos dados

Remoção de valores ausentes e inconsistentes

Transformação de variáveis categóricas em numéricas (One-Hot Encoding)

Escalonamento e normalização das variáveis numéricas

Remoção de outliers utilizando o método IQR

### 3.2. Modelagem Preditiva

A modelagem foi realizada utilizando Regressão Logística, devido à sua capacidade de classificação binária e interpretabilidade. As principais etapas foram:

Construção do pipeline de processamento:

Remoção de outliers

Escalonamento das variáveis numéricas

Codificação de variáveis categóricas

Divisão dos dados em treino e teste (70% para treino, 30% para teste)

Treinamento do modelo de Regressão Logística

Avaliação do desempenho do modelo

### 3.3. Métricas de Avaliação

Para medir a eficácia do modelo, utilizamos:

Acurácia: Mede a proporção de previsões corretas.

Matriz de confusão: Avalia os erros de classificação.

Precisão e Recall: Analisam a qualidade das previsões para cada classe.

F1-Score: Métrica equilibrada entre Precisão e Recall.

### 4. Resultados

O modelo de Regressão Logística conseguiu prever com eficiência a inadimplência dos clientes, alcançando uma boa taxa de acerto. O modelo final foi salvo em formato pickle (.pkl) para uso futuro.

### 5. Conclusão

O modelo desenvolvido permite a classificação de clientes de forma eficaz, auxiliando na tomada de decisão sobre concessão de crédito. Com esse sistema, é possível minimizar riscos financeiros e otimizar processos de análise de crédito.

### LINK PARA APLICAÇÃO (LIVE)


## Utilização

### Dependencias

#### 📌 Pré-requisitos
#### Sistema Operacional:

Windows 10 ou superior / Linux / macOS

#### Python:

Versão recomendada: Python 3.8 ou superior

#### Bibliotecas Necessárias:

Instale todas as bibliotecas com o seguinte comando:

bash
Copiar
Editar
pip install -r requirements.txt
Ou instale individualmente:

bash
Copiar
Editar
pip install pandas numpy scikit-learn matplotlib seaborn pycaret lightgbm pickle-mixin
#### 📦 Bibliotecas Utilizadas
pandas (análise e manipulação de dados)

numpy (operações matemáticas e vetoriais)

scikit-learn (machine learning e pré-processamento)

matplotlib e seaborn (visualização de dados)

pycaret (automação de machine learning)

lightgbm (modelo de machine learning para classificação)

pickle (salvamento e carregamento do modelo treinado)

streamlit (criação de dashboards e interfaces web para o projeto)

### Instalação

* Github

### Executando o projeto

* Streamlit run 'ProjetoFinal.py'

## Ajuda

Qualquer ponto importante de problemas ou erros comuns
```
comando para rodar se o programa tiver uma informação de ajuda
```

## Autores

Nomes dos desenvolvedores do projeto e informação para entrar em contato.

Adelson Campos Lima
[@adelson21](https://www.linkedin.com/in/adelson21/)

## Histórico de versões.

* 0.2
	* Ajustes de diversos bugs e otimização
* 0.1
    * Primeira versão

## Licença de uso

Esse projeto possui licença de uso [NAME HERE] - acesse o arquivo LICENSE.md para mais detalhes.

## Fontes de inspiração

Inspiração, trechos de códigos utilizados, etc.

