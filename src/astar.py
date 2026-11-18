"""Part 2 - A* search algorithm.

V = number of nodes (N), E = number of directed edges (6N - 12).
Repetition counts in the comments are worst case.

Heuristics (both never overestimate, so A* still finds the shortest path):
  h_abs(i, d) = |d - i|               (given in the assignment)
  h_cut(i, d) = stronger lower bound  (our suggestion, visits fewer nodes)
"""

import heapq                                                    # min-heap (priority queue)               | 1 time
from graph import build_graph                                   # builds the city graph                   | 1 time

INF = float("inf")                                              # "no path yet" value                     | 1 time


def h_abs(i, d):
    """Heuristic from the assignment: h(i, j) = |j - i|."""
    return abs(d - i)                                           # every edge costs >= the distance it covers | 1 time


def h_cut(i, d):
    """Alternative heuristic.

    To go from i to d we must cross the "gap" between m and m+1 for every m
    between them. An edge crossing gap m costs at least (m - 2) + (m + 1) = 2m - 1,
    and one edge crosses at most 3 gaps. So take every 3rd gap and add their
    minimum costs: K = ceil(|d - i| / 3) gaps starting from max(i, d) - 1.
    """
    hi = max(i, d)                                              # larger of the two nodes                 | 1 time
    k = (abs(d - i) + 2) // 3                                   # number of gaps we sum (ceil(|d-i|/3))   | 1 time
    return k * (2 * hi - 3) - 3 * k * (k - 1)                   # sum of 2m-1 for m = hi-1, hi-4, ...     | 1 time


def astar(graph, s, d, h=h_abs, show_steps=False):
    counters = {"init": 0, "main_loop": 0, "neighbors": 0, "path": 0}  # one counter per loop block       | 1 time
    g = {}                                                      # cost from s to each node                | 1 time
    prev = {}                                                   # previous node on the best path          | 1 time
    for v in graph:                                             # visit every node                        | V times
        counters["init"] += 1                                   # count init loop                         | V times
        g[v] = INF                                              # cost unknown at start                   | V times
        prev[v] = None                                          # no previous node yet                    | V times
    g[s] = 0                                                    # source costs 0                          | 1 time
    heap = [(h(s, d), s)]                                       # heap holds (f = g + h, node)            | 1 time
    expanded = 0                                                # how many nodes were expanded            | 1 time

    while heap:                                                 # until the heap is empty                 | <= E times
        counters["main_loop"] += 1                              # count main loop                         | <= E times
        f, u = heapq.heappop(heap)                              # node with the smallest f = g + h        | <= E times, O(log V) each
        if f > g[u] + h(u, d):                                  # old (stale) heap entry?                 | <= E times
            continue                                            # skip it                                 | <= E times
        expanded += 1                                           # u is expanded now                       | <= V times
        if show_steps:                                          # print the step for the report           | <= V times
            print(f"  expand {u} (g={g[u]}, h={h(u, d)}, f={f})")  # g, h and f of u                      | <= V times
        if u == d:                                              # destination reached?                    | <= V times
            break                                               # stop, shortest path found               | 1 time
        for v, w in graph[u]:                                   # each neighbor of u                      | E times in total
            counters["neighbors"] += 1                          # count neighbor loop                     | E times
            if g[u] + w < g[v]:                                 # cheaper path to v through u?            | E times
                g[v] = g[u] + w                                 # update cost of v                        | <= E times
                prev[v] = u                                     # remember we came from u                 | <= E times
                heapq.heappush(heap, (g[v] + h(v, d), v))       # add v with f = g + h                    | <= E times, O(log V) each

    path = []                                                   # shortest path from s to d               | 1 time
    node = d                                                    # start from the destination              | 1 time
    while node is not None:                                     # walk back to the source                 | <= V times
        counters["path"] += 1                                   # count path loop                         | <= V times
        path.append(node)                                       # add node to the path                    | <= V times
        node = prev[node]                                       # go to the previous node                 | <= V times
    path.reverse()                                              # path was built backwards                | 1 time
    return path, g[d], counters, expanded                       # path, cost, loop counts, expanded nodes | 1 time


def main():
    n = int(input("N (< 20): "))                                # number of cities                        | 1 time
    s = int(input("S (default 1): ") or 1)                      # source city                             | 1 time
    d = int(input(f"D (default {n}): ") or n)                   # destination city                        | 1 time
    if not (1 <= n < 20 and 1 <= s <= n and 1 <= d <= n):       # check the input                         | 1 time
        print("Invalid input: need N < 20 and 1 <= S, D <= N")  # error message                           | 1 time
        return                                                  # stop                                    | 1 time

    graph = build_graph(n)                                      # w_ij = i + j if |i - j| <= 3            | 1 time
    for name, h in [("h = |j - i|", h_abs), ("h = cut heuristic", h_cut)]:  # try both heuristics         | 2 times
        print(f"\nA* with {name}")                              # header                                  | 2 times
        path, cost, counters, expanded = astar(graph, s, d, h, show_steps=True)  # run the algorithm      | 2 times
        print("Shortest path:", " -> ".join(map(str, path)))    # output the path                         | 2 times
        print("Total cost:", cost)                              # output the cost                         | 2 times
        print("Expanded nodes:", expanded)                      # how many nodes were visited             | 2 times
        print("Repetitions:", counters)                         # repetitions per loop                    | 2 times
        print("Total repetitions:", sum(counters.values()))     # total repetitions (all c_i = 1)         | 2 times


if __name__ == "__main__":
    main()
