# -*- coding: utf-8 -*-
"""
Configurações globais do projeto.

Define parâmetros de plotagem, paths de saída e
configurações do OSMnx usados por todos os módulos.
"""

import os
import osmnx as ox

# Configuração global do OSMnx
ox.config(use_cache=True, log_console=True)

# Paths
OUTPUT_DIR = "output"
DATA_DIR = "data"
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")

# Criação de diretórios
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Parâmetros de plotagem
FIG_HEIGHT_DEFAULT = 6
FIG_HEIGHT_LARGE = 10
FIG_HEIGHT_HUGE = 30
DPI = 300
NODE_SIZE_DEFAULT = 4
EDGE_LINEWIDTH = 1.5
INTERSECTION_TOLERANCE = 25
NETWORK_TYPE = "drive"
PROJECTED_CRS = "epsg:3857"