# -*- coding: utf-8 -*-
"""
Catálogo de lugares utilizados nas análises.

Cada chave é um identificador curto; o valor é o nome
formal aceito pelo Nominatim/OSMnx. Organizado em
dicionários por grupo temático para facilitar reutilização.
"""

# Municípios individuais
NATAL = {
    "tibau": "Tibau do Sul, Rio Grande do Norte, Brazil",
    "extremoz": "Extremoz, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "saogoncaloamarante": "São Gonçalo do Amarante, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "natal": "Natal, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "parnamirim": "Parnamirim, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "macaiba": "Macaíba, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "espiritosnto": "Espírito Santo, Rio Grande do Norte, Brazil",
    "pedrovelho": "Pedro Velho, Rio Grande do Norte, Brazil",
    "arez": "Arez, Região Geográfica Imediata de Canguaretama, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "geoavelino": "Senador Georgino Avelino, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "goianinha": "Goianinha, Rio Grande do Norte, Brazil",
    "canguaretama": "Canguaretama, Rio Grande do Norte, Brazil",
    "vilaflor": "Vila Flor, Rio Grande do Norte, Brazil",
    "baiaformosa": "Baía Formosa, Rio Grande do Norte, Brazil",
    "nisiafloresta": "Nísia Floresta, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
    "saojosedemipibu": "São José de Mipibu, Região Geográfica Imediata de Natal, Região Geográfica Intermediária de Natal, Rio Grande do Norte, Região Nordeste, Brazil",
}

# Paraíba
PARAIBA = {
    "mataraca": "Mataraca, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Metropolitana do Vale do Mamanguape, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, Brazil",
    "riotinto": "Rio Tinto, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, 58297-000, Brazil",
    "baiadatraicao": "Baia da Traicao, Baía da Traição, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Metropolitana do Vale do Mamanguape, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, Brazil",
    "lucena": "Lucena, Região Geográfica Imediata de João Pessoa, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, Brazil",
    "mamanguape": "Mamanguape, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Metropolitana do Vale do Mamanguape, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, Brazil",
    "capim": "Capim, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Geográfica Intermediária de João Pessoa, Paraíba, Northeast Region, Brazil",
    "santarita": "Santa Rita, Região Geográfica Imediata de João Pessoa, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Região Nordeste, Brazil",
    "bayeux": "Bayeux, Região Geográfica Imediata de João Pessoa, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Região Nordeste, Brazil",
    "joaopessoa": "João Pessoa, Região Geográfica Imediata de João Pessoa, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Região Nordeste, Brazil",
    "cabedelo": "Cabedelo, Região Geográfica Imediata de João Pessoa, Região Metropolitana de João Pessoa, Região Geográfica Intermediária de João Pessoa, Paraíba, Região Nordeste, Brazil",
    "marcacao": "Marcação, Região Geográfica Imediata de Mamanguape-Rio Tinto, Região Metropolitana do Vale do Mamanguape, Região Geográfica Intermediária de João Pessoa, Paraíba, Região Nordeste, Brazil",
}

# Algarve / Portugal, foram exploradas para um saduiche em Portugal que foi cancelado em razão da pandemia de Covid-19
PORTUGAL = {
    "lagos": "Lagos, Algarve, Portugal",
    "portimao": "Portimão, Portugal",
    "albufeira": "Albufeira, Portugal",
    "faro": "Faro, Portugal",
    "olhao": "Olhão, Portugal",
    "tavira": "Tavira, Portugal",
    "vilareal": "Vila Real de Santo Antônio, Portugal",
    "loule": "Loulé, Algarve, Portugal",
    "cacela": "Vila Nova de Cacela, Portugal",
    "montegordo": "Monte Gordo, Faro, Algarve, Portugal",
    "algarve": "Algarve, Portugal",
}

# Outras cidades com classificação do Nordeste com classificação alta no MTUR 2018 e que não são capitais. Foram exploradas para comparar com Pipa, em um estudo paralelo
NORDESTE_MTUR = {
    "jericoacora": "Jericoacoara, Brazil",
    "ipojuca": "Ipojuca, Pernambuco, Brazil",
    "maragogi": "Maragogi, Microrregião do Litoral Norte Alagoano, Mesorregião Leste Alagoano, Alagoas, Brazil",
    "msaojoao": "Mata de São João, Microrregião de Catu, Região Metropolitana de Salvador, Mesorregião do Recôncavo baiano, Bahia, Northeast Region, 48280-000, Brazil",
    "cairu": "Cairu, Microrregião de Valença, Mesorregião do Sul Baiano, Bahia, Northeast Region, Brazil",
    "ilheus": "Ilhéus, Microrregião de Ilhéus-Itabuna, Mesorregião do Sul Baiano, Bahia, Northeast Region, Brazil",
}

# Macro-regiões, foram explorados vários recortes para um estudo paralelo 
MACRO = {
    "micronatal": "Microrregião de Natal, Mesorregião do Leste Potiguar, Rio Grande do Norte, Northeast Region, Brazil",
    "mesonatal": "Mesorregião do Leste Potiguar, Rio Grande do Norte, Northeast Region, Brazil",
}

# ─── Grupos de análise (combinações) ───

# Região imediata de Canguaretama (rimed), foram explorados vários recortes para um estudo paralelo 
RIMED_CANGUARETAMA = {
    "rimedcanguaretama": [
        NATAL["espiritosnto"],
        NATAL["pedrovelho"],
        NATAL["tibau"],
        NATAL["goianinha"],
        NATAL["canguaretama"],
        NATAL["vilaflor"],
        NATAL["baiaformosa"],
    ]
}

# Limites da região imediata (versão out2020), usado para comparar com mapa da calibração, baseado em mapa axial a partir de ortofotografia área de 2006 (IDEMA)
LIMITES_TIBAU_2020 = {
    "limediatotibauout2020": [
        NATAL["arez"],
        NATAL["geoavelino"],
        NATAL["tibau"],
        NATAL["vilaflor"],
        NATAL["goianinha"],
        NATAL["canguaretama"],
    ]
}

# Corredor Nísia Floresta → Lucena, foram explorados vários recortes para um estudo paralelo --- este é o recorte excluindo as capitais
NISIA_LUCENA = {
    "rnisiatolucena": [
        NATAL["nisiafloresta"],
        NATAL["baiaformosa"],
        PARAIBA["mataraca"],
        PARAIBA["riotinto"],
        PARAIBA["baiadatraicao"],
        PARAIBA["lucena"],
    ] + LIMITES_TIBAU_2020["limediatotibauout2020"]
}

# Corredor Natal → João Pessoa, este é o recorte final apresentado na tese
NATAL_JOAO_PESSOA = {
    "gnataltogjoaopessoa": [
        NATAL["extremoz"],
        NATAL["saogoncaloamarante"],
        NATAL["natal"],
        NATAL["parnamirim"],
        NATAL["macaiba"],
        NATAL["nisiafloresta"],
        NATAL["saojosedemipibu"],
        NATAL["arez"],
        NATAL["geoavelino"],
        NATAL["tibau"],
        NATAL["vilaflor"],
        NATAL["goianinha"],
        NATAL["canguaretama"],
        NATAL["baiaformosa"],
        PARAIBA["capim"],
        PARAIBA["mamanguape"],
        PARAIBA["mataraca"],
        PARAIBA["riotinto"],
        PARAIBA["baiadatraicao"],
        PARAIBA["marcacao"],
        PARAIBA["lucena"],
        PARAIBA["santarita"],
        PARAIBA["bayeux"],
        PARAIBA["joaopessoa"],
        PARAIBA["cabedelo"],
    ]
}

# Footprints — locais com análise de edifícios, exploratório, para comparar com mapa de Área Densamente Edificada do IBGE (2022). 
FOOTPRINT_PLACES = {
    **NORDESTE_MTUR,  # Maragogi, Mata de São João, Cairu, Ilhéus
    **{k: v for k, v in PORTUGAL.items() if k != "algarve"},
}
