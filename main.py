# -*- coding: utf-8 -*-
"""
Script principal: orquestra as análises de rede e footprint.

Uso:
    python main.py              # executa tudo
    python main.py --network    # só análise de redes
    python main.py --footprint  # só análise de footprints
"""

import argparse
import sys
import osmnx as ox
import networkx as nx

from config import OUTPUT_DIR
from places import (
    NATAL,
    LIMITES_TIBAU_2020,
    NATAL_JOAO_PESSOA,
    FOOTPRINT_PLACES,
)
from network_analysis import (
    fetch_and_project,
    compute_graph_area,
    compute_basic_stats,
    compute_extended_stats,
    compute_edge_centrality,
    centrality_to_edge_colors,
    plot_centrality_edges,
    save_graph_artifacts,
    plot_intersections,
    plot_node_types,
    plot_graph_plain,
    plot_line_graph,
)
from footprint_analysis import (
    fetch_building_footprints,
    project_footprints,
    plot_footprints,
    save_footprints,
    compute_building_coverage_ratio,
)


def analyze_single_place(name: str, place_query: str, suffix: str = "") -> None:
    """
    Executa a análise completa de rede para um único lugar.

    Parameters
    ----------
    name : str
        Identificador curto usado no nome dos arquivos.
    place_query : str
        Nome aceito pelo Nominatim.
    suffix : str
        Sufixo opcional para os arquivos de saída.
    """
    print(f"\n{'='*60}")
    print(f"▶ {name}: {place_query}")
    print("="*60)

    try:
        G_proj, G_raw = fetch_and_project(place_query)
    except Exception as e:
        print(f"  ❌ Falha ao baixar grafo: {e}")
        return

    # ── Área e estatísticas básicas ──
    area = compute_graph_area(G_proj)
    stats = compute_basic_stats(G_proj, area=area)
    print(f"  Área convexa: {area:,.0f} m²")
    for k, v in list(stats.items())[:5]:
        print(f"  {k}: {v}")

    # ── Plotagens básicas ──
    plot_node_types(G_proj, f"nodes_types-{name}{suffix}")
    plot_graph_plain(G_proj, f"graph_plain-{name}{suffix}")
    plot_intersections(G_proj, f"intersections-{name}{suffix}")
    plot_line_graph(G_proj, f"line_graph-{name}{suffix}")

    # ── Centralidades de arestas ──
    print("  Calculando centralidades...")
    metrics = {
        "cc": ("closeness", "nipy_spectral"),
        "cc_jet": ("closeness", "jet"),
        "bc": ("betweenness", "jet"),
        "degree": ("degree", "jet"),
        "eccentricity": ("eccentricity", "jet"),
    }
    for metric_key, (metric, cmap) in metrics.items():
        centrality = compute_edge_centrality(G_proj, metric=metric)
        colors, values = centrality_to_edge_colors(G_proj, centrality, cmap_name=cmap)
        plot_centrality_edges(
            G_proj,
            colors,
            cmap_name=cmap,
            output_name=f"edge_{metric_key}-{name}{suffix}",
        )

    # ── Salvar grafo com atributos ─
    for metric_key, (metric, _) in metrics.items():
        centrality = compute_edge_centrality(G_proj, metric=metric)
        nx.set_edge_attributes(G_proj, centrality, f"e_{metric_key}")

    save_graph_artifacts(G_proj, f"edge_centrality-{name}{suffix}")


def run_network_analysis() -> None:
    """Analisa grafos de todos os lugares definidos."""

    # ── Exemplo 1: análise exploratória de Tibau do Sul ──
    print("\n🟢 Análise exploratória: Tibau do Sul")
    analyze_single_place("tibau", "Tibau do Sul, Brazil", suffix="-exploratory")

    # ── Exemplo 2: análise de grupos ──
    for group_dict in [LIMITES_TIBAU_2020, NATAL_JOAO_PESSOA]:
        for group_key, places_list in group_dict.items():
            if isinstance(places_list, list):
                # Junta múltiplos lugares em um único polígono
                combined_query = ",".join(places_list)
                analyze_single_place(group_key, combined_query, suffix="-group")
            else:
                analyze_single_place(group_key, places_list)


def run_footprint_analysis() -> None:
    """Analisa footprints de edifícios dos lugares definidos."""
    for name, place_query in FOOTPRINT_PLACES.items():
        print(f"\n Footprint: {name} — {place_query}")
        try:
            gdf = fetch_building_footprints(place_query)
            gdf_proj = project_footprints(gdf)
            plot_footprints(gdf_proj, f"footprints-{name}")
            save_footprints(gdf, f"footprints-{name}")

            ratio = compute_building_coverage_ratio(place_query, gdf_proj)
            print(f"  Cobertura de edifícios: {ratio:.2%}")
        except Exception as e:
            print(f"  ❌ Falha: {e}")


def main():
    parser = argparse.ArgumentParser(description="Análise de redes urbanas e footprints.")
    parser.add_argument("--network", action="store_true", help="Executa apenas análise de redes.")
    parser.add_argument("--footprint", action="store_true", help="Executa apenas análise de footprints.")
    args = parser.parse_args()

    if not (args.network or args.footprint):
        args.network = True
        args.footprint = True

    if args.network:
        run_network_analysis()

    if args.footprint:
        run_footprint_analysis()

    print(f"\n✅ Concluído. Resultados em {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
