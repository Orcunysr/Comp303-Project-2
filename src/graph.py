"""City graph used by both Dijkstra and A*.

Nodes are cities 1..N. There is an edge between i and j if |i - j| <= 3
and i != j. The edge weight (travel time) is w_ij = i + j.
"""

MAX_HOP = 3  # an edge exists when |i - j| <= MAX_HOP


def weight(i, j):
    """Travel time between cities i and j (infinity if not connected)."""
    if i != j and abs(i - j) <= MAX_HOP:
        return i + j
    return float("inf")


def build_graph(n):
    """Return the graph as an adjacency list: {node: [(neighbor, weight), ...]}."""
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(max(1, i - MAX_HOP), min(n, i + MAX_HOP) + 1):
            if i != j:
                graph[i].append((j, weight(i, j)))
    return graph


def print_graph(graph):
    """Print each node with its neighbors and edge weights."""
    for node, edges in graph.items():
        neighbors = ", ".join(f"{j}(w={w})" for j, w in edges)
        print(f"{node:>4} -> {neighbors}")


if __name__ == "__main__":
    n = int(input("N: "))
    g = build_graph(n)
    print_graph(g)
    edge_count = sum(len(edges) for edges in g.values())
    print(f"\nNodes: {n}, directed edges: {edge_count}")
