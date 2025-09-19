# Scraping-fbref

Descrição Geral: Este projeto realiza o processo de web scraping do site FBref para coletar estatísticas de joadores de futebol (com ênfase na métrica de percentil), organiza os dados em arquivos CSV e gera visualizações comparativas.

## O projeto é dividido em duas funcionalidades
- Scrap dos dados de um atleta;
- Comparação e identificação de similaridade entre atletas



# Scrap dos Dados de um Atleta - fbrefScrap.py
Nesta etapa, coletamos os percentis de um único atleta diretamente do FBref.
Utilizamos Selenium para carregar páginas dinâmicas e BeautifulSoup para extrair os dados.

## Explicação Do Código
- Conecta à página do FBref usando Selenium
- Aguarda 5 segundos para carregar o conteúdo dinâmico
- Usa BeautifulSoup para extrair estatísticas, valores por 90 minutos e percentis
- Cria um DataFrame com colunas “Estatística”, “Por 90” e “Percentil”
- Salva os dados em um CSV



# Extração Simultânea - fbrefPerc.py
Aqui fazemos o scraping de dois jogadores simultaneamente, salvando tudo em um único CSV para análise comparativa.

## Explicação Do Código
- Percorre um dicionário com nome do jogador e link do FBref
- Para cada jogador, aplica a função de scrap e insere uma coluna “Jogador”
- Junta todos os DataFrames em um único arquivo CSV (jogadores.csv)


# Visualização - Comparação e Gráfico de Similaridade - fbrefComp.py
Nesta etapa, carregamos o arquivo jogadores.csv e criamos um gráfico para comparar o percentil dos dois jogadores em cada estatística disponível e identificar a porcentagem de semelhança entre eles.

## Explicação Do Código
Carrega o arquivo jogadores.csv
Converte coluna “Percentil” para numérico
Cria uma tabela pivô com jogadores nas linhas e estatísticas nas colunas
Seleciona dois jogadores para comparação
Calcula a similaridade dos atletas usando (Mean Absolute Difference).
Monta um gráfico de barras para visualizar as estatísticas lado a lado


# O que é percentil?
Os percentis são calculados comparando as estatísticas de um jogador com as dos jogadores do mesmo grupo de comparação. Por exemplo, Kaio Jorge tem o percentil 94 em 'assists', quer dizer então que ele dar mais assistências que 94% dos atacantes das principais ligas do mundo. 
