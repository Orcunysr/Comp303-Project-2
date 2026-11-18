"""Part 1 - Dijkstra's shortest path algorithm with a min-heap.

V = number of nodes (N), E = number of directed edges (6N - 12).
Repetition counts in the comments are worst case.
"""

import heapq                                                    # min-heap (priority queue)               | 1 time
from graph import build_graph                                   # builds the city graph                   | 1 time

INF = float("inf")                                              # "no path yet" value                     | 1 time


def dijkstra(graph, s, d, show_steps=False):
    counters = {"init": 0, "main_loop": 0, "neighbors": 0, "path": 0}  # one counter per loop block       | 1 time
    dist = {}                                                   # shortest known distance to each node    | 1 time
    prev = {}                                                   # previous node on the shortest path      | 1 time
    for v in graph:                                             # visit every node                        | V times
        counters["init"] += 1                                   # count init loop                         | V times
        dist[v] = INF                                           # distance unknown at start               | V times
        prev[v] = None                                          # no previous node yet                    | V times
    dist[s] = 0                                                 # source is 0 away from itself            | 1 time
    heap = [(0, s)]                                             # heap holds (distance, node)             | 1 time

    while heap:                                                 # until the heap is empty                 | <= E times
        counters["main_loop"] += 1                              # count main loop                         | <= E times
        du, u = heapq.heappop(heap)                             # node with the smallest distance         | <= E times, O(log V) each
        if du > dist[u]:                                        # old (stale) heap entry?                 | <= E times
            continue                                            # skip it                                 | <= E times
        if show_steps:                                          # print the step for the report           | <= V times
            print(f"  visit {u} (dist={du})")                   # node u is now final                     | <= V times
        if u == d:                                              # destination reached?                    | <= V times
            break                                               # stop, its distance is final             | 1 time
        for v, w in graph[u]:                                   # each neighbor of u                      | E times in total
            counters["neighbors"] += 1                          # count neighbor loop                     | E times
            if du + w < dist[v]:                                # shorter path to v through u?            | E times
                dist[v] = du + w                                # update distance of v                    | <= E times
                prev[v] = u                                     # remember we came from u                 | <= E times
                heapq.heappush(heap, (dist[v], v))              # add v to the heap                       | <= E times, O(log V) each

    path = []                                                   # shortest path from s to d               | 1 time
    node = d                                                    # start from the destination              | 1 time
    while node is not None:                                     # walk back to the source                 | <= V times
        counters["path"] += 1                                   # count path loop                         | <= V times
        path.append(node)                                       # add node to the path                    | <= V times
        node = prev[node]                                       # go to the previous node                 | <= V times
    path.reverse()                                              # path was built backwards                | 1 time
    return path, dist[d], counters                              # path, cost and loop counts              | 1 time


def main():
    n = int(input("N (< 20): "))                                # number of cities                        | 1 time
    s = int(input("S: "))                                       # source city                             | 1 time
    d = int(input("D: "))                                       # destination city                        | 1 time
    if not (1 <= n < 20 and 1 <= s <= n and 1 <= d <= n):       # check the input                         | 1 time
        print("Invalid input: need N < 20 and 1 <= S, D <= N")  # error message                           | 1 time
        return                                                  # stop                                    | 1 time

    graph = build_graph(n)                                      # w_ij = i + j if |i - j| <= 3            | 1 time
    print("Steps:")                                             # header                                  | 1 time
    path, cost, counters = dijkstra(graph, s, d, show_steps=True)  # run the algorithm                    | 1 time
    print("Shortest path:", " -> ".join(map(str, path)))        # output the path                         | 1 time
    print("Cost:", cost)                                        # output the cost                         | 1 time
    print("Repetitions:", counters)                             # repetitions per loop                    | 1 time
    print("Total repetitions:", sum(counters.values()))         # total repetitions (all c_i = 1)         | 1 time


if __name__ == "__main__":
    main()
