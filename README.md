# tessitura-viaria-osmnx
Scripts em Python desenvolvidos para capturar, filtrar (modo drive), simplificar e converter em grafo as malhas viárias de 25 municípios do recorte litorâneo de João Pessoa (PB) a Natal (RN). Inclui recortes exploratórios e de calibragem. 

# Pipeline de Extração e Processamento de Malha Viária (OSMnx)

Repositório complementar à tese de doutorado: *"Tessitura de uma arquitetura esparsa: localidades litorâneas enquanto economias de movimento"* (PPGAU/UFRN, 2025), financiada pela CAPES.

>MARTINS, Maurício Pereira. Tessitura de uma arquitetura esparsa: localidades litorâneas enquanto economias de movimento. Orientadora: Dra. Edja Bezerra Faria Trigueiro. 2025. 273f. Tese (Doutorado em Arquitetura e Urbanismo) - Centro de Tecnologia, Universidade Federal do Rio Grande do Norte, Natal, 2025.

https://repositorio.ufrn.br/handle/123456789/67269

## Descrição
Este repositório contém os scripts em Python utilizados para capturar, filtrar e processar as malhas viárias de aproximadamente 25 municípios costeiros e do entorno da BR-101, entre Natal-RN e João Pessoa-PB.

## Funcionalidades do Código
O pipeline utiliza a biblioteca `OSMnx` (Boeing, 2017) para:
1. **Captura:** Download da malha viária via OpenStreetMap para o recorte geográfico definido.
2. **Filtragem:** Seleção do modo de transporte `drive` (vias automotivas).
3. **Simplificação:** Redução de nós intermediários para limpeza topológica.
4. **Conversão:** Transformação da malha em estrutura de grafo (nós/vértices e arestas/edges) pronta para Análise da Sintaxe do Espaço.

## Relação com a Tese
Este código foi a base para a geração do dataset depositado com DOI no [Depositadados (IBICT)](https://doi.org/10.48472/deposita/MPCL1A), garantindo a total reprodutibilidade da etapa de preparação dos dados da pesquisa.

## Dependências Principais
- Python ≥ 3.10
- OSMnx ≥ 1.9.0
- NetworkX, GeoPandas, Matplotlib, NumPy, pyproj

## Instalação

```bash
git clone <url-do-repositorio>
cd urban_network_analysis
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Uso 

```bash
# Executa todas as análises
python main.py

# Apenas redes viárias
python main.py --network

# Apenas footprints de edifícios
python main.py --footprint
```
