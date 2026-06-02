# -*- coding: utf-8 -*-
"""
Funções de análise de redes viárias usando OSMnx e NetworkX.

Responsável por baixar, projetar, calcular centralidades e
exportar grafos urbanos.
"""

import networkx as nx
import numpy as np
import osmnx as ox
import matplotlib.cm as cm
import matplotlib.colors as mcolors

from config import (
    PROJECTED_CRS, NETWORK_TYPE,
    FIG_HEIGHT_DEFAULT, FIG_HEIGHT_LARGE, FIG_HEIGHT_HUGE,
    DPI, NODE_SIZE_DEFAULT, EDGE_LINEWIDTH,
    INTERSECTION_TOLERANCE, OUTPUT_DIR,
)


def fetch_and_project(place_query: str) -> tuple:
    """
    Baixa o grafo viário de um lugar e o projeta em CRS métrico.

    Parameters
    ----------
    place_query : str
        Nome do lugar conforme aceito pelo Nominatim.

    Returns
    -------
    G : networkx.MultiDiGraph
        Grafo projetado.
    G_unprojected : networkx.MultiDiGraph
        Grafo original (WGS84).
    """
    G = ox.graph_from_place(place_query, network_type=NETWORK_TYPE, simplify=True)
    G_proj = ox.project_graph(G, to_crs=PROJECTED_CRS)
    return G_proj, G


def compute_graph_area(G_proj) -> float:
    """Retorna a área convexa do grafo em metros quadrados."""
    nodes = ox.graph_to_gdfs(G_proj, edges=False)
    return nodes.unary_union.convex_hull.area


def compute_basic_stats(G, area: float = None) -> dict:
    """Estatísticas básicas do grafo (densidade, entre outros)."""
    return ox.basic_stats(
        G,
        area=area,
        clean_intersects=True,
        circuity_dist="euclidean",
    )


def compute_extended_stats(G: nx.Graph) -> dict:
    """Estatísticas topológicas avançadas (excentricidade, betweenness, etc)."""
    return ox.extended_stats(G, ecc=True, bc=True, cc=True)


def compute_edge_centrality(G: nx.Graph, metric: str = "closeness") -> dict:
    """
    Calcula uma métrica de centralidade por aresta usando o line graph.

    Parameters
    ----------
    G : networkx.Graph
        Grafo original (MultiGraph).
    metric : str
        Uma entre 'closeness', 'betweenness', 'degree', 'eccentricity'.
    """
    line_G = nx.line_graph(G).to_undirected()
    metric_func = {
        "closeness":    nx.closeness_centrality,
        "betweenness":  nx.betweenness_centrality,
        "degree":       nx.degree_centrality,
        "eccentricity": nx.eccentricity,
    }
    if metric not in metric_func:
        raise ValueError(f"Métrica '{metric}' não suportada.")

    return metric_func[metric](line_G)


def centrality_to_edge_colors(G: nx.Graph, centrality_dict: dict, cmap_name="nipy_spectral"):
    """
    Mapeia valores de centralidade em cores RGBA para cada aresta.
    """
    ev = [centrality_dict[edge + (0,)] for edge in G.edges()]
    norm = mcolors.Normalize(vmin=min(ev), vmax=max(ev))
    cmap = cm.ScalarMappable(norm=norm, cmap=getattr(cm, cmap_name))
    return [cmap.to_rgba(v) for v in ev], ev


def plot_centrality_edges(
    G: nx.Graph,
    edge_colors: list,
    cmap_name: str,
    output_name: str,
    fig_height: float = FIG_HEIGHT_DEFAULT,
):
    """Plota o grafo colorido por centralidade de arestas."""
    fig, ax = ox.plot_graph(
        G,
        bgcolor="w",
        axis_off=True,
        node_size=0,
        edge_color=edge_colors,
        edge_linewidth=EDGE_LINEWIDTH,
        edge_alpha=1,
        fig_height=fig_height,
        save=True,
        close=True,
        file_format="png",
        filepath=f"{OUTPUT_DIR}/{output_name}.png",
        dpi=DPI,
    )


def save_graph_artifacts(G: nx.Graph, prefix: str) -> None:
    """Exporta o grafo em Shapefile e GraphML."""
    ox.save_graph_shapefile(G, filename=f"{OUTPUT_DIR}/Gsimplify_{prefix}")
    ox.save_graphml(G, filename=f"{OUTPUT_DIR}/G_{prefix}.graphml", gephi=True)


def plot_intersections(G: nx.Graph, output_name: str) -> None:
    """Plota as interseções limpas do grafo."""
    intersections = ox.clean_intersections(G, tolerance=INTERSECTION_TOLERANCE, dead_ends=False)
    points = np.array([pt.xy for pt in intersections])

    fig, ax = ox.plot_graph(
        G,
        fig_height=FIG_HEIGHT_LARGE,
        show=True,
        close=False,
        node_alpha=0,
        save=True,
        file_format="png",
        filepath=f"{OUTPUT_DIR}/{output_name}.png",
    )
    ax.scatter(x=points[:, 0], y=points[:, 1], zorder=2, color="#66ccff", edgecolors="k")


def plot_node_types(G: nx.Graph, output_name: str) -> None:
    """
    Plota o grafo distinguindo nós terminais (dead-ends) de nós de passagem.
    """
    node_colors = [
        "blue" if ox.is_endpoint(G, node) else "red"
        for node in G.nodes()
    ]
    fig, ax = ox.plot_graph(
        G,
        node_color=node_colors,
        node_zorder=3,
        save=True,
        file_format="png",
        filepath=f"{OUTPUT_DIR}/{output_name}.png",
    )


def plot_graph_plain(G: nx.Graph, output_name: str, fig_height: float = FIG_HEIGHT_HUGE) -> None:
    """Plota o grafo com visual padrão (nós laranja, bordas pretas)."""
    fig, ax = ox.plot_graph(
        G,
        fig_height=fig_height,
        node_color="orange",
        node_size=30,
        node_zorder=2,
        node_edgecolor="k",
        save=True,
        file_format="png",
        filepath=f"{OUTPUT_DIR}/{output_name}.png",
    )


def plot_line_graph(G: nx.Graph, output_name: str) -> None:
    """Plota o line graph (arestas viram nós)."""
    line_G = nx.line_graph(G).to_undirected()
    fig, ax = ox.plot_graph(
        line_G,
        fig_height=FIG_HEIGHT_DEFAULT,
        save=True,
        close=True,
        file_format="png",
        filepath=f"{OUTPUT_DIR}/{output_name}.png",
        node_size=NODE_SIZE_DEFAULT,
        dpi=DPI,
    )