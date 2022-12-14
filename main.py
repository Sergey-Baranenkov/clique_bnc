import cplex
from find_initial_solution import *

from utils import find_maximal_weighted_set, find_maximal_set_with_vertices
from parse_graph import *
from paint_graph import *
from cplex._internal._subinterfaces import VarTypes
import sys

sys.setrecursionlimit(11000)


# Долго и находит некорректное решение
class Solver:
    def __init__(
            self,
            graph: nx.Graph,
            colors_grouped: List[set],
            start_time: datetime,
            ILP: bool = True,
            max_recursion_depth: int = 100,
            max_second_limit: int = 300,
            tol=1e-4
    ):
        self.start_time = start_time
        self.max_second_limit = max_second_limit
        self.max_recursion_depth = max_recursion_depth
        self.one = 1 if ILP else 1.0
        self.zero = 0 if ILP else 0.0
        self.type = VarTypes.binary if ILP else VarTypes.continuous

        self.tol = tol

        # cplex
        self.cplex: cplex.Cplex = None

        self.graph = graph
        self.nodes = list(
            sorted(graph.nodes))  # networkx их пересортирует в своем порядке, храним отсортированными для норм маппинга

        # Независимые множества из раскраски
        self.ind_sets = set(map(lambda x: tuple(x), colors_grouped))

        # Размер текущей максимальной клики
        self.current_max_clique_size = 0

        # Макс клика
        self.best_solution = None

        self.branch_num = 0
        self.separation_iter = 0
        self.soft_iter = 0
        self.call_iter = 0

    def initialize_variables(self, c: cplex.Cplex):
        nodes = self.nodes
        nodes_len = len(nodes)
        # Максимизируем целевую функцию (количество вершин в клике)
        c.objective.set_sense(c.objective.sense.maximize)
        c.variables.add(
            names=[f'x{v}' for v in nodes],
            types=self.type * nodes_len,
            obj=[self.one] * nodes_len,
            ub=[self.one] * nodes_len,
            lb=[self.zero] * nodes_len
        )

    def extend_ind_sets(self):
        strategies = [nx.coloring.strategy_random_sequential,
                      nx.coloring.strategy_independent_set,
                      nx.coloring.strategy_connected_sequential_bfs,
                      nx.coloring.strategy_connected_sequential_dfs,
                      nx.coloring.strategy_saturation_largest_first,
                      nx.coloring.strategy_smallest_last,
                      nx.coloring.strategy_largest_first,
                      ]

        for strategy in strategies:
            colors = nx.coloring.greedy_color(self.graph, strategy=strategy)
            vertex_groups = defaultdict(list)
            for vertex, color in colors.items():
                vertex_groups[color].append(vertex)

            for vertex_group in vertex_groups.values():
                self.ind_sets.add(tuple(vertex_group))

    def initialize_constraints(self, c: cplex.Cplex):
        complement_graph = nx.complement(self.graph)
        complement_graph_edges = complement_graph.edges

        constraints = []

        self.extend_ind_sets()
        # Ограничения по независимым множествам
        for ind_set in self.ind_sets:
            var_names = [f'x{v}' for v in ind_set]
            constraints.append([var_names, [self.one] * len(var_names)])

        # Ограничения по дополнению графа
        for v1, v2 in complement_graph_edges:
            constraints.append([[f'x{v1}', f'x{v2}'], [self.one] * 2])

        boundaries = [self.one] * len(constraints)
        names = [f'c{i}' for i in range(len(constraints))]

        # <=
        senses = ['L'] * len(constraints)

        c.linear_constraints.add(lin_expr=constraints,
                                 senses=senses,
                                 rhs=boundaries,
                                 names=names)

    def initialize_cplex(self):
        c = cplex.Cplex()
        c.set_log_stream(None)
        c.set_results_stream(None)
        c.set_warning_stream(None)
        c.set_error_stream(None)

        self.initialize_variables(c)
        self.initialize_constraints(c)
        self.cplex = c

    def get_branching_var(self, solution: list):
        enumerated_not_ints = [x for x in enumerate(solution) if not x[1].is_integer()]
        if not len(enumerated_not_ints):
            return None

        closest_to_1 = max(enumerated_not_ints, key=lambda x: x[1], default=(None, None))
        closest_to_0 = min(enumerated_not_ints, key=lambda x: x[1], default=(None, None))

        if closest_to_0[1] < 1 - closest_to_1[1]:
            return closest_to_0[0]
        return closest_to_1[0]

    def add_branching_constraint(self, value: int, boundary: float, branch_num: int, sense: str):
        self.cplex.linear_constraints.add(lin_expr=[[[value], [self.one]]],
                                          senses=[sense],
                                          rhs=[boundary],
                                          names=[f'b_{branch_num}'])

    def go_left(self, value: int, branch_num: int, recursion_depth: int):
        self.add_branching_constraint(value, self.zero, branch_num, 'L')
        self.run(recursion_depth + 1)
        self.cplex.linear_constraints.delete(f'b_{branch_num}')

    def go_right(self, value: int, branch_num: int, recursion_depth: int):
        self.add_branching_constraint(value, self.one, branch_num, 'G')
        self.run(recursion_depth + 1)
        self.cplex.linear_constraints.delete(f'b_{branch_num}')

    def calculate_rounded_solution_clique_size(self, solution):
        return sum([1 for x in solution if x == 1])

    def rounded_solution(self, solution: List[float]):
        return list(map(lambda x: round(x, 5), solution))

    def delete_separation_constraint(self, iter_num: int):
        self.cplex.linear_constraints.delete(f'separation_{iter_num}')

    def add_separation_constraint(self, vertices: List[int], iter_num: int):
        self.cplex.linear_constraints.add(lin_expr=[[[f'x{v}' for v in vertices], [self.one] * len(vertices)]],
                                          senses=['L'],
                                          rhs=[self.one],
                                          names=[f'separation_{iter_num}'])

    def add_soft_constraint(self, vertices: List[int], iter_num: int):
        self.cplex.linear_constraints.add(lin_expr=[[[f'x{v}' for v in vertices], [self.one] * len(vertices)]],
                                          senses=['L'],
                                          rhs=[self.one],
                                          names=[f'soft_{iter_num}'])

    def remove_weak_constraints(self):
        slacks = self.cplex.solution.get_linear_slacks()
        constraint_names = self.cplex.linear_constraints.get_names()
        for i, slack in enumerate(slacks):
            name: str = constraint_names[i]
            if slack > 1e-3 and not name.startswith('b_'):
                self.cplex.linear_constraints.delete(name)

    def check_end(self):
        try:
            self.cplex.solution.get_values()
            return False
        except cplex.exceptions.CplexSolverError:
            return True

    def run(self, recursion_depth: int):
        passed = (datetime.now() - self.start_time).total_seconds()

        if recursion_depth > self.max_recursion_depth or passed > self.max_second_limit:
            return

        self.cplex.solve()
        if self.check_end():
            return

        solution = self.cplex.solution.get_values()
        solution = self.rounded_solution(solution)

        cur_objective_value = sum(solution)

        if cur_objective_value <= self.current_max_clique_size:
            return

        # Очищаем малозначительные ограничения по слаку чтобы модель не распухала
        self.call_iter += 1
        if self.call_iter % 100 == 0:
            self.remove_weak_constraints()

        # SEPARATION STEP
        # добавляем ограничения

        prev_obj_value = -1
        obj_val_repeat_iter = 0
        while obj_val_repeat_iter < 20:
            ind_set, total_weight = find_maximal_weighted_set(self.graph, solution)
            if total_weight <= 1.0 + self.tol:
                break

            self.add_separation_constraint(ind_set, self.separation_iter)

            self.separation_iter += 1

            self.cplex.solve()

            if self.check_end():
                return

            solution = self.cplex.solution.get_values()
            solution = self.rounded_solution(solution)

            cur_objective_value = sum(solution)

            if cur_objective_value <= self.current_max_clique_size:
                return

            if cur_objective_value - prev_obj_value < 0.15:
                obj_val_repeat_iter += 1
            else:
                obj_val_repeat_iter = 0

            prev_obj_value = cur_objective_value

        ## BRANCHING PART
        # Получаем индекс максимальной не целой переменной
        branching_var = self.get_branching_var(solution)

        # Если все элементы целочисленные - конец
        if branching_var is None:
            nodes = self.get_clique(solution)
            #print(len(nodes), self.check_clique(nodes))
            if self.check_clique(nodes):
                # print(
                #     'clique_size', self.calculate_rounded_solution_clique_size(solution),
                #       'current_size', self.current_max_clique_size
                #       )
                if self.calculate_rounded_solution_clique_size(solution) > self.current_max_clique_size:
                    self.current_max_clique_size = self.calculate_rounded_solution_clique_size(solution)
                    self.best_solution = solution
            else:
                subgraph = self.graph.subgraph(nodes)
                comp = networkx.complement(subgraph)
                for edge in comp.edges():
                    ind_set, _ = find_maximal_set_with_vertices(self.graph, list(edge))
                    self.soft_iter += 1
                    self.add_soft_constraint(ind_set, self.soft_iter)

                self.run(recursion_depth + 1)
        else:
            self.branch_num += 1
            cur_branch = self.branch_num
            if round(solution[branching_var]):
                self.go_right(branching_var, cur_branch, recursion_depth)
                self.go_left(branching_var, cur_branch, recursion_depth)
            else:
                self.go_left(branching_var, cur_branch, recursion_depth)
                self.go_right(branching_var, cur_branch, recursion_depth)

    def get_clique(self, solution: List[float]):
        nodes = self.nodes
        solution_idx = [v[0] for v in enumerate(solution) if v[1] == 1]
        clique = [nodes[idx] for idx in solution_idx]
        return clique

    def clique_to_solution(self, clique: List[int]):
        solution = [0] * len(self.nodes)
        for vertex in clique:
            solution[vertex - 1] = 1

        return solution

    def check_clique(self, clique: List[int]):
        clique_size = len(clique)
        clique_set = set(clique)
        for node in clique:
            edges = set(map(lambda x: x[1], self.graph.edges(node)))
            intersection = edges.intersection(clique_set)
            intersection_size = len(intersection)
            # + 1 вершина (node)
            if intersection_size + 1 != clique_size:
                return False
        return True

    def assert_clique(self, clique: List[int]):
        result = self.check_clique(clique)

        if not result:
            raise Exception('Solution is not a clique!')

    def solve(self):
        initial_clique = find_initial_solution(self.graph)
        self.assert_clique(initial_clique)
        initial_solution = self.clique_to_solution(initial_clique)
        self.best_solution = initial_solution
        self.current_max_clique_size = len(initial_clique)

        self.initialize_cplex()
        self.run(0)
        clique = self.get_clique(self.best_solution)
        self.assert_clique(clique)

        return clique, len(clique)


def main():
    easy = (
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
    )

    hard = (
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

    files = {
        'easy': easy,
        'hard': hard,
    }
    for type_of_graphs, filenames in files.items():
        print(type_of_graphs)
        for filename in filenames:
            # Парсим и строим граф
            v, e, edges = parse_file(f'resources/{filename}')

            start = datetime.now()
            # Начальная раскраска графа для независимых множеств
            current_color, colors_grouped = paint_graph(v, edges)
            graph = get_graph(edges)

            # Получаем решение
            solver = Solver(graph, colors_grouped, start_time=start, ILP=False, max_recursion_depth=10000,
                            max_second_limit=7200)
            clique, clique_size = solver.solve()

            execution_time = (datetime.now() - start).total_seconds()

            print(filename, float('{:.5f}'.format(execution_time)), clique_size, ','.join(map(str, clique)), sep=';')


if __name__ == '__main__':
    main()
