# Extrator de Coordenadas do Google Maps

Automação em Python que lê uma lista de links do Google Maps, acessa cada um automaticamente com Selenium e gera um arquivo CSV com as coordenadas geográficas extraídas.

## Objetivo

Este projeto foi criado para agilizar a obtenção de latitude e longitude a partir de links do Google Maps, evitando o processo manual de abrir cada link e copiar as coordenadas individualmente.

## Como funciona

O script:

1. Lê os links do arquivo `links.txt`
2. Abre cada link no Google Maps usando Selenium
3. Captura a URL final carregada
4. Tenta extrair latitude e longitude em diferentes formatos de URL
5. Salva os resultados no arquivo `pontos.csv`

## Formatos de URL suportados

O script tenta identificar coordenadas nos seguintes padrões:

- `@latitude,longitude`
- `query=latitude,longitude`

Se não conseguir extrair as coordenadas, o link ainda é salvo no CSV, mas com os campos de latitude e longitude em branco.

## Tecnologias utilizadas

- Python
- Selenium
- WebDriver Manager
- Google Chrome / ChromeDriver
- CSV

## Estrutura do projeto


.
├── extrair_coordenadas.py
├── links.txt
└── pontos.csv

Requisitos

Antes de executar, instale as dependências:

pip install selenium webdriver-manager

Também é necessário ter o Google Chrome instalado na máquina.

Como executar

Adicione os links do Google Maps no arquivo links.txt, um por linha

Execute o script:

python extrair_coordenadas.py

Ao final, será gerado o arquivo:

pontos.csv
Formato de saída

O arquivo CSV gerado contém as colunas:

Nome

Latitude

Longitude

Link Original

Exemplo:

Nome,Latitude,Longitude,Link Original
Ponto 1,-22.120000,-51.390000,https://maps.app.goo.gl/xxxxx
Observações

O script utiliza o navegador em modo headless, ou seja, sem abrir a janela do Chrome visualmente

Foi pensado para processar múltiplos links de forma automática

Pode haver falhas em alguns links dependendo de redirecionamentos ou mudanças no comportamento do Google Maps

Possíveis melhorias futuras

Exportação para PDF ou XLSX

Interface gráfica simples

Tratamento de erros mais detalhado

Leitura de nomes personalizados para os pontos

Melhor desempenho no processamento em lote

Autor

Danilo Canali
