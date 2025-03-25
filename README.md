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

* Descreve quaisquer prerequisitos, bibliotecas, versão do SO, etc., que é necessário para rodar o projeto.
* exemplo. Windows 10...

### Instalação

* Como/aonde fazer o download do seu projeto/programa
* Quaisquer modificação necessária nos arquivos/diretórios

### Executando o projeto

* Como rodar o projeto/programa
* Passo a passo em tópicos (bullet points)
```
bloco de código para os comandos necessários
```

## Ajuda

Qualquer ponto importante de problemas ou erros comuns
```
comando para rodar se o programa tiver uma informação de ajuda
```

## Autores

Nomes dos desenvolvedores do projeto e informação para entrar em contato.

ex. Lucas Serra  
ex. [@LucasSerra](https://www.linkedin.com/in/lucasserra03/)

## Histórico de versões.

* 0.2
	* Ajustes de diversos bugs e otimização
* 0.1
    * Primeira versão

## Licença de uso

Esse projeto possui licença de uso [NAME HERE] - acesse o arquivo LICENSE.md para mais detalhes.

## Fontes de inspiração

Inspiração, trechos de códigos utilizados, etc.
* [readme-template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
