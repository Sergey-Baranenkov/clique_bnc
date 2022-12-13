import numpy as np
from utils import find_maximal_weighted_set

from parse_graph import parse_file, get_graph
from time import time

files = (
    'c-fat200-1.clq',
    'c-fat200-2.clq',
    'c-fat200-5.clq',
    'c-fat500-1.clq',
    'c-fat500-10.clq',
    'c-fat500-2.clq',
    'c-fat500-5.clq',
    'gen200_p0.9_55.clq',
    'johnson8-2-4.clq',
    'johnson8-4-4.clq',
    'johnson16-2-4.clq',
    'hamming6-2.clq',
    'hamming6-4.clq',
    'hamming8-2.clq',
    'hamming8-4.clq',
    'MANN_a9.clq',
    'san200_0.7_1.clq',
    'san200_0.9_1.clq',
    'san200_0.9_2.clq',
    'brock200_1.clq',
    'brock200_2.clq',
    'brock200_3.clq',
    'brock200_4.clq',
    'C125.9.clq',
    'gen200_p0.9_44.clq',
    'keller4.clq',
    'MANN_a27.clq',
    'MANN_a45.clq',
    'p_hat300-1.clq',
    'p_hat300-2.clq',
    'p_hat300-3.clq',
    'san200_0.7_2.clq',
    'san200_0.9_3.clq',
    'sanr200_0.7.clq',
)

result = []
for file in files:
    v, e, edges = parse_file(f'resources/{file}')
    graph = get_graph(edges)
    weights = [np.ceil(10 * i / v) * 0.1 for i in range(1, v + 1)]
    start = time()
    res, weight = find_maximal_weighted_set(graph, weights)
    print(file, 'time:', time() - start, 'weight:', weight, 'set:', res)
    #print(graph.edges(res))
