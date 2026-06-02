# -*- coding: utf-8 -*-
"""
Funções para obtenção e análise de footprints de edifícios via OSMnx.
"""

import os
import osmnx as ox

from config import DATA_DIR, IMAGES_DIR


def fetch_building_footprints(place_query: str, retain_invalid: bool = True):
    """Baixa os polígonos de edifícios de um lugar."""
    return ox.footprints.footprints_from_place(
        place_query,
        footprint_type="building",
        retain_invalid=retain_invalid,
    )


def project_footprints(gdf):
    """Projeta o GeoDataFrame de footprints para CRS métrico."""
    return ox.project_gdf(gdf)


def plot_footprints(gdf_proj, filename: str, dpi: int = 600) -> None:
    """Plota e salva os footprints sobre fundo escuro."""
    filepath = os.path.join(IMAGES_DIR, filename)
    fig, ax = ox.footprints.plot_footprints(
        gdf_proj,
        bgcolor="#333333",
        color="w",
        save=True,
        show=False,
        close=True,
        filepath=filepath,
        dpi=dpi,
    )


def save_footprints(gdf, filename: str) -> None:
    """Salva os footprints como shapefile (sem coluna 'nodes')."""
    if "nodes" in gdf.columns:
        gdf = gdf.drop(labels="nodes", axis=1)
    gdf.to_file(os.path.join(DATA_DIR, f"{filename}.shp"))


def get_place_boundary(place_query: str):
    """Retorna o polígono do limite administrativo de um lugar."""
    return ox.project_gdf(ox.gdf_from_place(place_query))


def compute_building_coverage_ratio(place_query: str, gdf_proj) -> float:
    """
    Calcula a proporção do território coberta por edifícios.

    Returns
    -------
    ratio : float
        Área de edifícios / área total do polígono.
    """
    building_area = gdf_proj.area.sum()
    boundary = get_place_boundary(place_query)
    total_area = boundary.area.iloc[0]
    return building_area / total_area