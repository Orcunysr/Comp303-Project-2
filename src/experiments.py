"""Items 3 and 6: run both algorithms for large N and plot measured vs theoretical.

Runs N = 10, 50, 100, 200, 500, 1000, 2000 with S = 1, D = N.
Measured running time = total number of loop repetitions (all c_i = 1).
Theoretical running time = (V + E) * log2(V), with V = N and E = 6N - 12.
"""

import math
import os

import matplotlib.pyplot as plt

from astar import astar, h_abs, h_cut
from dijkstra import dijkstra
from graph import build_graph

N_VALUES = [10, 50, 100, 200, 500, 1000, 2000]
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "figures"))


def theoretical(n):
    v, e = n, 6 * n - 12
    return (v + e) * math.log2(v)


def run():
    rows = []
    for n in N_VALUES:
        graph = build_graph(n)
        _, cost_d, cnt_d = dijkstra(graph, 1, n)
        _, cost_a, cnt_a, exp_a = astar(graph, 1, n, h_abs)
        _, cost_c, cnt_c, exp_c = astar(graph, 1, n, h_cut)
        assert cost_d == cost_a == cost_c, "algorithms disagree on the cost"
        rows.append({
            "N": n,
            "cost": cost_d,
            "dijkstra": sum(cnt_d.values()),
            "astar_abs": sum(cnt_a.values()),
            "astar_cut": sum(cnt_c.values()),
            "expanded_abs": exp_a,
            "expanded_cut": exp_c,
            "theory": theoretical(n),
        })
    return rows


def print_table(rows):
    header = f"{'N':>5} {'cost':>9} {'Dijkstra':>9} {'A*|j-i|':>9} {'A* cut':>9} {'exp|j-i|':>9} {'exp cut':>8} {'(V+E)logV':>10}"
    print(header)
    print("-" * len(header))
    for r in rows:
        print(f"{r['N']:>5} {r['cost']:>9} {r['dijkstra']:>9} {r['astar_abs']:>9} {r['astar_cut']:>9} "
              f"{r['expanded_abs']:>9} {r['expanded_cut']:>8} {r['theory']:>10.0f}")


def plot(rows, key, label, filename):
    ns = [r["N"] for r in rows]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ns, [r[key] for r in rows], "o-", label=f"{label} (measured repetitions)")
    ax.plot(ns, [r["theory"] for r in rows], "s--", label="Theoretical (V+E) log2 V")
    ax.set_xlabel("N (number of cities)")
    ax.set_ylabel("Running time (repetitions)")
    ax.set_title(f"{label}: measured vs theoretical")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, filename), dpi=150)
    plt.close(fig)


def plot_comparison(rows):
    ns = [r["N"] for r in rows]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ns, [r["dijkstra"] for r in rows], "o-", label="Dijkstra")
    ax.plot(ns, [r["astar_abs"] for r in rows], "s-", label="A*, h = |j - i|")
    ax.plot(ns, [r["astar_cut"] for r in rows], "^-", label="A*, cut heuristic")
    ax.set_xlabel("N (number of cities)")
    ax.set_ylabel("Total repetitions")
    ax.set_title("Dijkstra vs A* (S = 1, D = N)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "comparison.png"), dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = run()
    print_table(rows)
    plot(rows, "dijkstra", "Dijkstra", "dijkstra_runtime.png")
    plot(rows, "astar_abs", "A* (h = |j - i|)", "astar_runtime.png")
    plot_comparison(rows)
    print(f"\nPlots saved to {OUT_DIR}")
