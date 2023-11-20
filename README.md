# Web Scraping com python e load no AWS S3

## 1. Visão Geral

Esse projeto foi feito com o proposito de treinar minhas técnicas de programação utilizando python. O código apresenta como fazer Web Scraping em paginas de conteudo dinamico feitos em javasript utilizando **Python** e **Selenium**. 

Usei como dados o site da NBA para extrair informações estatísticas dos jogadores e gerar um arquivo json.

**Importante: apenas para fins educacionais**

## 2. Desenvolvimento da Solução

**Objetivo:** Extrair os dados estatísticos do site da NBA usando a biblioteca Selenium com o Python e, a partir dos dados dados extraidos, criar um arquivo JSON que será carregado no AWS S3.

> Este algoritmo foi desenvolvido para ser executado localmente, sendo o destino do arquivo JSON gerado o AWS S3

### 2.1 Extração

Utilizando a biblioteca **Selenium** as atividades dessa etapa foram divididas da seguinte maneira:

1. Configurações iniciais: 

 * Configurar um ambiente de navegação web automatizada, abre uma página específica, localiza um elemento na página pelo seu nome de classe e rola a página até que esse elemento fique visível na tela.

2. Acessar o DropDown para exibir todos os resultados da table que quero recuperar:

 * Procurar o dropdown com as opções de visualização dos dados e selecionar a Opção ALL para exibir todos os dados que quero extrair.

3. Procurar e extrair a Table de interesse com o option do Dropdown selecionado:

 * Procurar a table com os dados que quero e extrair o html usando o  `.get_attribute('outerHTML')`.
 * Parsear o HTML extraido usando a biblioteca BeautifulSoup.

4. Estruturar os dados extraídos das etapas anteriores para um dataframe do Pandas.

### 2.2 Tratamento

 1. Excluir as colunas vazias que não são importantes usando o comando da bibioteca pandas `.dropna(axis=1)`.
 2. Renomear as colunas para nomes mais legíveis usando o comando `.rename(columns={})`.
 3. Coverter o dataframe para um dicionário pandas usando o comando `.to_dict('records')`.
 4. Converter para JSON e salvar o arquivo com nome `dados.json`.
