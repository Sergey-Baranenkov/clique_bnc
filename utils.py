from typing import List
import numpy as np
from numpy import argsort

import networkx

# Отсортированные по весу
def sort_desc_by_weight(graph:networkx.Graph, weights: List[float]):
    return list(argsort(weights)[::-1])

def sort_combined(graph:networkx.Graph, weights: List[float]):
    new_weights = np.array(weights) / np.array([graph.degree(i) + 1 for i in range(1, len(weights) + 1)])
    return list(argsort(new_weights)[::-1])

def _find_maximal_weighted_set(graph: networkx.Graph, weights: List[float], sort_func = sort_combined):
    result = []
    deleted = [False] * len(weights)
    # Нумерация с 0
    sorted_vertices: list = sort_func(graph, weights)

    for v in sorted_vertices:
        if deleted[v]:
            continue

        result.append(v + 1)

        for neighbour in graph.neighbors(v + 1):
            deleted[neighbour - 1] = True

    return result, sum([weights[v - 1] for v in result])

def find_maximal_weighted_set(graph: networkx.Graph, weights: List[float]):
    by_weight = _find_maximal_weighted_set(graph, weights, sort_desc_by_weight)
    combined = _find_maximal_weighted_set(graph, weights, sort_combined)

    if by_weight[1] > combined[1]:
        return by_weight

    return combined

def find_maximal_set_with_vertices(graph: networkx.Graph, vertices: List[int]):
    weights = [1.0] * len(graph.nodes)
    for vertice in vertices:
        weights[vertice - 1] = float('inf')

    return find_maximal_weighted_set(graph, weights)